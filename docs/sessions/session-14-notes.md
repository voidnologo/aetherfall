# Session 14: Resolve Open Questions, Build Web Chapters, Navigation Restructure

**Date:** 2026-04-06
**Goal:** Resolve all WORLD_DESIGN.md §9 open questions, build the web chapters for State of the World and Adventuring Societies, restructure the rulebook from 13 to 15 chapters with world→group→individual flow.

## Overview

Resolved all ten open design questions from WORLD_DESIGN.md §9, then built two new web chapters: "The State of the World" (Ch 2) and "Adventuring Societies" (Ch 3). Restructured the entire 15-chapter rulebook to flow from world context → group context (Society) → individual character creation. Added four voice callout CSS styles (Handler, Scholar, Street, Believer) for inline sidebar commentary. Fixed TOC sidebar truncation for long chapters and converted adventure hooks to bullet lists.

---

## Changes Made

### Open Question Resolution
- All 10 questions in WORLD_DESIGN.md §9 resolved and locked in
- PROJECT_SPEC.md §2.5 and §2.6 updated with full cross-references to WORLD_DESIGN.md

### New Web Chapters
- **state-of-the-world.html (Ch 2):** History, rumors & wonders, three ideological currents, four detailed factions + four summary factions in table, zone politics. Uses all four voice callouts as sidebars.
- **societies.html (Ch 3):** What a Society is, patron relationship, seven archetypes with tension column, faction-specific gear, Society ecosystem, Session Zero building framework. Bridges world to character creation.

### Navigation Restructure
- PAGES array in main.js expanded from 13 to 15 entries
- All existing chapters renumbered +2 (creating 4, rolling 5, ... tables 15)
- Chapter numbers updated in all HTML headers and page heroes
- Prev/next navigation links updated (Welcome → State of the World → Societies → Creating)

### CSS & Visual Fixes
- Four voice callout styles added: callout-handler (grey), callout-scholar (aether blue), callout-street (galvanic gold), callout-believer (green)
- TOC sidebar max-height increased from 500px to 1200px (world chapter has 26 sections)
- Adventure hooks converted from run-on paragraphs to bullet lists

---

## Files Modified

| File | Change |
|------|--------|
| docs/requirements/WORLD_DESIGN.md | §9 open questions resolved with decisions |
| docs/requirements/PROJECT_SPEC.md | §2.5-2.6 updated with cross-references |
| docs/requirements/WORLD_DESIGN_PLAN.md | Execution plan (created last session) |
| web/rules/state-of-the-world.html | NEW — Chapter 2, The State of the World |
| web/rules/societies.html | NEW — Chapter 3, Adventuring Societies |
| web/rules/css/styles.css | Voice callout styles, TOC max-height fix |
| web/rules/js/main.js | PAGES array expanded to 15 chapters |
| web/rules/index.html | Next link → state-of-the-world, chapter number unchanged |
| web/rules/creating.html | Prev link → societies, chapter 2 → 4 |
| web/rules/rolling.html | Chapter 3 → 5 |
| web/rules/getting-hurt.html | Chapter 4 → 6 |
| web/rules/skills.html | Chapter 5 → 7 |
| web/rules/magic.html | Chapter 6 → 8 |
| web/rules/grimoire.html | Chapter 7 → 9 |
| web/rules/world-between.html | Chapter 8 → 10 |
| web/rules/combat.html | Chapter 9 → 11 |
| web/rules/equipment.html | Chapter 10 → 12 |
| web/rules/running-the-game.html | Chapter 11 → 13 |
| web/rules/reference.html | Chapter 12 → 14 |
| web/rules/tables.html | Chapter 13 → 15 |

## Key Design Decisions

- **World → Group → Individual chapter flow.** Reader needs to understand the world, then how Societies work in it, before they can build a character that fits. Large to small context grounding.
- **Societies as a separate chapter.** Bridges world-setting and player-facing rules — a different kind of content (decisions the table makes) than lore (context the table absorbs).
- **Split theme for world chapter.** Uses `data-theme="split"` since the content covers both Aetheric and Galvanic forces equally.
- **Voice callouts as sidebars, not main content.** The four voices (Handler, Scholar, Street, Believer) add flavor and perspective but the main text carries the information. Voices make it feel like real people commenting.
- **3-4 detailed factions + summary table.** Detailed factions show the depth; summary table shows the breadth. Neither set is "more important" than the other.

## Open Issues

- User wants voice callouts (Handler, Scholar, Street, Believer), "For the GM" sidebars, and "At the Table" examples carried through the rest of the book (chapters 4-13) where they make sense — this is the next session's primary task
- Game/GM tools and downloadable character sheet still pending

## Next Session
- Review the entire rulebook (chapters 4-13) and sprinkle in voice callouts, "For the GM" sidebars, and "At the Table" examples where they would bring the book more alive or clarify points
- Then: Game/GM tools and downloadable character sheet
