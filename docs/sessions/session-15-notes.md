# Session 15: Voice & Sidebar Enhancement Pass

**Date:** 2026-04-06
**Goal:** Review the entire rulebook (chapters 4-13) and add voice callouts (Handler, Scholar, Street, Believer), "For the GM" sidebars, and "At the Table" examples where they bring the book alive or clarify points.

## Overview

Added 35 voice sidebars and GM notes across all 10 mechanics chapters (4-13). Initial pass wrote some voice callouts as rules commentary rather than in-world perspective — user caught this and clarified the distinction: voices are people in the world sharing experiences, not meta-commentary on game design. Fixed 12 sidebars to be properly experiential and in-character. Codified the distinction in WRITING_STYLE.md with "the tavern test" and good/bad examples.

---

## Changes Made

### Voice Sidebar Pass (35 sidebars added)
- **Creating (Ch 4):** 3 — Handler on survival concepts, GM on skill divergence, Scholar on coming to casting late
- **Rolling (Ch 5):** 3 — Handler on a master fencer's precision, GM on mutual failure, Street on a fast draw on Vicker Street
- **Getting Hurt (Ch 6):** 3 — Handler on what wounds feel like, GM on death save drama, Street on recovery as luxury
- **Skills (Ch 7):** 4 — Handler on a lockpick kid, Street on Sootwell Row survival, Scholar on a team lost near Thornfeld, GM on social rolls
- **Magic (Ch 8):** 3 — Believer on casting as conversation, Handler on scholarly vs wild from experience, Street on watching backlash drop a caster
- **Grimoire (Ch 9):** 6 — One per school (Believer, Street, Handler, Scholar, GM, Believer)
- **World Between (Ch 10):** 3 — Believer on the Veil as membrane, Handler on carrying a blade, Street on reading zones like weather
- **Combat (Ch 11):** 2 — Handler on a knife fighter beating a gunman, Street on range shifting with the zone
- **Equipment (Ch 12):** 6 — Handler x2 on kit selection and armor, Street x2 on reliability and vehicles, Scholar on Galvanic uniqueness, GM on oddities as exploration tools
- **Running the Game (Ch 13):** 2 — Scholar on fieldwork with imprecise patterns, Believer on witnessing backlash firsthand

### Voice Sidebar Corrections (12 rewritten)
- Rewrote 12 sidebars that read as rules commentary into proper in-world experiential voice
- Handler sidebars became mission stories, Scholar became fieldwork experiences, Street became survival stories with named streets, Believer became spiritual encounters

### Writing Guide Update
- Added "Voice Callouts vs. GM Notes" section to WRITING_STYLE.md
- The tavern test: "Could this be spoken by a person in a tavern?"
- Good/bad examples, voice personality summaries, complementary usage guidance

---

## Files Modified

| File | Change |
|------|--------|
| web/rules/creating.html | +3 sidebars (Handler, GM, Scholar) |
| web/rules/rolling.html | +3 sidebars (Handler, GM, Street) |
| web/rules/getting-hurt.html | +3 sidebars (Handler, GM, Street) |
| web/rules/skills.html | +4 sidebars (Handler, Street, Scholar, GM) |
| web/rules/magic.html | +3 sidebars (Believer, Handler, Street) |
| web/rules/grimoire.html | +6 sidebars (Believer x2, Street, Handler, Scholar, GM) |
| web/rules/world-between.html | +3 sidebars (Believer, Handler, Street) |
| web/rules/combat.html | +2 sidebars (Handler, Street) |
| web/rules/equipment.html | +6 sidebars (Handler x2, Street x2, Scholar, GM) |
| web/rules/running-the-game.html | +2 sidebars (Scholar, Believer) |
| docs/requirements/WRITING_STYLE.md | New section: Voice Callouts vs. GM Notes |

## Key Design Decisions

- **Voice callouts are in-world, not meta.** Voices are people sharing experiences with other people. They never reference game mechanics, design philosophy, or the reader's role. GM notes handle that. Codified as "the tavern test" in WRITING_STYLE.md.
- **Light touch on well-served chapters.** Combat (already 8 callouts) and Running the Game (already 15+) got only 2 each. Grimoire (had 0) and Equipment (had 3) got 6 each.

## Open Issues

- None from this session

## Next Session
- Game/GM tools and downloadable character sheet
