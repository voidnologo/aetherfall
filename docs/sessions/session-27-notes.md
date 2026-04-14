# Session 27: Character Sheet Fixes, Production Bug Fixes, Lore Rename

**Date:** 2026-04-14
**Goal:** Continue character sheet polish from session 26, fix production bugs, rename founding event

## Overview

Picked up where session 26 left off (mid-session on a different account). Verified the character builder → sheet flow works with the localStorage fix from the previous session. Fixed broken image links on the production site caused by absolute asset paths that didn't account for the `/aetherfall/` path prefix on GitHub Pages. Fixed the magic path checkbox bug where "Wild" and "Non-caster" both showed as checked. Removed the hardcoded spell count from the grimoire. Fixed an HTML entity bleeding through in a frontmatter subtitle. Renamed the founding cataclysm from "the Eruption" to "the Tear" across the entire project — 15 files, ~80 replacements — including a reworked Believer voice callout.

---

## Changes Made

### Production Bug Fix — Broken Asset Paths
- All asset paths in `chapter.njk` and `sheet.njk` used absolute `/assets/...` which 404'd on GitHub Pages at `/aetherfall/`
- Applied Eleventy's `| url` filter to all asset `src`/`href` attributes in both templates
- Added `--pathprefix=/aetherfall/` to the GitHub Actions deploy workflow
- Local dev unaffected (pathPrefix defaults to `/`)

### Character Sheet Fixes
- Magic path checkboxes: JS now clears all checkbox states before marking the selected one (fixes Wild + Non-caster both checked)
- Removed hardcoded "38 spells" from grimoire intro — now says "all spells"

### Subtitle Fix
- `state-of-the-world.njk` frontmatter had `&rsquo;` which rendered as literal text (not in HTML context). Replaced with plain apostrophe.

### Lore Rename: "Eruption" → "Tear"
- Renamed the founding cataclysm across all rulebook chapters, design docs, art guides, character data, and README
- Reworked Believer voice callout: "They call it the Tear. As if something *broke*..." with fabric/mending metaphor
- Session notes left as historical record (still say "Eruption")

---

## Files Modified

| File | Change |
|------|--------|
| `.github/workflows/pages.yml` | Added `--pathprefix=/aetherfall/` to build command |
| `web/_includes/chapter.njk` | Asset paths use `\| url` filter |
| `web/_includes/sheet.njk` | Asset paths use `\| url` filter; checkbox clear-before-mark fix |
| `web/rules/grimoire.njk` | Removed hardcoded "38" spell count |
| `web/rules/state-of-the-world.njk` | Subtitle fix; Eruption → Tear (13 instances + voice callout) |
| `web/rules/artifacts.njk` | Eruption → Tear (6 instances, Pre-Tear section) |
| `web/rules/economy.njk` | Eruption → Tear (5 instances) |
| `web/rules/societies.njk` | Eruption → Tear (1 instance) |
| `web/rules/world-between.njk` | Eruption → Tear (1 instance) |
| `web/_data/characters/sera.json` | Eruption → Tear in description and notes |
| `docs/requirements/WORLD_DESIGN.md` | Eruption → Tear (30 instances + voice callout) |
| `docs/requirements/MAGICAL_ARTIFACTS.md` | Eruption → Tear (9 instances) |
| `docs/requirements/ECONOMY.md` | Eruption → Tear (5 instances) |
| `docs/requirements/DESIGN_PHILOSOPHY.md` | Eruption → Tear (3 instances) |
| `docs/requirements/WORLD_DESIGN_PLAN.md` | Eruption → Tear (3 instances) |
| `docs/requirements/WRITING_STYLE.md` | Eruption → Tear (1 instance) |
| `docs/art/style-guide.md` | Eruption → Tear (2 instances) |
| `docs/art/prompt-engineering/prompt-templates.md` | Eruption → Tear (1 instance) |
| `README.md` | Eruption → Tear (2 instances) |

## Key Design Decisions

- **"The Tear" over alternatives** (Sundering, Breach, Rending): "Tear" is the most natural extension of existing Veil language and simple enough for common speech. "Before the Tear" has the same rhythm as the old name.
- **Voice callout rework**: The Believer's pushback now uses a fabric/mending metaphor — "As if something broke... something to be mended" — which plays against the Tear naming naturally.
- **pathPrefix over relative paths**: Eleventy's `| url` filter + `--pathprefix` flag is the proper solution for GitHub Pages subdirectory deployment, keeping local dev at `/` and production at `/aetherfall/`.
- **"no calamity" in economy voice callout**: The Believer wouldn't say "no Tear can take it from you" — rephrased to "no calamity" which is more natural in-character.

## Open Issues

- Character sheet content still flows over/under watermark bottom decorations
- Embossed "A" design still pending revisit
- Character sheet art/watermarks could use further iteration

## Next Session
