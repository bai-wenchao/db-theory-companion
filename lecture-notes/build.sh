#!/usr/bin/env bash
# Build the book ("A Theoretical Companion to Database Research").
#   ./build.sh main                build the full book (all includes)  [default];
#                                  also refreshes the distributable copy
#                                  A-Theoretical-Companion-to-Database-Research.pdf
#   ./build.sh chapter <name>      build main-<name>.tex = chapters/<name>.tex ONLY
#                                  (no cover/license/ToC/ch0; book numbering kept)
#   ./build.sh clean               remove aux-generated files (aux/bbl/toc/log/... and the
#                                  generated main-* subset sources) — every .pdf is KEPT
# Build targets always: write buildstamp.tex, wipe aux/toc/out, run pdflatex + per-chapter
# bibtex, then rerun pdflatex until the PDF is BYTE-STABLE. The extra pass is
# NOT optional: tufte's \titlecontents wraps every ToC entry in fullwidth =
# adjustwidth* (changepage), which resolves page parity from aux data written
# by the PREVIOUS run -- three runs after an aux wipe leave ToC entries
# shifted exactly one overhang (167.4pt) off the left paper edge.
set -euo pipefail
cd "$(dirname "$0")"

# LaTeX byproducts a build can leave behind, for every job (never .pdf).
AUX_EXT="aux toc out bbl blg log fls fdb_latexmk lof lot synctex.gz"

# gen_subset <job> <chapter>: write <job>.tex = main.tex with ONLY
# chapters/<chapter>.tex kept -- the front matter (\maketitle, the verso
# license page, \tableofcontents) and every other \include are stripped.
# The chapter KEEPS its full-book numbering (Theorem 2.3 here = Theorem 2.3
# in main.pdf): the target's position in main.tex's include order IS its
# book chapter number (ch0 = 0, counter starts at -1), so the
# \setcounter{chapter}{-1} that precedes ch0 is rewritten to <position-1>.
gen_subset() {
  local job="$1" name="$2"
  python3 - "$job" "$name" <<'EOF'
import re, sys
job, name = sys.argv[1], sys.argv[2]
src = open('main.tex').read()
includes = re.findall(r'\\include\{chapters/([^}]+)\}', src)
if name not in includes:
    sys.exit('chapter not \\include-d in main.tex: ' + name)
num = includes.index(name)
pat = re.compile(r'\\maketitle.*?\\setcounter\{chapter\}\{-1\}\n', re.S)
if not pat.search(src):
    sys.exit('front-matter anchor (\\maketitle .. \\setcounter{chapter}{-1}) not found in main.tex')
out = pat.sub(lambda m: '\\setcounter{chapter}{%d}\n' % (num - 1), src, count=1)
out = re.sub(r'\\include\{chapters/(?!' + re.escape(name) + r'\})[^}]+\}\n?', '', out)
open(job + '.tex', 'w').write(out)
EOF
}

TARGET="${1:-main}"
case "$TARGET" in
  main) JOB=main ;;
  chapter)
    NAME="${2:-}"
    if [ -z "$NAME" ]; then
      echo "usage: $0 chapter <name>   (e.g. $0 chapter reduction)" >&2; exit 2
    fi
    case "$NAME" in
      *[!a-z0-9-]*) echo "chapter: bad name '$NAME' (expected [a-z0-9-]+)" >&2; exit 2 ;;
    esac
    if [ ! -f "chapters/$NAME.tex" ]; then
      echo "chapter: no chapters/$NAME.tex; available:" >&2
      ls chapters/*.tex | sed -e 's|chapters/||; s|\.tex$||' | grep -vx index | sed 's/^/  /' >&2
      exit 2
    fi
    grep -Fq "\\include{chapters/$NAME}" main.tex || {
      echo "chapter: '$NAME' is not \\include'd in main.tex" >&2; exit 2; }
    gen_subset "main-$NAME" "$NAME"
    JOB="main-$NAME" ;;
  clean)
    rm -f buildstamp.tex
    for ext in $AUX_EXT; do rm -f main."$ext" main-*."$ext"; done
    rm -f main-*.tex            # generated subset sources (main-<name>.tex)
    rm -f chapters/*.aux chapters/*.bbl chapters/*.blg
    echo "[clean] aux artifacts removed; PDFs kept:"
    ls -1 *.pdf 2>/dev/null | sed 's/^/  /' || echo "  (none)"
    exit 0 ;;
  *)
    echo "usage: $0 [main|chapter <name>|clean]" >&2; exit 2 ;;
esac

# License badge: pdflatex cannot read SVG -- convert the tracked cc-by.svg
# to cc-by.pdf (VECTOR, not raster) when missing or stale; main.tex includes
# it extensionless (\includegraphics prefers .pdf). cc-by.pdf is gitignored
# like the other generated assets.
if [ ! "cc-by.pdf" -nt "cc-by.svg" ]; then
  if command -v rsvg-convert >/dev/null 2>&1; then
    rsvg-convert -f pdf -o cc-by.pdf cc-by.svg
  elif command -v inkscape >/dev/null 2>&1; then
    inkscape cc-by.svg --export-type=pdf --export-filename=cc-by.pdf
  elif [ ! -f cc-by.pdf ]; then
    echo "cc-by.pdf missing and no SVG converter found (install librsvg's rsvg-convert or Inkscape)" >&2
    exit 2
  fi
fi

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

if LC_ALL=C grep -q '^!' "$JOB.log"; then echo "[$JOB] LaTeX ERRORS:"; LC_ALL=C grep '^!' "$JOB.log" | head -5; exit 1; fi
echo "[$JOB] $(pdfinfo "$JOB.pdf" 2>/dev/null | awk '/^Pages:/{printf "%s pp", $2}') $(ls -l "$JOB.pdf" | awk '{print $5}') bytes, $(LC_ALL=C grep -c 'Overfull' "$JOB.log" || true) overfulls"

# Distributable copy under the book's title (full builds only, never subsets).
if [ "$TARGET" = main ]; then
  cp -f main.pdf "A-Theoretical-Companion-to-Database-Research.pdf"
  echo "[main] distributable copy: A-Theoretical-Companion-to-Database-Research.pdf"
fi
