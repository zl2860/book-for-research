#!/usr/bin/env python3
"""Build a source-complete LLM reading pack from a PDF.

The pack is designed for long scientific papers where Methods and Results must
be translated and interpreted at sentence-level coverage, not summarized from a
few salient excerpts.
"""

from __future__ import annotations

import argparse
from dataclasses import asdict
from pathlib import Path
from textwrap import dedent

from extract_pdf_text import PdfTextDocument, Sentence, build_document


FOCUS_SECTIONS = {"results", "methods"}


def chunk_sentences(
    sentences: list[Sentence], target_chars: int, focus_target_chars: int
) -> list[list[Sentence]]:
    chunks: list[list[Sentence]] = []
    current: list[Sentence] = []
    current_chars = 0
    current_section = sentences[0].section if sentences else "other"

    def flush() -> None:
        nonlocal current, current_chars
        if current:
            chunks.append(current)
        current = []
        current_chars = 0

    for sentence in sentences:
        limit = focus_target_chars if sentence.section in FOCUS_SECTIONS else target_chars
        section_changed = current and sentence.section != current_section
        over_limit = current and current_chars + len(sentence.text) > limit
        if section_changed or over_limit:
            flush()
        current_section = sentence.section
        current.append(sentence)
        current_chars += len(sentence.text) + 1
    flush()
    return chunks


def sentence_range(chunk: list[Sentence]) -> str:
    return f"{chunk[0].id}..{chunk[-1].id}"


def render_contract(document: PdfTextDocument) -> str:
    results_count = document.section_sentence_counts.get("results", 0)
    methods_count = document.section_sentence_counts.get("methods", 0)
    return dedent(
        f"""
        # LLM Reading Contract

        You must treat the extracted PDF text as the source of truth. Do not rely
        on the abstract alone, prior knowledge, or guesses about the paper.

        Mandatory coverage:

        1. Process every sentence ID in this pack at least once.
        2. For `results` and `methods`, produce sentence-by-sentence bilingual
           handling: original sentence ID, faithful Chinese translation, and one
           concise interpretation of what the sentence contributes.
        3. For figures, tables, statistics, cohorts, thresholds, software,
           parameters, and validation steps, retain the source sentence IDs.
        4. Do not collapse multiple Results or Methods sentences into one
           unsupported paragraph unless all source sentence IDs are listed.
        5. If extraction noise is suspected, mark it as `EXTRACTION_CHECK`
           instead of silently repairing it.
        6. Before finalizing a note, output a coverage audit with:
           total sentence IDs covered, uncovered IDs, Results coverage, Methods
           coverage, and any low-confidence extraction spans.

        Minimum expected source coverage from this PDF:

        - Pages: {document.page_count}
        - Total extracted sentences: {len(document.sentences)}
        - Results sentences: {results_count}
        - Methods sentences: {methods_count}

        Required final note sections:

        - Basic metadata and PDF parsing quality.
        - Main figures and tables with source-linked interpretation.
        - Biological story and research question.
        - Study design and data structure.
        - Results, in original Results order, with sentence IDs.
        - Independent methodology explanation, with sentence IDs.
        - Statistical methods, with inputs, null/estimand, outputs, limitations.
        - Evidence strength, limitations, dangerous assumptions.
        - Coverage audit.
        """
    ).strip()


def render_chunk(index: int, total: int, chunk: list[Sentence]) -> str:
    section = chunk[0].section
    focus = "YES" if section in FOCUS_SECTIONS else "NO"
    lines = [
        f"## Chunk {index:03d}/{total:03d}",
        "",
        f"- Sentence range: `{sentence_range(chunk)}`",
        f"- Section: `{section}`",
        f"- Methods/Results sentence-level translation required: {focus}",
        "",
        "| Sentence ID | Page | Heading | Source sentence |",
        "|---|---:|---|---|",
    ]
    for sentence in chunk:
        source = sentence.text.replace("|", "\\|")
        heading = sentence.heading.replace("|", "\\|")
        lines.append(f"| `{sentence.id}` | {sentence.page} | {heading} | {source} |")
    return "\n".join(lines)


def render_pack(
    document: PdfTextDocument, target_chars: int, focus_target_chars: int
) -> str:
    chunks = chunk_sentences(document.sentences, target_chars, focus_target_chars)
    lines = [
        render_contract(document),
        "",
        "# Extraction Manifest",
        "",
        f"- Source PDF: `{document.source_pdf}`",
        f"- Extraction engine: `{document.extraction_engine}`",
        f"- Pages: {document.page_count}",
        f"- Total sentences: {len(document.sentences)}",
        "- Section sentence counts: "
        + ", ".join(
            f"{section}={count}"
            for section, count in sorted(document.section_sentence_counts.items())
        ),
        f"- Chunks: {len(chunks)}",
        "",
        "| Chunk | Section | Sentence range | Count | Methods/Results focus |",
        "|---:|---|---|---:|---|",
    ]
    for index, chunk in enumerate(chunks, start=1):
        section = chunk[0].section
        focus = "yes" if section in FOCUS_SECTIONS else "no"
        lines.append(
            f"| {index} | `{section}` | `{sentence_range(chunk)}` | {len(chunk)} | {focus} |"
        )
    lines.extend(["", "# Source Chunks", ""])
    for index, chunk in enumerate(chunks, start=1):
        lines.append(render_chunk(index, len(chunks), chunk))
        lines.append("")
    return "\n".join(lines).strip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Build an auditable LLM PDF pack.")
    parser.add_argument("pdf", type=Path, help="Path to source PDF")
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help="Output markdown file. Defaults to stdout.",
    )
    parser.add_argument(
        "--engine",
        choices=("auto", "pymupdf", "pypdf"),
        default="auto",
        help="Extraction engine passed through to extract_pdf_text.py.",
    )
    parser.add_argument(
        "--target-chars",
        type=int,
        default=12000,
        help="Target chunk size for non-focus sections.",
    )
    parser.add_argument(
        "--focus-target-chars",
        type=int,
        default=6500,
        help="Smaller target chunk size for Methods and Results.",
    )
    parser.add_argument(
        "--json-manifest",
        type=Path,
        help="Optional JSON extraction manifest for automated coverage checks.",
    )
    args = parser.parse_args()

    pdf_path = args.pdf.expanduser().resolve()
    if not pdf_path.exists():
        raise SystemExit(f"PDF not found: {pdf_path}")
    if pdf_path.suffix.lower() != ".pdf":
        raise SystemExit(f"Not a PDF: {pdf_path}")

    document = build_document(pdf_path, args.engine)
    pack = render_pack(document, args.target_chars, args.focus_target_chars)

    if args.output:
        output_path = args.output.expanduser().resolve()
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(pack, encoding="utf-8")
    else:
        print(pack)

    if args.json_manifest:
        import json

        manifest_path = args.json_manifest.expanduser().resolve()
        manifest_path.parent.mkdir(parents=True, exist_ok=True)
        manifest_path.write_text(
            json.dumps(asdict(document), ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
