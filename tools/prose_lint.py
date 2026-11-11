#!/usr/bin/env python3
"""Flag AI-isms in prose: the sentence habits that make machine-written fiction tiring to read.

Usage:
    python3 tools/prose_lint.py FILE [FILE ...]          # report per file
    python3 tools/prose_lint.py --summary FILE [...]    # rates only, no line hits
    python3 tools/prose_lint.py --only and-chain FILE   # one rule

The rules and the reasons behind them are in docs/writing/natural-prose.md.
A hit is a prompt to look, not a verdict. Rates matter more than single hits:
one "the way a dog stirs" is a simile; nine in a chapter is a tic.
"""
import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

# Whole-text rates (per 1,000 words of narration). Stories 02 and 03, whose prose
# reads naturally, run 4-5 ", and" per 1k; Story 01's first draft ran 15.
DASH_LIMIT = 8
# ", and" that opens a new clause with its own subject (", and he...", ", and the man...").
# Serial-comma lists ("climbed back, and dropped again") are not counted.
CLAUSE_AND = re.compile(r",\s+and\s+(?:then\s+)?(?:he|she|they|it|I|we|you|his|her|their|its|the|a|an|this|that|there|nobody|everyone|[A-Z][a-z]+)\b")
COMMA_AND_LIMIT = 4

# ---------------------------------------------------------------- text prep

def load_prose(path):
    """Return [(line_no, paragraph_text)] for prose paragraphs, skipping headings,
    front matter, HTML, horizontal rules and tables."""
    lines = Path(path).read_text(encoding="utf-8").splitlines()
    out, in_front = [], False
    for i, line in enumerate(lines, 1):
        s = line.strip()
        if i == 1 and s == "---":
            in_front = True
            continue
        if in_front:
            if s == "---":
                in_front = False
            continue
        if not s or s.startswith(("#", "<", ">", "|", "---", "***", "```", "- ", "* ", "1. ", "2. ", "3. ", "4. ", "5. ", "6. ", "7. ")):
            continue
        out.append((i, s))
    return out


SENT_SPLIT = re.compile(r'(?<=[.!?])["”’*]?\s+(?=["“‘*]?[A-Z])')


def sentences(para):
    return [s for s in SENT_SPLIT.split(para) if s.strip()]


def narration(sent):
    """Strip quoted dialogue so rules about narration don't fire on speech."""
    return re.sub(r'"[^"]*"|“[^”]*”', ' ', sent)


def words(text):
    return re.findall(r"[A-Za-z']+", text)

# ---------------------------------------------------------------- rules
# Each rule: (id, description, function(sentence, narration) -> bool | str)
# Limit = acceptable hits per 1,000 words before the rule counts as a tic.

PRONOUN_OR_NAME = r"(?:he|she|they|it|we|I|you|[A-Z][a-z]+)"

RULES = []


def rule(rid, limit, desc):
    def deco(fn):
        RULES.append((rid, limit, desc, fn))
        return fn
    return deco


@rule("and-chain", 1.0, "sentence strings three or more clauses together with 'and'")
def _and_chain(s, n):
    # Count 'and' that join clauses or long phrases: ', and' plus bare 'and' followed by a verb-ish subject.
    comma_and = len(re.findall(r",\s+and\b", n))
    total_and = len(re.findall(r"\band\b", n))
    return comma_and >= 2 or total_and >= 4


@rule("and-had", 1.0, "trailing ', and X had done Y' (pluperfect coda tacked onto a sentence)")
def _and_had(s, n):
    return bool(re.search(r",\s+and\s+(?:then\s+)?" + PRONOUN_OR_NAME + r"(?:'d|\s+had)\s+(?!to\b)\w+", n))


@rule("and-that", 0.5, "', and that is/was ...' summarising coda")
def _and_that(s, n):
    return bool(re.search(r"\band that(?:'s| is| was| would be| had been)\b", n))


@rule("the-way", 1.5, "', the way X does Y' simile clause")
def _the_way(s, n):
    return bool(re.search(r"\bthe way (?:a|an|the|your|you|one|some|he|she|they|people|men|women|[A-Z][a-z]+'s|[a-z]+s)\b", n))


@rule("as-if", 2.0, "'as if' / 'as though' simile")
def _as_if(s, n):
    return bool(re.search(r"\bas (?:if|though)\b", n, re.I))


@rule("like-simile", 3.0, "'like a/the ...' simile (count, not a ban: check the rate)")
def _like(s, n):
    return bool(re.search(r"\blike (?:a|an|the|someone|something|being|standing|trying)\b", n))


