# Session 28: HTML Entity Cleanup, Payout Clarity, README Overhaul

**Date:** 2026-04-14
**Goal:** Fix escaped HTML entities in chapter subtitles, clarify Scraps vs Honest Work distinction, update README for current project structure

## Overview

Continued from session 27 (same day, new conversation). Found and fixed HTML entities (`&mdash;`, `&amp;`) rendering as literal text in YAML frontmatter subtitles across 8 chapter files — same root cause as the `&rsquo;` fix in session 27. Clarified the payout table in the GM chapter so readers can see the Drift relationship at a glance (Scraps don't prevent Drift, Honest Work does). Rewrote the README to reflect the Eleventy build system, accurate chapter count (18 + quickstart), all 15 design docs, and current project structure.

---

## Changes Made

### HTML Entity Cleanup — Chapter Subtitles
- 7 files had `&mdash;` in frontmatter subtitles — replaced with literal em dash (`—`)
- 1 file had `&amp;` in frontmatter subtitle — replaced with literal `&`
- Same class of bug as session 27's `&rsquo;` fix: HTML entities in YAML frontmatter are not processed as HTML, so they render as literal text in page titles and headings

### Payout Table Clarification
- Changed Scraps ledger effect from "No change" to "No effect — Drift still applies"
- Changed Honest Work ledger effect from "Holds Level" to "Holds Level — prevents Drift"
- Without this, the two tiers read as functionally identical to anyone who hasn't memorized the Drift section above the table

### README Overhaul
- **Tech Stack:** Replaced "No build step, no dependencies, no framework" with Eleventy 3.x description, build/dev commands, deploy pipeline, template shortcodes
- **Project Structure:** Added `eleventy.config.js`, `_includes/`, `_data/`, `_site/`, art pipeline directories; updated chapter count from 16 to 18 + quickstart
- **Design Documents:** Added ECONOMY.md, MAGICAL_ARTIFACTS.md, STARTER_ADVENTURE.md, ART_DIRECTION.md (previously missing from reading order); expanded from 11 to 15 entries
- **Game Systems table:** Added Economy row (Ledger + Drift)
- **Tools:** Removed stale `character-sheet-sample.html` reference

---

## Files Modified

| File | Change |
|------|--------|
| `web/rules/grimoire.njk` | `&mdash;` → `—` in subtitle |
| `web/rules/skills.njk` | `&mdash;` → `—` in subtitle |
| `web/rules/artifacts.njk` | `&mdash;` → `—` in subtitle |
| `web/rules/rolling.njk` | `&mdash;` → `—` in subtitle |
| `web/rules/magic.njk` | `&mdash;` → `—` in subtitle |
| `web/rules/index.njk` | `&amp;` → `&` in subtitle |
| `web/rules/getting-hurt.njk` | `&mdash;` → `—` in subtitle |
| `web/rules/world-between.njk` | `&mdash;` → `—` in subtitle |
| `web/rules/running-the-game.njk` | Scraps/Honest Work ledger effect wording |
| `README.md` | Full rewrite for Eleventy, accurate structure and doc list |

## Key Design Decisions

- **Drift visibility in payout table:** The Drift mechanic was explained in its own section just above the payout table, but the table itself didn't reference it. Readers seeing "No change" vs "Holds Level" had no way to distinguish the two without prior context. Making Drift explicit in both rows tells the full story at a glance.

## Open Issues

- Character sheet content still flows over/under watermark bottom decorations
- Embossed "A" design still pending revisit
- Character sheet art/watermarks could use further iteration

## Next Session
