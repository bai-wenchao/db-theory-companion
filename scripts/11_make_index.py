#!/usr/bin/env python3
"""Build lecture-notes/chapters/index.tex: domain index + named results.

Chapter-number-based (\\ref to existing labels), no makeindex, no \\index markup
in the chapters. Reads main.tex's \\include order, so it stays in sync with the
book's chapter sequence.

Named statements are attributed to the corpus paper cited nearest before them
WITHIN THE SAME \\section (chapter-intro cites never leak into the classical
ladders), and papers carry the domain tags assigned in notes/sigmod26/batch_*.md.
Rerunnable: output is regenerated wholesale.

Usage:  python3 scripts/11_make_index.py
"""
import re
import pathlib
import sys
from collections import defaultdict

ROOT = pathlib.Path(__file__).resolve().parent.parent
LN = ROOT / "lecture-notes"
NOTES = ROOT / "notes" / "sigmod26"

# A named statement counts as corpus-derived only if its bracket title points
# back at the source paper ("; Theorem 3.5 of the paper", "from the paper's
# analysis", an embedded \citep{sigmod26-...}) or if it sits under the book's
# exemplar-\paragraph{Guarantee.} convention. Classical ladder theorems that
# merely FOLLOW a passing corpus mention must stay unattributed.
PAPER_MARKER = re.compile(r"the papers?\b|\\cite[pt]?\s*\{?sigmod26", re.I)

KINDS = {"theorem": "Theorem", "lemma": "Lemma", "proposition": "Proposition",
         "corollary": "Corollary", "definition": "Definition"}
ABBR = {"theorem": "Thm.", "lemma": "Lem.", "proposition": "Prop.",
        "corollary": "Cor.", "definition": "Def."}
ENV = "|".join(KINDS)

DOMAIN_NAMES = {
    "graph-db": "Graph data and queries",
    "privacy-dp": "Differential privacy",
    "streaming": "Streaming algorithms",
    "sketching": "Sketching",
    "ann-vector-search": "Vector search and ANN indexes",
    "indexing": "Indexing",
    "query-optimization": "Query optimization",
    "cardinality-estimation": "Cardinality estimation",
    "join-algorithms": "Join algorithms",
    "aqp": "Approximate query processing",
    "sampling": "Sampling",
    "llm-db": "LLM-backed data systems",
    "data-cleaning": "Data cleaning and repair",
    "entity-resolution": "Entity resolution",
    "data-integration": "Data integration",
    "transactions": "Transactions",
    "consensus-replication": "Consensus and replication",
    "distributed-query": "Distributed query processing",
    "security": "Security",
    "fairness": "Fairness",
    "data-market": "Data markets",
    "spatial": "Spatial data",
    "time-series": "Time series",
    "storage-compression": "Storage and compression",
    "caching-scheduling": "Caching and scheduling",
    "provenance": "Provenance",
    "uncertain-data": "Uncertain data",
    "workload-tuning": "Workload tuning",
    "benchmark": "Benchmarks and evaluation",
}


def tex_sort_key(s: str) -> str:
    """Alphabetize on letters only: drop commands, braces, math, punctuation."""
    s = re.sub(r"\\[a-zA-Z]+", "", s)      # \emph, \'e, \pods ...
    s = re.sub(r"[{}$\\]", "", s)          # delimiters
    s = s.lower()
    m = re.search(r"[a-z]", s)
    if m and m.start() > 0:
        s = s[m.start():]                  # sort math-first names by first letter
    return re.sub(r"[^a-z0-9]", "", s) or "zzz"


def clean_name(name: str) -> str:
    # drop source attributions: '; Theorem of the paper, ...' and
    # ', Theorem~6.4 of the paper, ...' (kinds in both singular/plural)
    name = re.sub(r"\s*;[\s\S]*$", "", name)
    name = re.sub(r",\s*(?:Theorems?|Lemmas?|Propositions?|Corollaries?|"
                  r"Definitions?|Claims?|Facts?|Observations?)\b[\s\S]*$", "", name)
    if re.search(r"the\s+paper", name):  # one-off attribution phrasings
        name = re.sub(r",[^,]*the\s+paper[\s\S]*$", "", name)
    # bracket names span source lines: collapse to single spaces so emitted
    # .tex never gains a stray indent/break
    return re.sub(r"\s+", " ", name).strip()


