# db-theory-companion

**How do database researchers actually use theory?** This repository answers that
question for the full SIGMOD 2026 research corpus, and distills the answer into a
book: **_A Theoretical Companion to Database Research_** — 273 pages, 13 technique
chapters, each grounded in theorems actually proved by SIGMOD papers.

The survey covers all 385 research articles of SIGMOD'26 (PACMMOD Vol 4, rounds
3–4, plus Vol 3 issues 4–6, rounds 1–2). Every paper's formal content is extracted
by script (statements, proofs, bound sentences, complexity signals), tagged by
LLM analysis against a controlled taxonomy (properties proved, tools used, domain,
role of theory in the paper), and the resulting cross-tabs drive the book: which
techniques earn their own chapter, and which corpus papers serve as exemplars.

The full methodology, environment notes, and run protocol live in
[CLAUDE.md](CLAUDE.md); the book's design rules in
[lecture-notes/CHAPTER-RULES.md](lecture-notes/CHAPTER-RULES.md).

## The book

`lecture-notes/` builds a Tufte-style book (ch0 + 13 tool chapters + script-built
index back matter) in which each chapter teaches one theoretical tool through
3–6 deduplicated exemplar theorems from the corpus. Exemplars drawn from the
PODS'26 issue of PACMMOD (29 articles share the corpus's DOI range) are flagged
so cross-venue claims stay honest.

| # | Chapter | The tool |
|---|---------|----------|
| 0 | ch0 | Scope, corpus statistics, how to read the book |
| 1 | reduction | From NP-hardness to conditional lower bounds |
| 2 | concentration-ineq | Chernoff/Bernstein tail bounds and friends |
| 3 | induction | Inductive invariants and correctness proofs |
| 4 | estimation-theory | Unbiasedness, variance, MSE |
| 5 | adversarial-construction | Worst-case inputs and lower-bound gadgets |
| 6 | dp-composition | Differential-privacy composition and post-processing |
| 7 | exchange-greedy | Exchange arguments and greedy correctness |
| 8 | spectral-matrix | Matrix concentration and spectral methods |
| 9 | amortized-potential | Potential functions and amortized bounds |
| 10 | coresets-rnla | Coresets and randomized numerical linear algebra |
| 11 | information-theory | Entropy, Fano, information-theoretic lower bounds |
| 12 | communication-complexity | Set disjointness and streaming lower bounds |
| 13 | online-decisions | Competitive analysis, regret, ski rental |

## Repository layout

Tracked (hand-written sources):

```
scripts/          01–13: corpus → tags → book pipeline (Python + bash, no LLM)
lecture-notes/    main.tex, chapters/*.tex (book text), tufte class files, build.sh
CLAUDE.md         methodology, taxonomy definitions, pipeline runbook
```

Generated locally, not redistributed (see `.gitignore` for the full regeneration
chain): `data/` (paper lists, downloaded PDFs/TeX, theory extractions — the
corpus itself is under the publishers' copyright), `index/` (scores and tag
cross-tabs), `notes/` (per-paper LLM analyses), `report/` (the prose survey), and
the script-built book assets (`figures/`, `chapters/index.tex`,
`chapters/*-all.bib`, `refs.bib`/`all.bib`).

## Pipeline

Two stages, both driven from the repo root:

```bash
# Stage A — corpus → tagged notes (network: OpenAlex, arXiv, Semantic Scholar)
python3 scripts/01_fetch_paper_list.py 4 data/sigmod26/papers.jsonl sigmod26
python3 scripts/02t_download_tex.py  data/sigmod26/papers.jsonl \
       data/sigmod26/s2_arxiv_map.json data/sigmod26/src       # arXiv TeX (preferred)
python3 scripts/02_download_pdfs.py ...                        # PDF fallback
python3 scripts/04t_extract_theory_tex.py ...                  # statements/proofs/signals
python3 scripts/05_build_index.py data/sigmod26 index/sigmod26_index
# per-paper tagging: LLM subagents write notes/sigmod26/batch_*.md
# per the protocol + taxonomy in CLAUDE.md, then:
python3 scripts/06_tag_stats.py notes/sigmod26 index/sigmod26_tags.md

# Stage B — tags → book (local; figures/bibs/index are script-built, 0 LLM)
python3 scripts/08_make_figures.py index/sigmod26_tags.md lecture-notes/figures
python3 scripts/11_make_index.py          # back-matter index from main.tex + notes
python3 scripts/12_chapter_bibs.py        # per-chapter cited-subset bibliographies
cd lecture-notes && ./build.sh main
```

ACM-only papers are fetched through a CDP-driven Chrome instance
(`scripts/02c_fetch_acm_cdp.py`); see CLAUDE.md's environment notes.

## Building the book

Requirements: a full-ish TeX Live (pdflatex with pgfplots, tcolorbox, chapterbib,
caption, microtype, newunicodechar), Python 3 with matplotlib for the figures,
`rsvg-convert` (librsvg) or Inkscape for the license badge (`build.sh` converts
the tracked `cc-by.svg` to vector `cc-by.pdf`), and poppler's `pdfinfo`
(optional — used only to print the page count).

```bash
cd lecture-notes
./build.sh main               # full book (default) → main.pdf
./build.sh chapter reduction  # main-reduction.pdf = ONLY chapter 1 (no cover/license/ToC/ch0)
./build.sh clean              # remove aux artifacts (aux/bbl/toc/log/... + generated
                              # main-* subset sources) — every .pdf is kept
```

Every build wipes aux, runs per-chapter bibtex, and reruns pdflatex until the
PDF is **byte-stable** (the Tufte ToC resolves page parity from the previous
run's aux, so a fixed pass count is not enough). The canonical page count always
comes from `./build.sh main`, never a bare pdflatex run. A full build also
refreshes a distributable copy under the book's title,
`A-Theoretical-Companion-to-Database-Research.pdf` (the file attached to
[releases](https://github.com/bai-wenchao/db-theory-companion/releases)).

Note for fresh clones: `figures/`, `chapters/index.tex`, and `chapters/*-all.bib`
are generated by Stage B scripts from the survey corpus and are not tracked, so
run Stage B (or drop in your own equivalents) before `./build.sh main`.

## License

- **Code** (`scripts/`, `build.sh`, tooling): [MIT License](LICENSE).
- **Book and survey-writing content** (`lecture-notes/` prose: `main.tex`,
  `chapters/*.tex`, and the survey documentation): [CC BY 4.0](LICENSE-CC-BY-4.0).
- Bundled Tufte-LaTeX class files (`tufte-book.cls`, `tufte-common.def`,
  `tufte.bst`, `xifthen.sty`) are redistributed under their own licenses — see
  [lecture-notes/THIRD-PARTY-NOTICES.md](lecture-notes/THIRD-PARTY-NOTICES.md).

## Citation

```bibtex
@book{bai2026companion,
  title  = {A Theoretical Companion to Database Research},
  author = {Bai, Wenchao and GLM5.3},
  note   = {Lecture notes distilled from a full-corpus survey of SIGMOD 2026},
  year   = {2026},
  url    = {https://github.com/bai-wenchao/db-theory-companion}
}
```