@rule("not-x-y", 1.0, "negative parallelism: 'Not X. Y.' / 'not X but Y' / 'wasn't X. It was Y'")
def _not_x(s, n):
    return bool(
        re.match(r"\s*Not (?:a|an|the|just|only|grey|because|that|this|all|now|yet|here|in|on|from|with|like|\w+ly\b)", n)
        or re.search(r"\bnot (?:just |only |merely )?\w+(?: \w+)?,? but\b", n)
        or re.search(r"\b(?:wasn't|isn't|weren't|aren't) [^.;]{1,40}[.;] (?:It|He|She|They) (?:was|is|were|are)\b", n)
    )


@rule("fragment-run", 0.0, "three or more verbless fragments in a row (handled per paragraph)")
def _frag(s, n):
    return False  # paragraph-level; see check_paragraph


@rule("echo-open", 0.0, "three or more sentences in a row opening with the same word (paragraph-level)")
def _echo(s, n):
    return False


@rule("tag-adverb", 1.0, "dialogue tag + adverb: said quietly / softly / gently / simply / mildly")
def _tag_adv(s, n):
    return bool(re.search(
        r"\b(?:said|says|asked|murmured|agreed|replied|answered)\b,?\s+(?:\w+\s+)?(?:quietly|softly|gently|simply|mildly|flatly|evenly|lightly|carefully|slowly|dryly|drily)\b",
        s))


STOCK = [
    r"for a (?:long )?moment", r"\ba beat\b", r"let the silence", r"silence (?:stretched|sat|settled|hung)",
    r"nobody said anything", r"no one said anything", r"for the first time", r"not for the first time",
    r"something (?:in|at|about) (?:his|her|their) (?:face|eyes|voice|mouth)", r"very (?:still|slightly|quietly|gently|carefully)",
    r"all the time in the world", r"(?:a|the) weight of", r"let out a breath", r"breath (?:he|she|they) didn't know",
    r"\bsomehow\b", r"\bsomething like\b", r"didn't need to", r"which was\b", r"in the way of (?:a|an|someone|people)",
    r"the look of (?:someone|a man|a woman|somebody)", r"the kind of \w+ (?:that|who|where|you)", r"a long way off",
    r"(?:his|her|their) (?:jaw|chest) tightened", r"shiver (?:ran|went) down", r"heart (?:went|beat) faster",
    r"despite (?:himself|herself|themselves)", r"\bvery, very\b", r"\bat last\b", r"\bin the end\b",
    r"\bit was the \w+ (?:of|that)\b", r"\bthat was all\b", r"\bthat was the (?:thing|part|trick)\b",
]
STOCK_RE = re.compile("|".join(STOCK), re.I)


@rule("stock", 2.0, "stock phrase common in model prose")
def _stock(s, n):
    m = STOCK_RE.search(n)
    return m.group(0) if m else False


@rule("summary-that", 1.0, "'That was ...' / 'It was ...' sentence that explains what the scene just showed")
def _summary(s, n):
    return bool(re.match(r"\s*(?:That|It) (?:was|is) (?:all|the|his|her|their|what|how|why|enough|a good|exactly)\b", n))


@rule("ing-tail", 2.0, "trailing participle clause (', making/leaving/sending ...')")
def _ing_tail(s, n):
    return bool(re.search(r",\s+(?:making|leaving|sending|giving|turning|letting|causing|casting|filling|drawing|bringing)\s+\w+", n))


@rule("doublet", 1.0, "matched pair 'very X, and very Y' / 'X, and X-er' cadence")
def _doublet(s, n):
    return bool(re.search(r"\b(very|so|too|more|less) (\w+),? and \1 \w+", n))


@rule("em-dash", 0.0, "em dashes (rate only)")
def _dash(s, n):
    return False

# ---------------------------------------------------------------- paragraph-level checks

FRAG_VERB = re.compile(
    r"\b(?:is|was|were|are|be|been|had|has|have|do|did|does|went|came|said|saw|felt|looked|could|would|should|might|must|can|will"
    r"|\w+ed|\w+'s|\w+s)\b", re.I)


def is_fragment(sent):
    w = words(sent)
    return 0 < len(w) <= 6 and not FRAG_VERB.search(sent) and not sent.strip().startswith(('"', '“'))


def check_paragraph(sents):
    hits = []
    run = 0
    for s in sents:
        run = run + 1 if is_fragment(s) else 0
        if run == 3:
            hits.append(("fragment-run", s))
    opens = [words(narration(s))[:1] for s in sents]
    for i in range(len(opens) - 2):
        if opens[i] and opens[i] == opens[i + 1] == opens[i + 2] and opens[i][0] not in ("The", "A"):
            hits.append(("echo-open", sents[i + 2]))
    return hits

