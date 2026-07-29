#!/usr/bin/env python3
"""Extract PDF text into auditable units for downstream LLM analysis.

The output is intentionally source-first: every sentence receives a stable ID
with page and section metadata so a note or translation can be checked against
the original PDF instead of relying on a lossy whole-document summary.
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Iterable, Literal


SectionKind = Literal[
    "title",
    "abstract",
    "introduction",
    "results",
    "methods",
    "discussion",
    "figures_tables",
    "references",
    "supplementary",
    "other",
]


SECTION_PATTERNS: list[tuple[SectionKind, re.Pattern[str]]] = [
    ("abstract", re.compile(r"^(abstract|summary)\b", re.I)),
    ("introduction", re.compile(r"^(introduction|背景|引言)\b", re.I)),
    ("results", re.compile(r"^(results|result|findings|结果)\b", re.I)),
    (
        "methods",
        re.compile(
            r"^(methods?|materials and methods|star methods|method details|"
            r"experimental procedures|统计分析|方法|材料与方法)\b",
            re.I,
        ),
    ),
    ("discussion", re.compile(r"^(discussion|conclusion|conclusions|讨论|结论)\b", re.I)),
    (
        "figures_tables",
        re.compile(
            r"^((figure|fig\.)\s*\d+\.\s+\S|table\s+\d+\.\s+\S|"
            r"extended data\s+\d+\.\s+\S|图\s*\d+\.\s+\S|表\s*\d+\.\s+\S)",
            re.I,
        ),
    ),
    (
        "references",
        re.compile(r"^(references|bibliography|参考文献|acknowledgements?)\b", re.I),
    ),
    (
        "supplementary",
        re.compile(r"^(supplementary|supplemental|supplementary information)\b", re.I),
    ),
]

SENTENCE_END_RE = re.compile(
    r"(?<=[.!?。！？])\s+(?=(?:[A-Z0-9(]|[\u4e00-\u9fff]))"
)
SOFT_HYPHEN_RE = re.compile(r"(?<=[A-Za-z])-\s*\n\s*(?=[a-z])")
LINEBREAK_RE = re.compile(r"\s*\n\s*")
SPACES_RE = re.compile(r"[ \t]+")


@dataclass(frozen=True)
class TextLine:
    page: int
    block: int
    line: int
    text: str
    bbox: tuple[float, float, float, float] | None = None


@dataclass(frozen=True)
class Sentence:
    id: str
    page: int
    section: SectionKind
    heading: str
    text: str


@dataclass(frozen=True)
class PdfTextDocument:
    source_pdf: str
    page_count: int
    extraction_engine: str
    pages: list[dict[str, Any]]
    sentences: list[Sentence]
    section_sentence_counts: dict[str, int]


@dataclass(frozen=True)
class TextBlock:
    block: int
    text: str
    bbox: tuple[float, float, float, float]
    lines: list[str]


def clean_line(text: str) -> str:
    text = text.replace("\u00ad", "")
    text = SPACES_RE.sub(" ", text)
    return text.strip()


def reading_order_blocks(blocks: list[TextBlock], page_width: float, page_height: float) -> list[TextBlock]:
    """Return a conservative reading order for common scientific PDF layouts.

    PyMuPDF's default y/x sorting often interleaves two-column articles. This
    heuristic keeps top full-width material first, then reads left and right
    columns top-to-bottom, and finally lower full-width captions/tables.
    """

    if not blocks:
        return []

    full_width_threshold = page_width * 0.62
    top_band = page_height * 0.22
    midpoint = page_width / 2

    top_full: list[TextBlock] = []
    lower_full: list[TextBlock] = []
    left: list[TextBlock] = []
    right: list[TextBlock] = []

    for block in blocks:
        x0, y0, x1, _ = block.bbox
        width = x1 - x0
        if width >= full_width_threshold:
            if y0 <= top_band:
                top_full.append(block)
            else:
                lower_full.append(block)
        elif (x0 + x1) / 2 < midpoint:
            left.append(block)
        else:
            right.append(block)

    by_position = lambda block: (block.bbox[1], block.bbox[0], block.block)
    return (
        sorted(top_full, key=by_position)
        + sorted(left, key=by_position)
        + sorted(right, key=by_position)
        + sorted(lower_full, key=by_position)
    )


def normalize_paragraph(text: str) -> str:
    text = SOFT_HYPHEN_RE.sub("", text)
    text = LINEBREAK_RE.sub(" ", text)
    text = SPACES_RE.sub(" ", text)
    return text.strip()


def looks_like_heading(text: str) -> bool:
    normalized = clean_line(text).strip(":")
    if not normalized:
        return False
    if len(normalized) > 120:
        return False
    if any(pattern.match(normalized) for _, pattern in SECTION_PATTERNS):
        return True
    if re.match(r"^\d+(\.\d+)*[.)]\s+[A-Z][A-Za-z]", normalized):
        return True
    words = re.findall(r"[A-Za-z]+", normalized)
    if 1 <= len(words) <= 12 and normalized[:1].isupper():
        lower_words = sum(1 for word in words if word[:1].islower())
        return lower_words <= max(1, len(words) // 3)
    return False


def classify_heading(text: str, current: SectionKind) -> SectionKind:
    normalized = clean_line(text).strip(":")
    for kind, pattern in SECTION_PATTERNS:
        if pattern.match(normalized):
            return kind
    return current


def paragraphize_lines(lines: list[TextLine]) -> list[dict[str, Any]]:
    paragraphs: list[dict[str, Any]] = []
    current: list[TextLine] = []

    def flush() -> None:
        nonlocal current
        if not current:
            return
        text = normalize_paragraph("\n".join(line.text for line in current))
        if text:
            paragraphs.append(
                {
                    "page": current[0].page,
                    "start_line": current[0].line,
                    "end_line": current[-1].line,
                    "text": text,
                }
            )
        current = []

    for line in lines:
        text = line.text
        if not text:
            flush()
            continue
        if looks_like_heading(text):
            flush()
            paragraphs.append(
                {
                    "page": line.page,
                    "start_line": line.line,
                    "end_line": line.line,
                    "text": text,
                    "is_heading": True,
                }
            )
            continue
        current.append(line)
        if re.search(r"[.!?。！？]\s*$", text):
            flush()
    flush()
    return paragraphs


def split_sentences(text: str) -> list[str]:
    text = normalize_paragraph(text)
    if not text:
        return []
    parts = SENTENCE_END_RE.split(text)
    sentences = [part.strip() for part in parts if part.strip()]
    if len(sentences) == 1 and len(sentences[0]) > 900:
        return split_long_sentence(sentences[0])
    return sentences


def split_long_sentence(text: str, max_chars: int = 700) -> list[str]:
    chunks: list[str] = []
    current = ""
    for piece in re.split(r"(?<=[;,；:：])\s+", text):
        if current and len(current) + len(piece) + 1 > max_chars:
            chunks.append(current.strip())
            current = piece
        else:
            current = f"{current} {piece}".strip()
    if current:
        chunks.append(current.strip())
    return chunks or [text]


def extract_with_pymupdf(pdf_path: Path) -> tuple[list[dict[str, Any]], int, str]:
    import fitz

    doc = fitz.open(pdf_path)
    pages: list[dict[str, Any]] = []
    for page_index, page in enumerate(doc, start=1):
        raw = page.get_text("dict", sort=False)
        page_width = float(page.rect.width)
        page_height = float(page.rect.height)
        text_blocks: list[TextBlock] = []
        for block_no, block in enumerate(raw.get("blocks", []), start=1):
            block_lines: list[str] = []
            for line in block.get("lines", []):
                spans = [span.get("text", "") for span in line.get("spans", [])]
                text = clean_line("".join(spans))
                if text:
                    block_lines.append(text)
            if not block_lines:
                continue
            bbox = tuple(round(float(value), 2) for value in block.get("bbox", ()))
            if len(bbox) != 4:
                continue
            text_blocks.append(
                TextBlock(
                    block=block_no,
                    text=normalize_paragraph("\n".join(block_lines)),
                    bbox=bbox,
                    lines=block_lines,
                )
            )

        lines: list[TextLine] = []
        line_no = 0
        for block in reading_order_blocks(text_blocks, page_width, page_height):
            for text in block.lines:
                if not text:
                    continue
                line_no += 1
                lines.append(
                    TextLine(
                        page=page_index,
                        block=block.block,
                        line=line_no,
                        text=text,
                        bbox=block.bbox,
                    )
                )
        pages.append(
            {
                "page": page_index,
                "width": round(page_width, 2),
                "height": round(page_height, 2),
                "lines": [asdict(line) for line in lines],
                "paragraphs": paragraphize_lines(lines),
            }
        )
    return pages, len(doc), "pymupdf"


def extract_with_pypdf(pdf_path: Path) -> tuple[list[dict[str, Any]], int, str]:
    from pypdf import PdfReader

    reader = PdfReader(str(pdf_path))
    pages: list[dict[str, Any]] = []
    for page_index, page in enumerate(reader.pages, start=1):
        raw_text = page.extract_text() or ""
        lines = [
            TextLine(page=page_index, block=1, line=index, text=clean_line(line))
            for index, line in enumerate(raw_text.splitlines(), start=1)
        ]
        pages.append(
            {
                "page": page_index,
                "lines": [asdict(line) for line in lines if line.text],
                "paragraphs": paragraphize_lines([line for line in lines if line.text]),
            }
        )
    return pages, len(reader.pages), "pypdf"


def extract_pages(pdf_path: Path, engine: str) -> tuple[list[dict[str, Any]], int, str]:
    if engine in {"auto", "pymupdf"}:
        try:
            return extract_with_pymupdf(pdf_path)
        except ModuleNotFoundError:
            if engine == "pymupdf":
                raise
        except Exception:
            if engine == "pymupdf":
                raise
    return extract_with_pypdf(pdf_path)


def iter_paragraphs(pages: Iterable[dict[str, Any]]) -> Iterable[dict[str, Any]]:
    for page in pages:
        yield from page["paragraphs"]


def build_sentences(pages: list[dict[str, Any]]) -> list[Sentence]:
    sentences: list[Sentence] = []
    current_section: SectionKind = "title"
    current_heading = "Title / Front matter"
    counters: dict[int, int] = {}

    for paragraph in iter_paragraphs(pages):
        text = paragraph["text"]
        page = int(paragraph["page"])
        if paragraph.get("is_heading"):
            next_section = classify_heading(text, current_section)
            if next_section != "figures_tables":
                current_section = next_section
            current_heading = text
            continue
        if current_section == "title" and page > 1:
            current_section = "other"
            current_heading = "Main text"
        for sentence_text in split_sentences(text):
            counters[page] = counters.get(page, 0) + 1
            sentence_id = f"P{page:03d}.S{counters[page]:04d}"
            sentences.append(
                Sentence(
                    id=sentence_id,
                    page=page,
                    section=current_section,
                    heading=current_heading,
                    text=sentence_text,
                )
            )
    return sentences


def build_document(pdf_path: Path, engine: str) -> PdfTextDocument:
    pages, page_count, used_engine = extract_pages(pdf_path, engine)
    sentences = build_sentences(pages)
    section_counts: dict[str, int] = {}
    for sentence in sentences:
        section_counts[sentence.section] = section_counts.get(sentence.section, 0) + 1
    return PdfTextDocument(
        source_pdf=str(pdf_path),
        page_count=page_count,
        extraction_engine=used_engine,
        pages=pages,
        sentences=sentences,
        section_sentence_counts=section_counts,
    )


def render_text(document: PdfTextDocument) -> str:
    chunks: list[str] = []
    for page in document.pages:
        chunks.append(f"\n\n===== Page {page['page']} =====\n")
        chunks.extend(paragraph["text"] for paragraph in page["paragraphs"])
    return "\n\n".join(chunks).strip()


def render_sentences(document: PdfTextDocument) -> str:
    lines = [
        f"# Sentence inventory",
        f"- Source PDF: {document.source_pdf}",
        f"- Pages: {document.page_count}",
        f"- Extraction engine: {document.extraction_engine}",
        "",
    ]
    current_section = ""
    for sentence in document.sentences:
        if sentence.section != current_section:
            current_section = sentence.section
            lines.append(f"\n## {current_section}")
        lines.append(
            f"- `{sentence.id}` [p.{sentence.page}; {sentence.heading}] {sentence.text}"
        )
    return "\n".join(lines).strip()


def render_markdown(document: PdfTextDocument) -> str:
    lines = [
        "# PDF Text Extraction",
        "",
        f"- Source PDF: `{document.source_pdf}`",
        f"- Pages: {document.page_count}",
        f"- Extraction engine: {document.extraction_engine}",
        f"- Total sentences: {len(document.sentences)}",
        "- Section sentence counts: "
        + ", ".join(
            f"{section}={count}"
            for section, count in sorted(document.section_sentence_counts.items())
        ),
        "",
    ]
    lines.append(render_sentences(document))
    lines.append("\n# Page Text")
    lines.append(render_text(document))
    return "\n".join(lines).strip()


def write_output(content: str, output_path: Path | None) -> None:
    if output_path:
        output_path = output_path.expanduser().resolve()
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(content, encoding="utf-8")
    else:
        print(content)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Extract auditable text, sections, and sentence IDs from a PDF."
    )
    parser.add_argument("pdf", type=Path, help="Path to PDF file")
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help="Optional output file. Defaults to stdout.",
    )
    parser.add_argument(
        "--format",
        choices=("text", "sentences", "markdown", "json"),
        default="text",
        help="Output format. Use 'sentences' or 'json' for LLM coverage checks.",
    )
    parser.add_argument(
        "--engine",
        choices=("auto", "pymupdf", "pypdf"),
        default="auto",
        help="Extraction engine. auto prefers PyMuPDF layout extraction.",
    )
    args = parser.parse_args()

    pdf_path = args.pdf.expanduser().resolve()
    if not pdf_path.exists():
        raise SystemExit(f"PDF not found: {pdf_path}")
    if pdf_path.suffix.lower() != ".pdf":
        raise SystemExit(f"Not a PDF: {pdf_path}")

    try:
        document = build_document(pdf_path, args.engine)
    except ModuleNotFoundError as exc:
        raise SystemExit(
            "Missing dependency. Install with `python -m pip install -r requirements.txt`."
        ) from exc

    if args.format == "json":
        content = json.dumps(asdict(document), ensure_ascii=False, indent=2)
    elif args.format == "sentences":
        content = render_sentences(document)
    elif args.format == "markdown":
        content = render_markdown(document)
    else:
        content = render_text(document)

    write_output(content, args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
