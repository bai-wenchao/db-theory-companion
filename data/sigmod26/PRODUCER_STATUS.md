# PRODUCER status — TeX-first ingest, 2026-09-13

- src_ok: 137 (all 138 s2-mapped arXiv e-prints fetched; stage A 9 + stage B 128)
- src_fail: 1 (sigmod26-281 / arXiv 2509.00480 — PDF-only submission, no TeX in e-print)
- tex_extracted: 137 (theory/<id>.{json,md} from="tex", overwriting pdf-derived versions)
- flagged_total: 98 (index rebuilt: 385 papers, 156 pdf_ok, with_any_theory=107)
- recovered_via_title: 0 (arXiv API export.arxiv.org still 429 at re-test — stage C skipped)
- Coverage: 156/385 papers have theory extractions (137 tex + 19 pdf-only legacy)
- Stage A validation: 6 fresh papers spot-checked (e.g. sigmod26-022) — statements/proofs/bound sentences readable
- 04t bug fixes: (1) detex leaked literal env names ("enumerate"/"itemize"/"restatable") -> now strips \begin{...}/\end{...}, \item -> "; "; (2) SyntaxWarning from module docstring -> raw string
- 02t_download_tex.py: no bugs encountered; zero 429s during e-print downloads (1.5s throttle sufficed)
