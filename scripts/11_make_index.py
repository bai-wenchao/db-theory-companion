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
    w("so each entry shows which tools (chapters) that area's papers exercise and")
    w("what they prove; PODS'26 exemplars are flagged in the header. Classical")
    w("background statements carry no corpus source and appear only in the")
    w("alphabetical list below. Full references appear in each chapter's")
    w("bibliography.")
    w("")
    w("\\section*{By paper domain}")
    w("% columns start on a fresh page: keeps the section heading with its list")
    w("\\begin{multicols}{2}")
    w("\\RaggedRight")   # narrow columns: no justification squeeze
    w("\\begin{itemize}")
    for d in sorted(dom_res, key=dom_key):
        np, npods = len(dom_pids[d]), len(dom_pids[d] & pods)
        ex = f"{np} exemplar" + ("" if np == 1 else "s")
        if npods:
            ex += f", {npods} of them PODS'26"
        w(f"  \\item \\textbf{{{DOMAIN_NAMES.get(d, d)}}} ({ex}).")
        ch_order = [c for _, _, c in chapters if c in dom_res[d]]
        for i, c in enumerate(ch_order):
            refs = ", ".join(
                "%s (\\mbox{%s~\\ref{%s}})" % (r["name"], r["abbr"], r["label"])
                for r in dom_res[d][c])
            lead = "Ch.~\\ref{%s}: " % c if i == 0 else "; Ch.~\\ref{%s}: " % c
            w(f"    {lead}{refs}%")  # % kills the newline space before "; Ch."
        w("")
    w("\\end{itemize}")
    w("\\end{multicols}")
    w("")
    w("% columns start on a fresh page: keeps the section heading with its list")
    w("\\clearpage")
    w("\\section*{Named theorems, lemmas, and definitions}")
    w("\\begin{multicols}{2}")
    w("\\RaggedRight")
    w("\\begin{itemize}")
    merged = defaultdict(list)
    for r in results:
        merged[r["name"]].append((r["kw"], r["label"]))
    for name in sorted(merged, key=tex_sort_key):
        refs_str = ", ".join(f"\\mbox{{{kw}~\\ref{{{lab}}}}}" for kw, lab in merged[name])
        w(f"  \\item {name}, {refs_str}")
    w("\\end{itemize}")
    w("\\end{multicols}")
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
