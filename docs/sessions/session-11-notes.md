# Session 11: Galvanic Rating Propagation & GM Chapter Design

**Date:** 2026-04-05
**Goal:** Complete Aetheric→Galvanic rating rename propagation, then design the GM chapter ("Running the Game")

## Overview

First half: propagated "Galvanic rating" terminology to all remaining pages and design docs. The rename from session 10 had left stale "Aetheric rating" references in world-between.html, reference.html, tables.html, BASE_MECHANICS.md, WRITING_STYLE.md, and FIREARMS_EQUIPMENT.md.

Second half: designed the full GM chapter as a design doc (GM_CHAPTER.md). Covers adjudication philosophy, social situations, chases, zone management, narrating spell effects, creating devices on the fly, and four worked examples with full math.

---

## Changes Made

### Phase 1: Terminology Propagation
- Updated all remaining "Aetheric rating" references to "Galvanic rating" across 6 files
- Fixed grammar ("an Galvanic" → "a Galvanic") in FIREARMS_EQUIPMENT.md
- Clarified distinction: "Aetheric" describes magic-side concepts (accumulation, zones, balance, the Manipulation school); "Galvanic rating" describes Engine-powered device output

### Phase 2: GM Chapter Design Doc
- Created GM_CHAPTER.md with 8 sections covering all GM-facing guidance
- Introduced 4 new mechanical elements:
  1. **Stat-based quick checks** — `(5 + stat) × 10` for raw capability tests (range 20-80), distinct from unskilled formula (×5, range 10-40)
  2. **NPC Disposition modifiers** — 5-tier system from Hostile (−30%) to Allied (+30%), GM guidance not rigid tracking
  3. **Chase structure** — timing track extension with Sprint, obstacles, shortcuts, complications table (d6), vehicle speeds. PLAYTEST NOTE flagged.
  4. **Location baseline table** — 12 common locations with Aetheric/Galvanic baseline ranges
- Wrote 4 worked examples with full math:
  1. "The Dockmaster's Favor" — social encounter (Etiquette, Persuasion, Deception vs. Empathy)
  2. "Through the Market District" — foot chase with timing track, obstacles, zone transition
  3. "The Holloway House" — exploration with zone tracking, accumulation math, room-by-room gradient
  4. "The Resonance Cage" — improvised device creation using quick creation method

---

## Files Modified

| File | Change |
|------|--------|
| web/rules/world-between.html | "Aetheric rating" → "Galvanic rating", table header updated |
| web/rules/tables.html | Table index description updated |
| web/rules/reference.html | Cheat sheet line updated |
| docs/requirements/BASE_MECHANICS.md | Balance shift table + worked example updated |
| docs/requirements/WRITING_STYLE.md | Terminology table entry + example updated |
| docs/requirements/FIREARMS_EQUIPMENT.md | Stat name, table headers, device template, all 6 device listings updated |
| docs/requirements/GM_CHAPTER.md | NEW — full GM chapter design doc |
| docs/sessions/session-11-notes.md | This file |

## Key Design Decisions

1. **Stat-based quick check (×10 vs ×5)** — The unskilled formula maxes at 40%, which is right for "attempting a skilled task without training." But raw capability tests (resist poison, hold breath) need a wider range. ×10 gives 20-80%, which feels correct for "how tough/smart/charming are you, fundamentally?"

2. **NPC Dispositions as guidance, not system** — The 5-tier table (−30% to +30%) anchors social encounters in concrete numbers without requiring the GM to track a stat per NPC. Some GMs will use it precisely, others will eyeball it. Both are valid.

3. **Chase soft cap at 15-20 counts** — Chases that drag past 20 counts lose tension. The forced final opposed check ensures resolution without feeling arbitrary — whoever's been performing better mechanically probably wins the final check too.

4. **Backlash narration table** — Each spell concept gets its own backlash flavor. This turns a mechanical penalty into a narrative moment. Force backlash is concussive rebound; Mend backlash is healing gone wrong; Commune backlash is something whispering back.

5. **Device balance test (three questions)** — "Does it replace a character ability? Does it have meaningful cost? Does it solve the problem too cleanly?" Quick gut-check before handing players a new toy.

6. **Creative spell use framework (three questions)** — "Does the concept cover this? What tier required? Is it within that tier's scope?" Gives GMs a structured way to adjudicate creative spell proposals without needing a ruling for every possible use.

## Open Issues

- Stat-based quick check formula is new and untested — may need tuning after playtest
- Chase rules are PLAYTEST NOTE — pacing, soft cap, and vehicle speeds may need adjustment
- GM chapter web page (running-the-game.html) not yet created — planned for next session
- Web page creation requires renumbering Reference (11→12) and Tables (12→13), updating PAGES array and navigation links

## Next Session
- Create web/rules/running-the-game.html (chapter 11, neutral theme)
- Update main.js PAGES array — insert new chapter, renumber Reference and Tables
- Update equipment.html next link → running-the-game.html
- Update reference.html chapter number and prev link
- Update tables.html chapter number
- Define major factions and Adventuring Societies
