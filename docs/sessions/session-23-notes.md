# Session 23: Economy & Resource System Design

**Date:** 2026-04-13
**Goal:** Design a narrative-first economy system — marks as currency, wealth tiers for story-driving resource access, patron support scales. No checkbook balancing, no exhaustive price lists.

## Overview

Researched 10 RPG economy systems (Blades in the Dark, Shadowrun, Mothership, Savage Worlds, Fate, PbtA/Dungeon World, Stars Without Number, Band of Blades, Trophy, Cypher System/Numenera) and designed a complete economy system for Aetherfall. The system uses three core mechanics — Station (individual wealth tier 0–5), the Ledger (Society resource state: Flush/Level/Lean/Dire), Backing (patron support 1–5), Cost Tiers for equipment, and the Drift for between-job pressure — to create story-driving resource access without any transaction tracking.

Built the full design doc with research notes, then implemented the economy as a new web rulebook chapter ("Coin & Commerce," Chapter 12), added Cost Tier columns to all weapon and armor tables, renumbered all subsequent chapters, and added economy tables to the Table Index. Also centralized all chapter numbers and prev/next navigation into the PAGES registry in main.js — inserting or reordering chapters now requires updating one array instead of touching every HTML file.

---

## Changes Made

### Economy Design Document
- **Full design doc:** `docs/requirements/ECONOMY.md` — 14 sections covering research, principles, and the complete system
- **Research section:** 10 RPG systems surveyed with analysis of what we borrowed, rejected, and why
- **8 design principles:** Access not Balance, Story Fuel not Simulation, One Number Per Layer, Shape not Precision, GM Controls Pace, Marks Are Flavor, Patron Relationships Are Economic, Reaching Creates Adventure
- **Core system:** Station (0–5), Ledger (Flush/Level/Lean/Dire), Backing (1–5), Cost Tiers (0–5), Payout Ratings, the Drift
- **Equipment integration:** Cost Tier assignments for all existing weapon, armor, and gear categories
- **Special items:** Artifact narrative valuation, Potion Cost Tiers
- **Voice callouts:** In-world experiences from Handler, Scholar, Street, Believer — no rules commentary

### Web Rulebook — New Economy Chapter
- **New chapter:** `web/rules/economy.html` — "Coin & Commerce" (Chapter 12, neutral theme)
- Sections: Marks, Station, Cost Tiers, Access Rule, Station Checks, Reaching Beyond Means, Society Ledger, Patron Backing, Faction-Specific Gear, Owned vs Issued Gear, the Drift, Downtime Actions, Artifacts, Potions
- Voice callouts from all four perspectives, At the Table example (Sera at the tailor), For the GM guidance callouts

### Equipment Table Updates
- Added Cost Tier column to melee weapons, ranged weapons (martial), modern firearms, medieval armor, and modern armor tables
- Tier values assigned per ECONOMY.md §11.1

### Chapter Renumbering
- Economy inserted as Chapter 12
- Equipment → 13, Artifacts → 14, Running the Game → 15, Quick Reference → 16, Table Index → 17, GM Tools → 18
- PAGES registry in main.js updated

### Centralized Navigation (Refactor)
- Added `initPageChrome()` function to main.js — generates header-chapter text, page-number, compact nav (top), and full nav (bottom) from the PAGES registry
- Stripped hardcoded chapter numbers and nav links from all 20 HTML files
- Inserting or reordering chapters now requires updating one array

### Table Index
- Added Economy & Resources section with 10 new table entries linking to economy.html

### Design Doc Fixes
- Removed enchanted firearms open question (violates Aetheric/Galvanic split)
- Confirmed starting equipment guideline: pick gear within your Station
- Noted For the GM and At the Table callout types alongside voice callouts

---

## Files Modified

| File | Change |
|------|--------|
| `docs/requirements/ECONOMY.md` | New — full economy design document with research, principles, system |
| `docs/pending-tasks.md` | Economy/artifact pricing resolved, 5 new follow-up tasks added |
| `web/rules/economy.html` | New — Coin & Commerce chapter (Chapter 12) |
| `web/rules/js/main.js` | Economy in PAGES registry, `initPageChrome()` for dynamic chapter/nav |
| `web/rules/equipment.html` | Cost Tier column added to all weapon/armor tables, chapter 13, nav stripped |
| `web/rules/combat.html` | Nav stripped (now JS-driven) |
| `web/rules/artifacts.html` | Chapter 14, nav stripped |
| `web/rules/running-the-game.html` | Chapter 15, nav stripped |
| `web/rules/reference.html` | Chapter 16, nav stripped |
| `web/rules/tables.html` | Chapter 17, economy tables added, nav stripped |
| `web/rules/gm-tools.html` | Chapter 18, nav stripped |
| `web/rules/index.html` | Nav stripped |
| `web/rules/state-of-the-world.html` | Nav stripped |
| `web/rules/societies.html` | Nav stripped |
| `web/rules/creating.html` | Nav stripped |
| `web/rules/character-sheet.html` | Nav stripped |
| `web/rules/rolling.html` | Nav stripped |
| `web/rules/getting-hurt.html` | Nav stripped |
| `web/rules/skills.html` | Nav stripped |
| `web/rules/magic.html` | Nav stripped |
| `web/rules/grimoire.html` | Nav stripped |
| `web/rules/world-between.html` | Nav stripped |
| `web/rules/quickstart.html` | Nav stripped |

## Key Design Decisions

1. **Station, not bank balance** — Wealth is a tier (0–5) determining access, not a number to subtract from. Inspired by Shadowrun lifestyles, simplified further.
2. **The Ledger is qualitative, not quantitative** — Four states instead of a numerical pool. Inspired by Mothership Debt, abstracted to remove math.
3. **Marks are flavor** — In-world NPCs talk in marks, but players never track a balance. Station handles mechanics.
4. **Backing formalizes patron generosity** — 1–5 scale with faction-specific gear provisions. Makes patron support concrete and variable.
5. **Station Checks use existing skills** — Etiquette, Streetwise, Persuasion, Deception depending on context. No new mechanics.
6. **No enchanted firearms** — Violates the core Aetheric/Galvanic split. Edge-case adventure content only.
7. **Economy gets its own chapter** — Before Equipment, so Cost Tiers are a known quantity when readers see them on weapon tables.
8. **PAGES registry drives all chapter chrome** — Single source of truth for chapter numbers, titles, and navigation. No more hardcoded values in HTML.

## Open Issues

- Station Check frequency needs playtesting — the -15% modifier may need tuning
- Zone-specific economy adjustments (cheaper in home districts?) — interesting but may add complexity
- Economy sections for Societies, Equipment, and GM chapters need cross-reference callouts
- Station and Backing/Ledger fields need adding to character sheet builder
- User wants to discuss whether the site is complex enough to warrant a web framework + build step

## Next Session

- Discuss web framework / build system for the rulebook site
- Review economy chapter in browser
- Add Station to character sheet builder
- Cross-reference economy in Societies and GM chapters
