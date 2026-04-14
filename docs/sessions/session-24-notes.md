# Session 24: Eleventy Migration, Economy Integration & Unified Character Sheets

**Date:** 2026-04-13
**Goal:** Migrate rulebook to Eleventy, design starting Station/Backing mechanics, integrate economy across all chapters, unify character sheets into a single template with JSON data.

## Overview

Major infrastructure and content session. Migrated the entire web rulebook from 20 static HTML files to Eleventy with a shared layout template, 9 callout shortcodes, and build-time page chrome. Added Starting Station trade mechanic and Starting Backing rules to the economy system. Removed Downtime Actions (rejected). Integrated economy references into Creating, Societies, Equipment, and GM chapters. Updated the character builder with Station/Backing/Ledger fields and save/load JSON.

Then unified all 7 character sheet files (blank, sample, 4 quickstart pre-gens) into a single Nunjucks template driven by JSON data files — eliminating 4,065 lines of duplication. Character data now lives in `web/_data/characters/*.json`; 11ty pagination generates all sheets at build time. The builder exports/imports the same JSON format, so player saves and build configs are interchangeable.

Also completed Phase 3 cleanup: sidebar chapter list moved to build-time, PAGES duplication eliminated from main.js (-125 lines), and added an "Economy at the Table" section to the GM chapter.

---

## Changes Made

### Eleventy Migration
- 11ty config, layout template, pages.json, 9 callout shortcodes, flat-URL permalinks
- All 20 chapters converted from .html to .njk (920 lines boilerplate removed)
- GitHub Action updated with Node + build step
- main.js simplified: removed PAGES const, initPageChrome(), buildSidebar(), initPageTransitions() (-125 lines total)
- Sidebar chapter list generated at build time in layout template

### Economy Design & Rulebook Updates
- Starting Station trade (±1 for 3 skill levels) — design doc + rulebook
- Starting Backing (default 3, GM adjusts) — design doc + rulebook
- Downtime Actions rejected (Drift is the point) — kept in design doc with rationale
- Creating chapter: new Step 6 (Station), Step 7 (Equipment with Cost Tiers), Magic → Step 8
- Societies chapter: Backing + Ledger as step 5
- Equipment chapter: Cost Tier explanation
- Character Sheet page: Station and Society economy fields in builder/sheet descriptions
- GM chapter: new "Economy at the Table" section + economy entries in GM Toolkit table

### Character Builder
- Station (0-5, default 2) in Identity section
- Backing (1-5, default 3) and Ledger (4 states, default Level) in Society section
- All three print to character sheet output
- Save JSON: exports character as JSON file (same format as build data)
- Load JSON: imports a file and populates entire form

### Unified Character Sheets
- Single `sheet.njk` template replaces 6 standalone HTML files (4,065 lines deleted)
- Character data as JSON: `web/_data/characters/{blank,sample,kael,sera,aldric,mira}.json`
- `characters.js` data aggregator + `sheets.njk` pagination driver
- All existing URLs preserved via `filename` field
- To add a character: drop a JSON file, it builds automatically
- Player save files and build configs are the same format

---

## Files Modified

| File | Change |
|------|--------|
| `eleventy.config.js` | New — 11ty config |
| `package.json`, `package-lock.json` | New — 11ty dependency |
| `.gitignore` | Added node_modules/, _site/ |
| `.github/workflows/pages.yml` | Node + build step |
| `web/_data/pages.json` | New — chapter registry |
| `web/_data/characters.js` | New — aggregates character JSONs for pagination |
| `web/_data/characters/*.json` (6 files) | New — character data (blank, sample, 4 pre-gens) |
| `web/_includes/chapter.njk` | New — chapter layout with build-time sidebar |
| `web/_includes/sheet.njk` | New — canonical character sheet template |
| `web/rules/sheets.njk` | New — pagination driver for sheet generation |
| `web/rules/js/main.js` | Removed PAGES, buildSidebar, initPageChrome, initPageTransitions |
| `web/rules/*.njk` (20 files) | All chapters: .html → .njk with shortcodes |
| `web/rules/creating.njk` | Station step, equipment with Cost Tiers |
| `web/rules/societies.njk` | Backing + Ledger as step 5 |
| `web/rules/equipment.njk` | Cost Tier explanation |
| `web/rules/economy.njk` | Starting Station trade, Starting Backing, Downtime Actions removed |
| `web/rules/running-the-game.njk` | Economy at the Table section, GM Toolkit entries |
| `web/rules/character-sheet.njk` | Updated builder/sheet field descriptions |
| `web/rules/tools/character-builder.html` | Station/Backing/Ledger fields, save/load JSON |
| `web/rules/tools/tools.json` | Excludes tools/ from 11ty processing |
| `docs/requirements/ECONOMY.md` | Starting Station/Backing rules, Downtime Actions rejected |
| Deleted: `web/rules/tools/character-sheet.html` | Replaced by sheet.njk template |
| Deleted: `web/rules/tools/character-sheet-sample.html` | Replaced by sample.json + template |
| Deleted: `web/rules/tools/quickstart-{kael,sera,aldric,mira}.html` | Replaced by JSON + template |

## Key Design Decisions

1. **Eleventy over Jekyll** — Node-based, clean shortcodes, no Ruby
2. **Flat URL permalinks** — Global config preserves existing URL structure
3. **Build-time page chrome and sidebar** — Layout generates everything, JS only does section TOC + scroll spy
4. **Station trade at 3 skill levels** — ~15% of starting investment, creates organic diversity
5. **Downtime Actions rejected** — The Drift is the pressure; take jobs or slide
6. **Unified character sheets from JSON** — One template, data files, build generates all. Same format for build configs and player saves.
7. **Save/load in builder uses build format** — A player's exported JSON can be dropped into _data/characters/ to generate a static sheet. Zero conversion needed.

## Open Issues

- Character builder's print template (JS) and sheet.njk (Nunjucks) are parallel implementations of the same layout — the one remaining duplication point
- Landing page still standalone with duplicated CSS
- Visual review of all generated character sheets for print layout accuracy
- Bare `callout` class has no shortcode (Intimidation flex-stat note)

## Next Session

- Visual review of site and sheets in browser
- Character sheet art / watermarks
- Align builder print template with sheet.njk (or accept the duplication)
- Design work: bestiary, archetypes, zone mechanics
