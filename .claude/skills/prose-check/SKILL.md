---
name: prose-check
description: Check and clean prose for AI-isms (", and" chains, ", and X had done Y" codas, "the way X does Y" similes, "Not X. Y." contrasts, lists of three, echo openings, summary sentences, stock beats, adverb tags, antislop phrases). Use after writing or revising any Aetherfall fiction, voice callout, rulebook prose or PR description, when the user says "prose check", "AI-isms", "slop", "make it read naturally", or before committing a story chapter.
---

# Prose Check

Line-edit prose so it reads like a person wrote it. The full guide, with examples, research and calibration, is `docs/writing/natural-prose.md`. Read it first if it isn't already in context.

## Workflow

### 1. Measure

```bash
python3 tools/prose_lint.py --summary <files>
```

Note every `OVER` rule and the header rates: clause-joining `, and` (limit 4 per 1k), em dashes (8), antislop words (15, advisory).

### 2. Mark

```bash
python3 tools/prose_lint.py <file>                    # every rule, with line numbers
python3 tools/prose_lint.py --only and-chain <file>   # one rule
```

The script finds candidates; you decide. It misses things (a list of three without commas, rhythm repeated across paragraphs) and flags things that are fine (abbreviations read as fragments, "walk out the way you came"). Read the whole chapter once and mark what the script can't see.

### 3. Rewrite, a chapter at a time

Write the cleaned chapter in full. In priority order:

1. **And-chains and ", and" codas.** Split into sentences. Subordinate or cut the weaker clause. This one fix does most of the work.
2. **Summary sentences** ("That was the...", "It was the look of someone who..."). Delete, then check nothing was lost.
3. **Similes** ("the way X does Y", "as if", "like a"). Keep the best one or two a chapter. Never two in a sentence.
4. **"Not X. Y."** State the true thing.
5. **Adverb tags and stock beats.** "said" or no tag. Cut "for a long moment", "let the silence sit", "very still", "at last", and anything on the antislop list.
6. **Echo openings and fragment runs.** Vary.
7. **Em dashes.** Use commas, colons, full stops or parentheses where the dash isn't doing real work. Keep dashes for interrupted dialogue.

### 4. Audit the rewrite

Run the linter again, then re-read the rewrite and ask what still sounds machine-made. Look for tics that **moved** instead of disappearing:

- "the way" turned into "like" or "as if"
- an and-chain turned into "She X. She Y. She Z."
- everything chopped to the same short length (vary it)

Fix those and run the linter once more.

### 5. Hold the line

- Change wording, not story. Keep every plot beat, fact, name, continuity detail and the meaning of every line of dialogue. Don't invent details to fill a gap left by a cut (Story 01: "Ashworth had built it" doesn't tell you whether Ashworth is a person or a firm, so don't write "he").
- Keep each character's voice (`fiction/world/05-style-guide.md`, POV section). Kael stays clipped; Aldric stays precise; Mira stays quick.
- Rulebook text needs explicit user approval before it changes (CLAUDE.md). For rulebook prose, report the hits and proposed edits; don't apply them unasked.

### 6. Report

Give before/after rates for the files you touched, plus the hits you kept on purpose and why.
