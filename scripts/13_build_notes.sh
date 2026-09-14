#!/bin/bash
# Build the lecture notes with per-chapter bibliographies (chapterbib).
# Usage: bash scripts/13_build_notes.sh   [from repo root or anywhere]
set -e
cd "$(dirname "$0")/../lecture-notes"
pdflatex -interaction=nonstopmode main.tex >/dev/null
for aux in chapters/*.aux; do
  if grep -q '\\bibdata' "$aux" 2>/dev/null; then
    bibtex "${aux%.aux}" 2>&1 | grep -i 'error\|warning--' || true
  fi
done
pdflatex -interaction=nonstopmode main.tex >/dev/null
pdflatex -interaction=nonstopmode main.tex >/dev/null
echo "errors: $(grep -c '^!' main.log || true)"
grep -m5 'LaTeX Warning.*undefined' main.log || true
grep 'Output written' main.log || echo "NO PDF PRODUCED"
