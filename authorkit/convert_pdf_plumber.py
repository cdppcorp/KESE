#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""PDF to Markdown converter using pdfplumber (handles CID Korean fonts)"""

import fitz  # pymupdf - for image extraction
import pdfplumber
import os
import sys
import re
from datetime import datetime
from pathlib import Path


def extract_pdf_to_markdown(pdf_path, output_dir, ref_id):
    """Convert PDF to markdown using pdfplumber for text + pymupdf for images"""

    os.makedirs(output_dir, exist_ok=True)
    images_dir = os.path.join(output_dir, "images")
    os.makedirs(images_dir, exist_ok=True)

    # Open with both libraries
    plumber = pdfplumber.open(pdf_path)
    fitz_doc = fitz.open(pdf_path)
    total_pages = len(plumber.pages)

    all_text = []
    image_count = 0
    headings_detected = 0
    total_chars = 0

    print(f"Processing: {os.path.basename(pdf_path)}")
    print(f"Total pages: {total_pages}")
    print(f"Engine: pdfplumber (text) + pymupdf (images)")

    for page_num in range(total_pages):
        page = plumber.pages[page_num]
        fitz_page = fitz_doc[page_num]

        # Extract text with pdfplumber
        text = page.extract_text() or ""

        # Extract tables if any
        tables = page.extract_tables()
        table_md = ""
        if tables:
            for table in tables:
                if table and len(table) > 0:
                    # Convert table to markdown
                    rows = []
                    for row in table:
                        cells = [str(c).replace("\n", " ").strip() if c else "" for c in row]
                        rows.append("| " + " | ".join(cells) + " |")
                    if len(rows) > 1:
                        # Add header separator
                        header_sep = "| " + " | ".join(["---"] * len(table[0])) + " |"
                        rows.insert(1, header_sep)
                    table_md += "\n" + "\n".join(rows) + "\n"

        # Extract images using pymupdf
        page_images = fitz_page.get_images()
        img_refs = []
        for img_idx, img in enumerate(page_images):
            try:
                xref = img[0]
                pix = fitz.Pixmap(fitz_doc, xref)
                if pix.colorspace and pix.colorspace.n >= 4:
                    pix = fitz.Pixmap(fitz.csRGB, pix)
                elif pix.n - pix.alpha > 3:
                    pix = fitz.Pixmap(fitz.csRGB, pix)
                if pix.alpha:
                    pix = fitz.Pixmap(pix, 0)

                # Skip tiny images (decorative)
                if pix.width < 50 or pix.height < 50:
                    continue

                img_filename = f"p{page_num+1:04d}_img{img_idx}.png"
                img_path = os.path.join(images_dir, img_filename)
                pix.save(img_path)
                image_count += 1
                img_refs.append(f"\n![이미지 {page_num+1}-{img_idx}](images/{img_filename})")
            except Exception as e:
                pass  # Skip problematic images

        # Process headings
        lines = text.split('\n')
        processed_lines = []
        for line in lines:
            line = line.strip()
            if not line:
                processed_lines.append("")
                continue

            # Skip page headers/footers
            if re.match(r'^\d+\s*\|\s*디지털헬스케어', line):
                continue
            if re.match(r'^디지털헬스케어\s*보안모델\s*$', line):
                continue

            # Korean chapter patterns
            if re.match(r'^제\s*\d+장\s', line):
                processed_lines.append(f"\n## {line}\n")
                headings_detected += 1
            elif re.match(r'^\d+\.\s+[가-힣A-Z]', line) and len(line) < 80:
                processed_lines.append(f"\n### {line}\n")
                headings_detected += 1
            elif re.match(r'^\d+\.\d+\.?\s+[가-힣A-Z]', line) and len(line) < 80:
                processed_lines.append(f"\n#### {line}\n")
                headings_detected += 1
            elif re.match(r'^[가-힣]+\)\s', line) or re.match(r'^[①②③④⑤⑥⑦⑧⑨⑩]', line):
                processed_lines.append(f"- {line}")
            else:
                processed_lines.append(line)

        page_text = '\n'.join(processed_lines)

        # Add table markdown
        if table_md:
            page_text += "\n" + table_md

        # Add image references
        for ref in img_refs:
            page_text += ref

        total_chars += len(page_text)
        all_text.append(f"\n---\n<!-- Page {page_num+1} -->\n{page_text}")

        if (page_num + 1) % 20 == 0:
            print(f"  Processed {page_num + 1}/{total_pages} pages...")

    plumber.close()
    fitz_doc.close()

    # Write full markdown
    full_md = '\n'.join(all_text)
    full_md_path = os.path.join(output_dir, "full.md")
    with open(full_md_path, 'w', encoding='utf-8') as f:
        f.write(f"# {os.path.basename(pdf_path).replace('.pdf', '')}\n\n")
        f.write(f"> Converted: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
        f.write(f"> Engine: pdfplumber + pymupdf\n")
        f.write(f"> Ref ID: {ref_id}\n\n")
        f.write(full_md)

    # Write conversion log
    log_path = os.path.join(output_dir, "conversion-log.md")
    with open(log_path, 'w', encoding='utf-8') as f:
        f.write(f"# Conversion Log\n\n")
        f.write(f"- **Source**: {os.path.basename(pdf_path)}\n")
        f.write(f"- **Ref ID**: {ref_id}\n")
        f.write(f"- **Pages**: {total_pages}\n")
        f.write(f"- **Converted**: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
        f.write(f"- **Engine**: pdfplumber (text) + pymupdf (images)\n")
        f.write(f"- **Text characters**: {total_chars:,}\n")
        f.write(f"- **Images extracted**: {image_count}\n")
        f.write(f"- **Headings detected**: {headings_detected}\n")

    print(f"\nConversion complete!")
    print(f"  Text: {total_chars:,} characters")
    print(f"  Images: {image_count}")
    print(f"  Headings: {headings_detected}")
    print(f"  Output: {full_md_path}")

    return {
        'pages': total_pages,
        'characters': total_chars,
        'images': image_count,
        'headings': headings_detected
    }


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python convert_pdf_plumber.py <pdf_path> <output_dir> <ref_id>")
        sys.exit(1)

    pdf_path = sys.argv[1]
    output_dir = sys.argv[2]
    ref_id = sys.argv[3]
    extract_pdf_to_markdown(pdf_path, output_dir, ref_id)