def main() -> int:
    main_tex = (LN / "main.tex").read_text()
    order = [c for c in re.findall(r"\\include\{chapters/([a-z0-9-]+)\}", main_tex)
             if c != "index"]

    chapters = []  # (slug, title, ch-label) in book order
    for slug in order:
        text = (LN / f"chapters/{slug}.tex").read_text()
        mt = re.search(r"\\chapter\{([^}]*)\}", text)
        ml = re.search(r"\\label\{(ch:[^}]*)\}", text)
        if not mt or not ml:
            print(f"WARNING: {slug}: missing chapter title or ch: label", file=sys.stderr)
            continue
        chapters.append((slug, mt.group(1), ml.group(1)))

    # --- domain tags per paper, from the analysis notes (0 LLM tokens)
    paper_dom = {}
    for f in sorted(NOTES.glob("batch_*.md")):
        for m in re.finditer(r"### (sigmod26-\d+)[^\n]*\ndomain: ([^\n]+)", f.read_text()):
            tags = [t.strip() for t in m.group(2).split("|")
                    if t.strip() and not t.strip().startswith("+")]
            paper_dom.setdefault(m.group(1), set()).update(tags)

    # --- named results with per-statement paper attribution
    results = []  # {"name","kw","label","chlab","paper"} in book order
    pods = set()  # corpus ids flagged \pods anywhere
    unmatched = 0
    for slug, _, chlab in chapters:
        text = (LN / f"chapters/{slug}.tex").read_text()
        secs = [m.start() for m in re.finditer(r"\\section\*?\{", text)]
        paras = [m.start() for m in re.finditer(r"\\paragraph\{", text)]

        def sec_of(i, secs=secs):
            started = [p for p in secs if p <= i]
            return started[-1] if started else -1

        def in_guarantee(i, secs=secs, paras=paras, text=text):
            mysec = sec_of(i)
            started = [p for p in paras if sec_of(p) == mysec and p <= i]
            return bool(started) and \
                text[started[-1]:].startswith("\\paragraph{Guarantee")

        cites = [(m.start(), m.group(0)) for m in re.finditer(r"sigmod26-\d+", text)]
        for cm in re.finditer(r"sigmod26-\d+", text):
            if "\\pods" in text[cm.end():cm.end() + 15]:
                pods.add(cm.group(0))
        for m in re.finditer(r"\\begin\{(" + ENV + r")\}\[([^\]]*)\]", text):
            kind, name = m.group(1), m.group(2)
            lm = re.search(r"\\label\{((?:thm|lem|prop|cor|def):[^}]*)\}",
                           text[m.end():m.end() + 300])
            if not lm:
                unmatched += 1
                continue
            mysec = sec_of(m.start())
            prev = [pid for cpos, pid in cites
                    if cpos < m.start() and sec_of(cpos) == mysec]
            paper = prev[-1] if (prev and (PAPER_MARKER.search(name)
                                           or in_guarantee(m.start()))) else None
            results.append({"name": clean_name(name), "kw": KINDS[kind],
                            "abbr": ABBR[kind], "label": lm.group(1),
                            "chlab": chlab, "paper": paper})

    # --- group corpus-derived results by domain, then chapter (book order)
    dom_res = defaultdict(lambda: defaultdict(list))  # domain -> chlab -> [result]
    dom_pids = defaultdict(set)
    for r in results:
        if not r["paper"]:
            continue
        for d in paper_dom.get(r["paper"], ()):
            dom_res[d][r["chlab"]].append(r)
            dom_pids[d].add(r["paper"])

    def dom_key(d):
        n = sum(len(v) for v in dom_res[d].values())
        return (-n, DOMAIN_NAMES.get(d, d))

    # ---------------- emit ----------------
    out = []
    w = out.append
    w("% AUTO-GENERATED by scripts/11_make_index.py -- do not edit by hand.")
    w("% Regenerate with: python3 scripts/11_make_index.py")
    w("\\chapter*{Index}")
    w("\\addcontentsline{toc}{chapter}{Index}")
    w("\\markboth{Index}{Index}")
    w("")
    w("Every entry is a hyperlink to the statement's home chapter. \\emph{By paper")
    w("domain} indexes the book from the corpus side: named statements transcribed")
    w("from exemplar papers are grouped under the research area of the source paper,")
    w("one entry per line, so each area shows which tools (chapters) its papers")
    w("exercise and what they prove. Classical background statements carry no")
    w("corpus source and appear only in the alphabetical list below. Full")
    w("references appear in each chapter's bibliography.")
    w("")
    w("% Full-measure index lines WITHOUT fullwidth/adjustwidth*. adjustwidth*")
    w("% cannot judge an entry that lands at the top of a fresh page: the live")
    w("% \\c@page test still counts the PREVIOUS page (the round-8 ToC disease,")
    w("% see main.tex), and strict mode's aux probe precedes the list's")
    w("% breakable top glue, so it too ships with the previous page and")
    w("% converges stably WRONG (observed: one-line entries judged for the")
    w("% prior page and painted at x = 72-167.4 = -95pt, half off the paper).")
    w("% Instead each entry is ONE unbreakable paragraph (\\interlinepenalty")
    w("% 10000) at the full text+overhang measure, with \\leftskip chosen from")
    w("% the PREVIOUS run's aux: the \\protected@write probe sits INSIDE the")
    w("% entry's first line, so \\thepage expands at shipout to the page the")
    w("% line actually lands on. The written definition (\\gdef\\idxpg<roman>)")
    w("% uses kernel primitives only -- no @, so it survives the aux being")
    w("% re-tokenized at \\begin{document}. Pagination is parity-independent")
    w("% (same measure both parities), so build.sh's byte-stable loop")
    w("% converges it in 2-3 runs.  Spacing: \\parskip=0 so a domain header")
    w("% has NO breakable glue before its first entry; the breakable")
    w("% separator between entries is \\idxsep instead, and \\idxfirstline")
    w("% (no separator) follows headers and section heads.")
    w("\\setlength{\\parskip}{0pt}")
    w("\\makeatletter")
    w("\\newcounter{idxprobe}")
    w("\\newcommand*{\\idxentry}[1]{%")
    w("  \\par")
    w("  \\stepcounter{idxprobe}%")
    w("  \\begingroup")
    w("    \\interlinepenalty=10000 %")
    w("    \\hsize=\\dimexpr\\textwidth+\\@tufte@overhang\\relax")
    w("    \\leftskip=\\z@")
    w("    \\ifcsname idxpg\\romannumeral\\the\\c@idxprobe\\endcsname")
    w("      \\ifodd\\csname idxpg\\romannumeral\\the\\c@idxprobe\\endcsname\\relax\\else")
    w("        \\leftskip=-\\@tufte@overhang")
    w("      \\fi")
    w("    \\else")
    w("      \\leftskip=-\\@tufte@overhang")
    w("    \\fi")
    w("    \\noindent\\protected@write\\@auxout{}{%")
    w("      \\string\\gdef\\string\\idxpg\\romannumeral\\the\\c@idxprobe{\\thepage}}%")
    w("    #1\\par")
    w("  \\endgroup}")
    w("\\makeatother")
    w("\\newcommand*{\\idxsep}{\\vskip2.5pt plus1pt}")
    w("% domain header + its FIRST entry are ONE paragraph joined by \\\\*")
    w("% (parskip glue -- even 0pt -- is a legal page break, so separate")
    w("% paragraphs can orphan a header; a paragraph with interlinepenalty")
    w("% 10000 and a starred \\\\ cannot break at all)")
    w("\\newcommand*{\\idxdom}[3]{\\idxentry{\\hangindent=1.8em\\hangafter=2")
    w("  \\textbf{#1} (#2).\\\\* \\textbullet\\hspace{0.55em}#3}}")
    w("\\newcommand*{\\idxfirstline}[1]{\\idxentry{\\hangindent=1.8em\\hangafter=1")
    w("  \\textbullet\\hspace{0.55em}#1}}")
    w("\\newcommand*{\\idxline}[1]{\\idxsep\\idxfirstline{#1}}")
    w("")
    w("\\section*{By paper domain}")
    for i, d in enumerate(sorted(dom_res, key=dom_key)):
        if i:
            w("\\medskip")
        np = len(dom_pids[d])
        ex = f"{np} exemplar" + ("" if np == 1 else "s")
        bodies = [f"{r['name']} (Ch.~\\ref{{{c}}}, "
                  f"\\mbox{{{r['abbr']}~\\ref{{{r['label']}}}}})"
                  for _, _, c in chapters for r in dom_res[d].get(c, ())]
        w(f"\\idxdom{{{DOMAIN_NAMES.get(d, d)}}}{{{ex}}}{{{bodies[0]}}}")
        for b in bodies[1:]:
            w(f"\\idxline{{{b}}}")
    w("")
    w("\\clearpage")
    w("\\section*{Named theorems, lemmas, and definitions}")
    merged = defaultdict(list)
    for r in results:
        merged[r["name"]].append((r["kw"], r["label"]))
    for j, name in enumerate(sorted(merged, key=tex_sort_key)):
        refs_str = ", ".join(f"\\mbox{{{kw}~\\ref{{{lab}}}}}" for kw, lab in merged[name])
        cmd = "\\idxfirstline" if j == 0 else "\\idxline"
        w(f"{cmd}{{{name}, {refs_str}}}")
    w("")

    (LN / "chapters" / "index.tex").write_text("\n".join(out))
    n_assoc = sum(1 for r in results if r["paper"])
    print(f"chapters/index.tex: {len(chapters)} chapters, "
          f"{len(results)} named results ({unmatched} envs without label skipped; "
          f"{n_assoc} corpus-derived, {len(results) - n_assoc} classical), "
          f"{len(dom_res)} domains from "
          f"{len(set().union(*dom_pids.values()))} exemplar papers "
          f"({len(pods)} PODS-flagged).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
