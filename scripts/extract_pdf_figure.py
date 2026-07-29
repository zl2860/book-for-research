#!/usr/bin/env python3
"""Render a cropped figure from a PDF page.

Coordinates use PDF point units with origin at the top-left in PyMuPDF's page
coordinate system. Page numbers are 1-based.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import fitz


def parse_clip(value: str) -> fitz.Rect:
    parts = [float(part.strip()) for part in value.split(",")]
    if len(parts) != 4:
        raise argparse.ArgumentTypeError("clip must be x0,y0,x1,y1")
    x0, y0, x1, y1 = parts
    if x1 <= x0 or y1 <= y0:
        raise argparse.ArgumentTypeError("clip must satisfy x1>x0 and y1>y0")
    return fitz.Rect(x0, y0, x1, y1)


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract a cropped PDF figure as PNG.")
    parser.add_argument("pdf", type=Path, help="Path to source PDF")
    parser.add_argument("--page", type=int, required=True, help="1-based page number")
    parser.add_argument("--clip", type=parse_clip, required=True, help="x0,y0,x1,y1")
    parser.add_argument("--output", type=Path, required=True, help="Output PNG path")
    parser.add_argument("--zoom", type=float, default=3.0, help="Render zoom factor")
    args = parser.parse_args()

    pdf_path = args.pdf.expanduser().resolve()
    output_path = args.output.expanduser().resolve()
    if not pdf_path.exists():
        raise SystemExit(f"PDF not found: {pdf_path}")
    if args.page < 1:
        raise SystemExit("--page must be >= 1")

    doc = fitz.open(pdf_path)
    if args.page > len(doc):
        raise SystemExit(f"PDF has only {len(doc)} pages")

    page = doc[args.page - 1]
    pixmap = page.get_pixmap(
        matrix=fitz.Matrix(args.zoom, args.zoom),
        clip=args.clip,
        alpha=False,
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    pixmap.save(output_path)
    print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
