#!/usr/bin/env bash
# Build the lecture notes.
#   ./build.sh pilot   regenerate main-pilot.tex (ch0 + concentration only), build it
#   ./build.sh main    build the full book (all includes)
# Always: write buildstamp.tex, wipe aux/toc/out, run pdflatex + per-chapter
# bibtex, then rerun pdflatex until the PDF is BYTE-STABLE. The extra pass is
# NOT optional: tufte's \titlecontents wraps every ToC entry in fullwidth =
# adjustwidth* (changepage), which resolves page parity from aux data written
# by the PREVIOUS run -- three runs after an aux wipe leave ToC entries
# shifted exactly one overhang (167.4pt) off the left paper edge.
set -euo pipefail
cd "$(dirname "$0")"

TARGET="${1:-pilot}"
case "$TARGET" in
  pilot)
    python3 - <<'EOF'
import re
src = open('main.tex').read()
out = re.sub(r'\\include\{chapters/(?!ch0|concentration-ineq)[^}]+\}\n?', '', src)
open('main-pilot.tex', 'w').write(out)
EOF
    JOB=main-pilot ;;
  main) JOB=main ;;
  *) echo "usage: $0 [pilot|main]" >&2; exit 2 ;;
esac

printf '%s\n' "\\newcommand{\\buildstamp}{$(date '+%Y-%m-%d %H:%M %Z')}" > buildstamp.tex

rm -f "$JOB".aux "$JOB".toc "$JOB".out "$JOB".bbl "$JOB".blg "$JOB".pdf
rm -f chapters/*.aux chapters/*.bbl chapters/*.blg
pdflatex -interaction=nonstopmode "$JOB.tex" > /dev/null 2>&1 || true
for a in chapters/*.aux; do bibtex "${a%.aux}" > /dev/null 2>&1 || true; done

pdfhash() { md5 -q "$1" 2>/dev/null || md5sum "$1" | cut -d' ' -f1; }
prev=""
for i in 1 2 3 4 5 6 7 8; do
  pdflatex -interaction=nonstopmode "$JOB.tex" > /dev/null 2>&1 || true
  cur=$(pdfhash "$JOB.pdf")
  if [ "$cur" = "$prev" ]; then echo "[$JOB] byte-stable after $i extra run(s)"; break; fi
  prev=$cur
done
[ "$cur" = "$prev" ] || { echo "[$JOB] WARNING: not byte-stable after 8 runs"; exit 1; }

if grep -q '^!' "$JOB.log"; then echo "[$JOB] LaTeX ERRORS:"; grep '^!' "$JOB.log" | head -5; exit 1; fi
echo "[$JOB] $(pdfinfo "$JOB.pdf" 2>/dev/null | awk '/^Pages:/{printf "%s pp", $2}') $(ls -l "$JOB.pdf" | awk '{print $5}') bytes, $(grep -c 'Overfull' "$JOB.log") overfulls"
