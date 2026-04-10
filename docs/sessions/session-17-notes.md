# Session 17: Character Sheet & Interactive Builder

**Date:** 2026-04-06
**Goal:** Create a downloadable blank character sheet PDF and an interactive web-based character builder form.

## Overview

Built a complete character sheet system: a 2-page printable blank sheet, a filled-out sample character (Elara Voss), and an interactive character builder form that auto-calculates all derived values and generates the same printable layout. Recovered the original character sheet from git history as a layout reference, then redesigned it from scratch to reflect the current game system (exhaustion tracks, dual soak armor, Scholarly/Wild casting paths, Aetheric balance, etc.).

Also removed "complexity" as a player-facing concept from the grimoire — it remains in design docs but spell entries now show only casting time and per-tier exhaustion costs directly. The character sheet got its own dedicated page in the TOC (between Creating Your Adventurer and Rolling the Dice) since it's a player tool, not just a GM tool.

---

## Changes Made

### Blank Character Sheet (`web/rules/tools/character-sheet.html`)
- 2-page portrait layout, print-ready HTML
- Page 1: header (name/player/archetype), attributes with -3 to +3 bubbles, weapons table (unarmed prefilled), armor with soak totals, character description, 15 skill rows, XP tracker, full-width wound + exhaustion tracks with 10 boxes per tier
- Page 2: magic section (path checkboxes, casting stats), 12-row spell table (W/S/St/Sp exhaustion), inventory, society, faction, contacts, backlash effects, notes, quick reference formula bar
- Tool-header matching site style (Playfair Display, dark background, teal accents)

### Sample Character Sheet (`web/rules/tools/character-sheet-sample.html`)
- Fully filled-out example: Elara Voss, Smoke Surgeon, Scholarly caster
- Attributes marked, 13 skills with calculated targets, weapons/armor filled, 8 spells, society details, contacts, in-progress damage/exhaustion marked, backlash effect active
- Tests that all fields have adequate space for real data

### Interactive Character Builder (`web/rules/tools/character-builder.html`)
- Form wizard UI with site color palette (deep blue backgrounds, teal/amber accents)
- Clickable attribute bubbles (-3 to +3), auto-calculates net total, HP/tier, EP/tier, concentration
- Skill dropdowns (alphabetical, showing parent stat), auto-fills stat and calculates target number, tracks pool budget with over-budget warnings
- Weapon/armor text inputs with add/remove rows, auto-totals soak and hinder
- Magic path selector: Scholarly shows individual spell picker, Wild shows school picker (select 2 schools, see all spells)
- Spell dropdown auto-fills school, casting time, and all 4 exhaustion tier costs
- Society, faction, contacts, inventory, notes — all text inputs
- Floating action bar (Reset/Print) stays visible while scrolling
- Print generates the same 2-page layout as the blank sheet with all data filled in, crossed-out HP/EP boxes based on actual stats

### Character Sheet Page (`web/rules/character-sheet.html`)
- Dedicated rulebook page with site chrome (sidebar, header, navigation)
- Links to builder, blank sheet, and sample
- Feature tables describing builder capabilities and sheet contents
- Quick reference formula table
- Positioned in TOC between Creating Your Adventurer and Rolling the Dice

### Grimoire Changes (`web/rules/grimoire.html`)
- Removed "Complexity" from all 37 spell-meta lines (was "Complexity: X — Casting Time: Yct", now just "Casting Time: Yct")
- Removed the complexity-to-exhaustion reference table
- Each spell still has its per-tier exhaustion costs in its own effect table

### Navigation Updates
- Added Character Sheet to PAGES array in main.js (arrow icon, after Ch 04)
- Updated Creating Your Adventurer next link to Character Sheet
- Updated Rolling the Dice prev link to Character Sheet
- Removed character sheet section from GM Tools page
- All character tools link back to Character Sheet page (not GM Tools)

---

## Files Modified

| File | Change |
|------|--------|
| web/rules/tools/character-sheet.html | NEW — 2-page printable blank character sheet |
| web/rules/tools/character-sheet-sample.html | NEW — filled-out sample (Elara Voss) |
| web/rules/tools/character-builder.html | NEW — interactive form with auto-calc + print output |
| web/rules/character-sheet.html | NEW — dedicated Character Sheet page in rulebook |
| web/rules/grimoire.html | Removed complexity labels from all spell entries and reference table |
| web/rules/gm-tools.html | Removed character sheet section (moved to own page) |
| web/rules/js/main.js | Added Character Sheet to PAGES array |
| web/rules/creating.html | Next link points to Character Sheet |
| web/rules/rolling.html | Prev link points to Character Sheet |

## Key Design Decisions

- **HTML over generated PDF.** Print-ready HTML gives us both a downloadable PDF (via browser print) and the foundation for the interactive builder — same layout, two entry points.
- **Form wizard, not sheet layout.** The builder doesn't mirror the sheet layout — it's a proper form with dropdowns and auto-calc. Generates the sheet layout only at print time.
- **Wild casters pick schools, not spells.** Wild casters select 2 schools and automatically know all spells in those schools. The form reflects this with a school picker instead of individual spell selection.
- **Complexity removed from player-facing content.** Complexity is a design-side concept that maps to exhaustion costs. Players just need to see the costs directly on each spell. Complexity remains in design docs.
- **Character Sheet as a top-level page.** Not buried under GM Tools — players need it immediately after character creation. Arrow icon in sidebar distinguishes it from numbered chapters.
- **10 boxes per tier row.** Maximum possible is 7+3=10 (BR or PW at +3). Players cross out unused boxes based on their actual attribute values.

## Open Issues

- Wild caster school count is hardcoded to 2 in the builder JS — may need to be configurable if rules change
- No save/load for builder data (localStorage could preserve work-in-progress)
- Art/watermark for the character sheet — blank space reserved on page 1
- Builder doesn't validate creation-time skill cap (level 3 max at creation vs 5 max in play)

## Next Session
- Visual polish on character sheet (art, watermarks)
- Save/load character data in builder (localStorage)
- Any other playtest feedback iteration
