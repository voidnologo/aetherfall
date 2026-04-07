# Session 18: Quick Reference Redesign, Exhaustion Tier Rename, Title & Repo Rename

**Date:** 2026-04-06
**Goal:** Polish the Quick Reference page, add combat and spellcasting flowcharts, rename exhaustion tiers, choose a real game title, and rename the repo.

## Overview

Major polish and identity session. Redesigned the Quick Reference chapter from a dense monospace `<pre>` block into a card-grid layout with proper tables, formula highlights, and Mermaid flowcharts for both spellcasting and combat procedures. Renamed the exhaustion track tiers from Weakened/Severely Weak/Incapacitated to Wearied/Drained/Overwhelmed across the entire project. Chose "Aetherfall" as the game's official title (replacing the working title "Adventure"), renamed every reference across all 30+ files, renamed the GitHub repo, and added a comprehensive README with a design doc reading guide.

---

## Changes Made

### Quick Reference Redesign (`web/rules/reference.html`)
- Replaced single `<pre>` block with a card-grid layout (2-column responsive)
- Each rules area gets its own card: Core Mechanics, Damage & Recovery, Spellcasting, Combat
- Proper HTML tables for wound/exhaustion tiers, range bands, backlash percentages, malfunction severity
- Formula highlights in JetBrains Mono inline boxes
- Mermaid.js flowcharts for spellcasting and combat procedures
- Color-coded nodes: teal for start/spell links, green for completion, red for failures, amber for warnings
- TOC anchors for each section and flowchart

### Exhaustion Tier Rename (9 files)
- **Weakened** → **Wearied** (-10%)
- **Severely Weak / Sev. Weak** → **Drained** (-25%)
- **Incapacitated** → **Overwhelmed** (-50%) (exhaustion track only; wound track keeps Incapacitated)
- Updated in: getting-hurt.html, reference.html, character-sheet.html, character-sheet-sample.html, character-builder.html, BASE_MECHANICS.md, MAGIC_SYSTEM.md, PROJECT_SPEC.md, COMBAT_PROCEDURE.md

### Game Title: Adventure → Aetherfall (30+ files)
- All `<title>` tags: "Chapter — Aetherfall RPG"
- All header logos: "Aetherfall RPG"
- All sidebar titles: "Aetherfall"
- All footers: "Aetherfall RPG — Playtest Draft"
- Character sheet headers (blank, sample, builder print output)
- Landing page hero title
- Design docs (PROJECT_SPEC, WRITING_STYLE, WORLD_DESIGN_PLAN)
- Sidebar "Back to Aetherfall" links
- CSS comment header
- Preserved: "Adventurer", "Adventuring Societies", "Adventure Hooks" (English words)

### GitHub Repo Rename
- Renamed from `voidnologo/Adventure` to `voidnologo/aetherfall`
- Updated local git remote URL

### README (`README.md`)
- Project overview with status and live site link
- Annotated directory tree
- Tech stack description (no-build static HTML)
- Design doc reading guide — numbered reading order for all 11 design docs with descriptions
- Systems-at-a-glance table
- Interactive tools descriptions
- Development log and balance testing sections

---

## Files Modified

| File | Change |
|------|--------|
| web/rules/reference.html | Complete redesign — card grid, tables, Mermaid flowcharts |
| web/rules/getting-hurt.html | Exhaustion tiers renamed + title/logo/footer to Aetherfall |
| web/rules/tools/character-sheet.html | Exhaustion tiers + title rename |
| web/rules/tools/character-sheet-sample.html | Exhaustion tiers + title rename |
| web/rules/tools/character-builder.html | Exhaustion tiers in print output + title rename |
| docs/requirements/BASE_MECHANICS.md | Exhaustion tiers renamed |
| docs/requirements/MAGIC_SYSTEM.md | Exhaustion tiers renamed |
| docs/requirements/PROJECT_SPEC.md | Exhaustion tiers + title rename |
| docs/requirements/COMBAT_PROCEDURE.md | Exhaustion tiers renamed |
| docs/requirements/WRITING_STYLE.md | Title rename |
| docs/requirements/WORLD_DESIGN_PLAN.md | Title rename |
| web/index.html | Title/hero rename to Aetherfall |
| web/rules/index.html | Title/logo/sidebar/footer rename |
| web/rules/state-of-the-world.html | Title/logo/sidebar/footer rename |
| web/rules/societies.html | Title/logo/sidebar/footer rename |
| web/rules/creating.html | Title/logo/sidebar/footer rename |
| web/rules/character-sheet.html | Title/logo/sidebar/footer rename |
| web/rules/rolling.html | Title/logo/sidebar/footer rename |
| web/rules/skills.html | Title/logo/sidebar/footer rename |
| web/rules/magic.html | Title/logo/sidebar/footer rename |
| web/rules/grimoire.html | Title/logo/sidebar/footer rename |
| web/rules/world-between.html | Title/logo/sidebar/footer rename |
| web/rules/combat.html | Title/logo/sidebar/footer rename |
| web/rules/equipment.html | Title/logo/sidebar/footer rename |
| web/rules/running-the-game.html | Title/logo/sidebar/footer rename |
| web/rules/tables.html | Title/logo/sidebar/footer rename |
| web/rules/gm-tools.html | Title/logo/sidebar/footer rename |
| web/rules/css/styles.css | CSS comment header rename |
| web/rules/tools/zone-tracker.html | Title rename |
| web/rules/tools/combat-tracker.html | Title rename |
| README.md | NEW — project overview, design doc guide, systems reference |

## Key Design Decisions

- **Wearied/Drained/Overwhelmed over Dazed/Stunned/Incapacitated.** "Dazed" and "Stunned" sound like sudden impact conditions (getting punched), not building exhaustion. "Strained" was rejected because it rhymes with "Drained" — confusing at the table. "Wearied" conveys the first stage of fatigue without rhyming. "Overwhelmed" distinguishes the exhaustion final tier from the wound track's "Incapacitated."
- **Aetherfall as the title.** Single word, memorable, implies a world-defining event ("what fell?"), captures the Aetheric theme. Chosen over "Smoke & Aether" (great but two words), "The Aetheric Age" (harder to say casually), and "Gaslight & Grimoire" (too gothic).
- **Card-grid over the old pre block for Quick Reference.** The monospace dump was dense and hard to scan. Cards with headers let you find the section you need visually. Tables render structured data (tiers, ranges, backlash %) much better than aligned text.
- **Mermaid flowcharts with short labels.** Initial version had multi-line descriptive text that got clipped in nodes. Shortened to essential keywords — the surrounding reference cards have the detail.

## Open Issues

- Flowchart node sizing still depends on viewport/font rendering — may need further tuning on different screens
- Mermaid loads from CDN — flowcharts won't render offline (rest of the site works offline)
- Landing page at web/index.html still says "A 1920s Steampunk RPG" — may want to refine the tagline to match the Aetherfall identity
- Character sheet art/watermarks still pending

## Next Session
- Visual polish and art for character sheets
- Flowchart refinement based on feedback
- Any playtest feedback iteration
