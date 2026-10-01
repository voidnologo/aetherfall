---
name: natural-prose
description: Check and line-edit prose for AI-isms so it reads like a person wrote it. Catches ", and" clause chains, ", and X had done Y" codas, "the way X does Y" similes, "Not X. Y." contrasts, summary sentences, lists of three, echo openings, stock beats ("for a long moment", "voice barely above a whisper"), adverb dialogue tags, em-dash overuse, and the antislop phrase lists. Use on fiction, docs, READMEs, PR descriptions or any prose when the user says "AI-isms", "slop", "sounds like AI", "make it read naturally", "humanize", or "prose check", and after drafting long prose yourself.
---

# Natural Prose

Line-edit prose so it reads like a person wrote it. The full guide (tics ranked by damage, examples, fixes, research and sources) is `references/guide.md`. Read it before a first edit in a session.

A project may have its own wrapper (for example a `prose-check` skill with house voice rules). If it does, follow the project's rules and use this skill for the method.

## 1. Measure

```bash
python3 ~/.claude/skills/natural-prose/scripts/prose_lint.py --summary <files>
```

The script reads Markdown or plain text and skips headings, lists, tables, blockquotes and front matter. It also strips quoted dialogue from the narration rules. It prints per-1,000-word rates and marks `OVER` where a rate passes its limit. Header rates: clause-joining `, and` (limit 4), em dashes (8), antislop words (15, advisory). Exit code 1 means something is over.

To set limits for a new project, run it over a few pages the user says read well and use those rates as the ceiling.

## 2. Mark

```bash
python3 ~/.claude/skills/natural-prose/scripts/prose_lint.py <file>                  # all hits with line numbers
python3 ~/.claude/skills/natural-prose/scripts/prose_lint.py --only and-chain <file> # one rule
```

A hit is a prompt to look, not a verdict. The script misses lists of three without commas and rhythm repeated across paragraphs. It also flags harmless things, such as abbreviations read as fragments, or "the way you came". Read the whole passage once and mark what the script can't see.

## 3. Rewrite

Rewrite a chapter or section at a time, in priority order:

1. **And-chains and ", and" codas.** Split into sentences. Subordinate or cut the weaker clause. This one fix does most of the work.
2. **Summary sentences** ("That was the...", "It was the look of someone who..."). Delete, then check nothing was lost.
3. **Similes** ("the way X does Y", "as if", "like a"). Keep the best one or two a chapter. Never two in a sentence.
4. **"Not X. Y."** State the true thing.
5. **Adverb tags and stock beats.** Use "said" or no tag. Cut "for a long moment", "let the silence sit", "very still", "at last", and anything on the antislop list.
6. **Echo openings and fragment runs.** Vary them.
7. **Em dashes.** Use commas, colons, full stops or parentheses where the dash isn't doing real work. Keep dashes for interrupted dialogue.

In non-fiction, also cut announcements before the point, inflated significance, bold labels on every bullet, writing about the document instead of its subject, chat residue and stacked hedges (guide §10).

## 4. Audit the rewrite

Run the linter again, then re-read and ask what still sounds machine-made. Look for tics that **moved** rather than disappeared:

- "the way" turned into "like" or "as if"
- an and-chain turned into "She X. She Y. She Z."
- everything chopped to one short length (vary it)

## 5. Hold the line

- Change wording, not content. Keep every fact, plot beat, name, continuity detail and the meaning of every line of dialogue. Don't invent details to fill gaps left by cuts.
- Keep each character's or author's voice. Read a sample the user likes and match it.
- If the text is canon or needs sign-off (rules, legal, published copy), report the hits and proposed edits instead of applying them.

## 6. Report

Give before/after rates for the files you touched, plus any hits you kept on purpose and why.
