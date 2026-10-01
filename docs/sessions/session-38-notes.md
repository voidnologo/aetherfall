# Session 38: Natural Prose — AI-ism Guide, Prose Skills, Line Edits of All Four Stories

**Date:** 2026-10-01
**Goal:** Research how AI prose gives itself away; write a guide, a linter and skills (project and reusable); line-edit Stories 01 and 04, then the published 02 and 03, without changing the stories.

## Overview

The user found Story 01 (PR #26) full of AI tics: ", and" chains, ", and X had done Y" codas, ", the way X does Y" similes. After researching the literature and existing skills (Wikipedia's Signs of AI writing, the Antislop paper and lists, blader/humanizer, Freeburg on em dashes), we wrote a guide, a linter and two skills (project `prose-check`, portable user-level `natural-prose`). Then we line-edited every piece of prose in the project without changing content: Stories 01 and 04 (heavy and-chains), the published Stories 02 and 03 (dashes, "Not X. Y."), and the whole rulebook (em dashes at 21.5/1k), ahead of a draft print and playtest.

---

## Changes Made

### Research
- Wikipedia "Signs of AI writing"; Paech et al. *Antislop* (ICLR 2026) and the antislop-sampler lists; Freeburg, *The Last Fingerprint* (em dashes: Opus 4.6 at 9.1/1k against a human baseline of 3.2/1k); EQ-Bench slop score; Gorrie on tricolon and antithesis; blader/humanizer (MIT Claude skill, 26 patterns); NousResearch autonovel ANTI-SLOP.md; Entangled Text on fiction tics.
- No official Anthropic skill covers prose quality (anthropics/skills has doc-coauthoring, internal-comms and others, none of them about prose). We borrowed humanizer's audit step and its non-fiction patterns.
- Antislop data lists **Kael** and **Elara** among the most over-used names in model fiction. Flagged to the user; canon unchanged.

### Tooling, PR #31 (merged; the first self-merge attempt was blocked, merged once the user asked for the skills to be persisted)
- `docs/writing/natural-prose.md`: the guide (tics ranked by damage, fixes, calibration table, sources).
- `tools/prose_lint.py`: per-1k rates and line hits; `tools/data/antislop.json` (top 600 phrases and 300 words, Apache-2.0).
- `.claude/skills/prose-check/SKILL.md`: measure → mark → rewrite → audit for tics that moved → report.
- CLAUDE.md "Natural Prose" rule; fiction style guide pointer.

### Persistence (user asked for the skills to be committed and reusable)
- PR #31 merged (project guide, linter, `prose-check` skill, CLAUDE.md rule).
- Standalone user-level skill `~/.claude/skills/natural-prose/` (SKILL.md, `scripts/prose_lint.py`, `scripts/data/antislop.json`, `references/guide.md`); backup in the repo at `tools/skills/natural-prose/` (PR #32, merged). Reinstall: `cp -r tools/skills/natural-prose ~/.claude/skills/`.
- Memory saved: `prose-no-ai-isms`.

### Story 04 line edit, PR #25 (commit 4cb194b)
- All eight chapters. Per 1k: and-chains 3.8 → 0.3, clause ", and" 7.0 → 3.7, "the way" 1.3 → 0.1, em dashes 7.7 → 0. 24.7k → 23.0k words. Kael's delirium fragments (ch06) and the timber pile-up (ch03) kept on purpose.

### Published stories 02 and 03, PR #33 (merged at the user's request)
- Light pass: only dashes, "Not X. Y.", "the way", summary beats. Em dashes 15 → 0.5, "Not X. Y." 2.4 → 0.5. Aldric's notebook/journal entries verbatim.
- Two continuity fixes: Story 02 ch07 POV slip; Story 03 ch05 Sera's eye colour.
- Flagged, not changed: spell names in Story 02 prose (Detect, Reveal, cantrip); Fels's "seals were intact" line in Story 03 ch07.

### Rulebook prose pass, PR #34 (open, approved as "option 2" by the user)
- Checker run over all 21 chapters (prose only): the one systemic tic was em dashes (21.5/1k rules text, 15.1/1k voice callouts). Fixed to 0.6 and 0.1. Plus "not just X, but Y", "Not X — Y", summary sentences, "the kind of place where", "something else entirely", "like a living thing".
- Wording only. Verified that every number in removed lines appears in added lines. Kept heading labels, empty "—" cells, interrupted dialogue, school-title subtitles (41 dashes).
- Grimoire: 159 table cells converted in bulk (first dash → colon, second → semicolon); user should skim.
- `tools/rulebook_prose.py` extracts rulebook prose (with source line maps) for `prose_lint.py`.

### Story 01 line edit, PR #26 (commit e07de20)
- All six chapters. Per 1k words: and-chains 4.2 → 0; clause ", and" 6.2 → 2.6 (Stories 02/03: 3.0/2.7); "the way" 1.8 → 0.4; "Not X. Y." 1.3 → 0.1; stock beats 3.9 → 0.6; em dashes 11.1 → 1.6. 11.7k → 10.9k words.
- One wording fix for continuity: "the foundry closed" (the draft doesn't say whether Ashworth is a person or a firm).

---

## Files Modified

| File | Change |
|------|--------|
| `docs/writing/natural-prose.md` | New guide: tics ranked by damage, calibration, sources |
| `tools/prose_lint.py`, `tools/data/antislop.json` | New linter + antislop lexicon (Apache-2.0) |
| `tools/rulebook_prose.py` | Extracts rulebook prose for the linter (on PR #34) |
| `.claude/skills/prose-check/SKILL.md` | New project skill |
| `tools/skills/natural-prose/` (+ `~/.claude/skills/natural-prose/`) | Portable skill and its backup |
| `CLAUDE.md`, `fiction/world/05-style-guide.md` | Natural Prose rule and pointer |
| `fiction/stories/story-01/ch01–06.md` | Line edit (PR #26, open) |
| `fiction/stories/story-04/ch01–08.md` | Line edit (PR #25, open) |
| `fiction/stories/story-02/ch01–10.md`, `story-03/ch01–08.md` | Light line edit (PR #33, merged) |
| `web/rules/*.njk` (19 chapters) | Prose pass, wording only (PR #34, open) |

## Key Design Decisions

- Budgets, not bans: every rule is a rate per 1k words, calibrated on Stories 02/03, which the user liked.
- ", and" counts only clause joins, not serial-comma lists. The antislop word density stays advisory because it barely separates the drafts the user liked from the ones they didn't.
- A line edit changes wording, never content. For the rulebook this was checked mechanically: every number in a removed line had to reappear.
- Stories 01/04 are new, so they stay on PRs for the user's read. The published 02/03 and the rulebook got lighter passes that keep the original voice.


## Open Issues

- Awaiting the user's review: #26 (Story 01), #25 (Story 04), #34 (rulebook). #25 and #26 both touch `fiction.js` and the series bible; the second to merge needs the conflict fix.
- In Story 02 the spell names (Detect, Reveal, cantrip) may break the "no mechanics in fiction" rule. User to decide.
- Antislop data lists Kael and Elara among the most over-used names in model fiction. Canon unchanged; user informed.

- After the wrap: #33 and #34 merged; site deploy verified (voidnologo.com/aetherfall); PDF rebuilt (235 pp, 44.7 MB). The user chose to keep the PDF local rather than offer it on the site.

## Next Session

- Review/merge #26, #25, #34; close draft #3. Rebuild the PDF (`python3 scripts/build-pdf.py`) for the draft print after #34 merges.
- Then the queued work: web hero and og:image cards, Hesper reroll, Story 05 plan (write it with `prose-check` from the first draft).
