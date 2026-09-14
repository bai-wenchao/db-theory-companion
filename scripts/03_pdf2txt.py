#!/usr/bin/env python3
"""Convert pdfs to text with pdftotext (fallback: pypdf).

Usage: python3 03_pdf2txt.py <pdf_dir> <txt_dir>
"""
import glob, os, shutil, subprocess, sys

pdf_dir, txt_dir = sys.argv[1], sys.argv[2]
os.makedirs(txt_dir, exist_ok=True)
HAS_PDFTOTEXT = shutil.which("pdftotext") is not None


def via_pypdf(pdf, txt):
    from pypdf import PdfReader
    r = PdfReader(pdf)
    with open(txt, "w") as f:
        for pg in r.pages:
            f.write((pg.extract_text() or "") + "\n")


ok = bad = skip = 0
for pdf in sorted(glob.glob(os.path.join(pdf_dir, "*.pdf"))):
    base = os.path.splitext(os.path.basename(pdf))[0]
    txt = os.path.join(txt_dir, base + ".txt")
    if os.path.exists(txt) and os.path.getsize(txt) > 500:
        skip += 1
        continue
    try:
        if HAS_PDFTOTEXT:
            subprocess.run(["pdftotext", "-q", pdf, txt], check=True, timeout=180)
        else:
            via_pypdf(pdf, txt)
        if os.path.exists(txt) and os.path.getsize(txt) > 500:
            ok += 1
        else:
            bad += 1
    except Exception as e:
        print("ERR", base, type(e).__name__, file=sys.stderr)
        bad += 1
print(f"converted={ok} skipped={skip} failed={bad} engine={'pdftotext' if HAS_PDFTOTEXT else 'pypdf'}")