# ---------------------------------------------------------------- antislop lexicon
# Sam Paech's antislop lists: phrases and words over-represented in LLM fiction
# across 67 models (Apache-2.0). Phrases are hits; words are a density measure,
# because "nodded" or "faint" alone is fine but a page full of them is not.

_AS = json.loads((Path(__file__).parent / "data" / "antislop.json").read_text())
SLOP_PHRASE_RE = re.compile(r"\b(?:" + "|".join(re.escape(p) for p in sorted(_AS["phrases"], key=len, reverse=True)) + r")\b", re.I)
SLOP_WORDS = set(_AS["words"])
SLOP_WORD_LIMIT = 15  # per 1k words; a rate, not a ban


@rule("slop-phrase", 0.5, "phrase from the antislop list (over-represented in LLM fiction)")
def _slop_phrase(s, n):
    m = SLOP_PHRASE_RE.search(n)
    return m.group(0) if m else False

# ---------------------------------------------------------------- report

def lint(path, only=None):
    paras = load_prose(path)
    wc = 0
    dash = 0
    commas_and = 0
    slopw = Counter()
    hits = defaultdict(list)
    for ln, para in paras:
        wc += len(words(para))
        dash += para.count("—") + para.count(" -- ")
        commas_and += len(CLAUSE_AND.findall(narration(para)))
        slopw.update(w for w in words(narration(para)) if w in SLOP_WORDS)  # lowercase only: skips names like Kael
        sents = sentences(para)
        for s in sents:
            n = narration(s)
            for rid, _lim, _d, fn in RULES:
                if only and rid != only:
                    continue
                r = fn(s, n)
                if r:
                    hits[rid].append((ln, s if r is True else f"[{r}] {s}"))
        for rid, s in check_paragraph(sents):
            if not only or rid == only:
                hits[rid].append((ln, s))
    return wc, dash, commas_and, slopw, hits


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="+")
    ap.add_argument("--summary", action="store_true", help="rates only")
    ap.add_argument("--only", help="run one rule id")
    ap.add_argument("--width", type=int, default=160, help="truncate quoted sentences")
    a = ap.parse_args()

    limits = {rid: lim for rid, lim, _d, _f in RULES}
    descs = {rid: d for rid, _l, d, _f in RULES}
    total_wc, total_hits, total_dash, total_ca, total_sw = 0, Counter(), 0, 0, 0
    any_over = False

    for f in a.files:
        wc, dash, ca, slopw, hits = lint(f, a.only)
        total_wc += wc
        total_dash += dash
        total_ca += ca
        total_sw += sum(slopw.values())
        per_k = lambda c: 1000 * c / max(wc, 1)
        print(f"\n== {f}  ({wc} words; per 1k: {per_k(dash):.1f} em dashes [aim < {DASH_LIMIT}], "
              f"{per_k(ca):.1f} ', and' [aim < {COMMA_AND_LIMIT}], "
              f"{per_k(sum(slopw.values())):.1f} slop words [aim < {SLOP_WORD_LIMIT}])")
        if not a.summary and slopw:
            print("         slop words: " + ", ".join(f"{w} {c}" for w, c in slopw.most_common(12)))
        for rid in [r for r, *_ in RULES]:
            if rid not in hits:
                continue
            c = len(hits[rid])
            total_hits[rid] += c
            rate = per_k(c)
            over = rate > limits[rid]
            any_over |= over
            flag = "OVER " if over else "     "
            print(f"  {flag}{rid:<13} {c:>3}  ({rate:.1f}/1k, limit {limits[rid]})  {descs[rid]}")
            if not a.summary:
                for ln, s in hits[rid]:
                    s = s if len(s) <= a.width else s[: a.width - 1] + "…"
                    print(f"         L{ln}: {s}")

    if len(a.files) > 1:
        k = 1000 / max(total_wc, 1)
        print(f"\n== TOTAL ({total_wc} words; per 1k: {total_dash * k:.1f} em dashes, {total_ca * k:.1f} ', and', {total_sw * k:.1f} slop words)")
        for rid, c in total_hits.most_common():
            rate = 1000 * c / max(total_wc, 1)
            print(f"  {'OVER ' if rate > limits[rid] else '     '}{rid:<13} {c:>4}  ({rate:.1f}/1k)")
    sys.exit(1 if any_over else 0)


if __name__ == "__main__":
    main()
