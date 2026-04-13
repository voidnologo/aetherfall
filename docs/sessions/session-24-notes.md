# Session 24: Eleventy Migration, Economy Rules & Integration

**Date:** 2026-04-13
**Goal:** Evaluate and implement a web framework for the rulebook site, design starting Station/Backing mechanics, integrate economy system into all relevant chapters, update character builder.

## Overview

Evaluated Jekyll, Astro, and Eleventy for the rulebook site. Chose Eleventy (11ty) for zero client-side overhead, clean shortcode syntax, and Node-based local dev (no Ruby). Built the full infrastructure — layout template, pages.json data file, 9 callout shortcodes, flat-URL permalinks, GitHub Action with build step — then converted all 20 chapter files from static HTML to .njk templates. Removed ~920 lines of duplicated boilerplate. The `initPageChrome()` JS function was deleted since page chrome is now generated at build time.

Added Starting Station trade mechanic (±1 Station for 3 skill levels) and Starting Backing rules (default 3, GM adjusts for tone) to the economy design doc and rulebook. Removed Downtime Actions (rejected — the Drift's pressure is the point). Integrated economy references into Creating Your Adventurer (new Station step, equipment rewritten around Cost Tiers), Adventuring Societies (Backing + Ledger as step 5), Character Sheet (Station and Society economy fields), and Equipment (Cost Tier explanation). Updated the interactive character builder with Station, Backing, and Ledger fields.

---

## Changes Made

### Eleventy Migration
- **11ty config** (`eleventy.config.js`): Input from `web/`, output to `_site/`, flat URL permalinks, passthrough for CSS/JS/tools/assets
- **Layout template** (`web/_includes/chapter.njk`): Single source of truth for page shell — theme, fonts, atmosphere, sidebar, header, nav, footer, scripts. Supports `extraHead`/`extraFoot` for special pages.
- **Pages data** (`web/_data/pages.json`): PAGES registry as build-time data — drives chapter numbers, titles, themes, and prev/next navigation
- **9 callout shortcodes**: handler, scholar, street, believer (fixed label), gmnote, example, warning, scene (custom label with defaults)
- **All 20 chapters** converted from .html to .njk — boilerplate stripped, callouts converted to shortcodes
- **GitHub Action** updated to install Node, run `npm ci` + `npx @11ty/eleventy`, deploy `_site/`
- **main.js** simplified — `initPageChrome()` removed (65 lines), sidebar still JS-generated from PAGES

### Economy Design Updates
- **Starting Station trade**: ±1 from Backing floor costs/gains 3 skill levels from one group pool. Max Station 3 at creation. Station 0 requires a character hook.
- **Starting Backing**: Default 3 (Full Package), GM adjusts for campaign tone (gritty 1-2, standard 3, elite 4-5). Table-level decision.
- **Downtime Actions rejected**: Drift pressure is the point — no mini-games to counteract it. Record kept in design doc with rationale.

### Economy Integration Across Chapters
- **Creating Your Adventurer**: New Step 6 (Station), Step 7 (Equipment rewritten around Cost Tiers), Magic renumbered to Step 8
- **Adventuring Societies**: New step 5 (Backing + Ledger) in Building Your Society section
- **Character Sheet page**: Station and Society economy fields added to builder and blank sheet descriptions
- **Equipment**: Cost Tier explanation paragraph added before weapon tables

### Character Builder Tool
- **Station** (0-5, default 2) added to Identity section with trade hint
- **Backing** (1-5, default 3) and **Ledger** (Flush/Level/Lean/Dire, default Level) added to Society section
- All three print to the character sheet output
- Reset clears to defaults

---

## Files Modified

| File | Change |
|------|--------|
| `eleventy.config.js` | New — 11ty config with shortcodes, filters, passthrough, flat URLs |
| `package.json` | New — 11ty dependency, build/dev scripts |
| `package-lock.json` | New — lockfile |
| `.gitignore` | Added node_modules/ and _site/ |
| `.github/workflows/pages.yml` | Added Node setup + 11ty build step before deploy |
| `web/_data/pages.json` | New — PAGES registry as build-time data |
| `web/_includes/chapter.njk` | New — layout template for all chapters |
| `web/rules/tools/tools.json` | New — excludes tools/ from 11ty processing |
| `web/rules/js/main.js` | Removed initPageChrome() (now build-time) |
| `web/rules/*.njk` (20 files) | All chapters converted from .html to .njk with frontmatter + shortcodes |
| `web/rules/creating.njk` | New Station step, equipment rewritten around Cost Tiers |
| `web/rules/societies.njk` | Backing + Ledger as step 5 in Society creation |
| `web/rules/character-sheet.njk` | Station and Society economy fields added |
| `web/rules/equipment.njk` | Cost Tier explanation paragraph added |
| `web/rules/economy.njk` | Starting Station trade, Starting Backing, Downtime Actions removed |
| `docs/requirements/ECONOMY.md` | Starting Station trade, Starting Backing, Downtime Actions rejected |
| `web/rules/tools/character-builder.html` | Station, Backing, Ledger fields added to form + print |

## Key Design Decisions

1. **Eleventy over Jekyll** — Node-based (no Ruby dependency), cleaner paired shortcodes, unconstrained plugin ecosystem
2. **Flat URL permalinks** — Global config outputs `rules/economy.html` not `rules/economy/index.html`
3. **Callout shortcodes** — 4 voice (fixed label) + 5 utility (custom label with defaults)
4. **Build-time page chrome** — Layout generates chapter numbers, header text, prev/next nav
5. **Station trade at 3 skill levels** — ~15% of typical starting investment, meaningful not crippling
6. **Downtime Actions rejected** — Dilutes the Drift's purpose
7. **Station step before Equipment in character creation** — Must know your Station to pick gear
8. **Economy fields default but adjustable** — Station defaults to 2, Backing to 3, Ledger to Level

## Open Issues

- PAGES duplication between pages.json and main.js — resolve in Phase 3 cleanup
- Sidebar chapter list still JS-generated — could move to build-time
- Blank printable character sheet needs Station and Society economy fields added
- Landing page (web/index.html) still standalone with duplicated CSS
- Review all chapters in browser for visual regression after 11ty conversion
- Bare `callout` class (Intimidation flex-stat note) has no shortcode

## Next Session

- Review site in browser for visual regression
- Add Station/Backing/Ledger to blank printable sheet
- Phase 3 cleanup: resolve PAGES duplication, consider build-time sidebar
