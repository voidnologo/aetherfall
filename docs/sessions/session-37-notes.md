# Session 37: Wave 4 Art, Stories 01 and 04, and the Deco Fiction Reader

**Date:** 2026-09-30 to 2026-10-01 (overnight)
**Goal:** Settle the corner ornaments (keep both), clear the content backlog, and bring the fiction reader up to the rulebook's art and typography. Then, overnight and unattended (the user was asleep): queue Wave 4 art in blocks with cool-down breaks, publish a selector page, write the next story, and push towards sellable art, layout, lore and hooks.

## Overview

A long session in three parts. **Evening:** corners kept on both callouts and stat blocks; the fiction reader gained the rulebook's Deco ornaments and justified prose; four pending canon decisions were settled (renames, Quick Reload rounds up); the stranded Story 03 bible update reached main. **Overnight, unattended:** 111 Wave 4 renders ran in blocks of 12 with 8-minute GPU rests; a click-to-pick selector page was built and published; Story 04 ("No Kinder Country") was written from its plan, and Story 01 ("The Ashwick Job", the Quickstart as fiction, with a Play This Story link) was written from scratch. Both stories are on open PRs for review. **Morning:** the user picked two rounds of art (19 + 17) and asked for placement. 22 plates and scenes went into 14 chapters, with portraits for Laine and a new "Faces of Ashwick" cast on the fiction index. The PDF gained a full-bleed cover and prints the plates at about 300 DPI.

---

## Changes Made

### Fiction reader: Deco ornaments, PR #22
- Each story has a rulebook `theme` and a card `spot` in `web/_data/fiction.js` (Story 02 aether + `wild`; Story 03 split + `tunnels`).
- Title pages show the theme crown with the number and title typeset inside it. Chapter openings use the drop-cap tile, scene breaks use the theme divider, and a tailpiece closes each story.
- On the index, the header gets a Deco divider, and story cards get corner ornaments and a round spot.
- Prose is justified with hyphenation. Plan §7 records the reader standard.

### Content decisions, PR #23 (CANON_DECISIONS §8–9)
- Gideon Marlow (was Aldric Voss), Elara Pryce (was Elara Voss), Hollowmere (was Thornfeld). Fels now smokes clove cigarettes; Dace keeps the thin cigar.
- Quick Reload rounds up.

### Series bible, PR #24
- Story 03 outcomes folded in from e379a60, with conflicts resolved against main.

### Overnight (unattended)

**Wave 4 art, PR #27 (merged): tooling only, nothing placed**
- 36 pieces in `tools/deco_suite.py`: 12 full-page plates, 10 half-page scenes, 3 cover candidates, 7 NPC portraits, 4 Story 04 spots (111 renders: 3 seeds each, 4 for covers). `PLATE_STYLE` / `PORTRAIT_STYLE` are full-bleed and lamp-free.
- `tools/render_blocks.py` rendered them in 10 blocks of 12 with an 8-minute GPU rest between blocks (about 85 s per image in performance mode; the GPU peaked at about 75 °C and cooled to about 50 °C in the rests). Run detached with `setsid nohup`.
- `tools/wave_page.py` builds the selector page: https://claude.ai/artifact/E47GCrji4ykVKy3TyJWm4z (first publish: plates and scenes).
- `{% plate %}` shortcode and plate CSS for web and print (a full plate gets its own midnight page in the PDF).

**Story 04 "No Kinder Country", PR #25 (open, for review)**
- Eight chapters from the plan, 24.9k words (long: over the 15k guide). Galvanic theme, `misfire` card spot for now. Continuity fixes against the plan are listed in the PR. Series bible: Story 4 entry, new NPCs, "After Story 04" tracker.

**Story 01 "The Ashwick Job", PR #26 (open, for review)**
- The site had only 02 and 03 because Story 01 existed only as the Quickstart module. Written as fiction: plan plus six chapters, 11.8k words. Its ending has a **Play This Story** button to the Quickstart; the fiction index says "New to Ashwick? Start with Story No. 01". Neutral theme, `foundry` spot.
- PRs #25 and #26 both touch `fiction.js` and the series bible; whichever merges second needs a small conflict fix.

---

### Morning: picks and placement (user present)

- Round 1 picks: 1c 2b 3b 4c 5a 7b 8a 9a 10c 11a 12c 13a 14c 15c 16b 17b 18a 19b 20c, plus a reroll of the market fight (v02 puts the cyan shield at the centre). PR #28.
- Round 2 (same selector URL): 1a 2b 3c 4d 5d 6d 7a 8a 9c 10c 11b 12b 13b 14a 15b 16c 17b. Everything approved; rejected candidates archived.
- **Placed, PR #29:** 22 plates and scenes across 14 chapters; Laine's portrait on her Quickstart stat block; three Story 04 spots (stretcher, dampener, ward); the "Faces of Ashwick" cast of seven portraits on the fiction index (`web/_data/cast.json`); the Story 04 card spot is now `ford` (on PR #25).
- `tools/plate_manifest.json` + `tools/plate_web.py` rebuild every full-bleed web copy from its approved master, recording paint-outs (Wet Ember plaque, Laine's call box, Hesper's crate and label), crops (foundry signature, Crane's signature) and automatic bone-border trims.
- **PDF:** a full-bleed cover ("Between two cities"); plates, covers and portraits print from 4x masters downsampled to about 300 DPI. 235 pages, 44.7 MB. It now includes the renames and the Quick Reload change.
- Memory saved: art picks always go through a click-to-pick selector page (`art-selector-pages`).

## Files Modified

| File | Change |
|------|--------|
| `web/_data/fiction.js`, `web/fiction/*.njk`, `web/fiction/css/fiction.css` | Deco reader |
| `docs/art/deco-suite-plan.md` | Corner decision; §7 fiction reader |
| `docs/requirements/CANON_DECISIONS.md` | §8 renames, §9 Quick Reload |
| `web/rules/skills.njk`, `equipment.njk`, `web/_data/characters/sample.json` | Hollowmere, round up, Elara Pryce |
| `fiction/world/02-the-local-scene.md`, `docs/requirements/WORLD_DESIGN.md` | Gideon Marlow |
| `fiction/stories/story-03/{ch01,ch07,PLAN}.md` | Fels's clove cigarettes |
| `fiction/world/06-series-bible.md` | Story 03 outcomes; Story 01 and 04 entries (on their PRs) |
| `tools/deco_suite.py`, `tools/render_blocks.py`, `tools/wave_page.py` | Wave 4 prompts, block renderer, selector page |
| `eleventy.config.js`, `web/rules/css/styles.css`, `print.css` | Plate shortcode and styles |
| `fiction/stories/story-01/`, `story-04/`, `web/fiction/*` | New stories and reader pages (on PRs #25, #26) |

## Key Design Decisions

- Corners on both callouts and stat blocks (user).
- Plates are never cut out; every web copy is rebuilt from its approved master through `tools/plate_manifest.json`, so paint-outs and crops are reproducible.
- Full plates sit before a chapter's first section (after the flavour paragraph, so the drop cap survives); scenes sit at a mid-chapter heading. At most one full plate per chapter (the Quickstart has two, one per act).
- Fiction NPCs get portraits on the fiction index rather than in the rulebook, because only Laine appears in the rules.
- Story 01 exists to be the front door: read the story, then play the same night from the Quickstart.
- Stories written unattended stay on open PRs for the user's review; art tooling and placements were self-merged.
- Fiction stories carry a rulebook theme. Story 03 is `split`: the Aether at work under a Galvanic foundry.

## Open Issues

- PR #3 (Story 04 plan, draft) is stale. Its bible commit is now on main; the plan needs rebasing or carrying over once reviewed.
- Overnight, Claude Code stopped a background log-watcher because memory was low (ComfyUI holds about 19.8 GB). The detached renderer kept going.
- The SSH agent stopped signing overnight ("communication with agent failed"), so pushes went over HTTPS with the `gh` token as a one-off credential helper (no config changed). It may need unlocking or a restart.
- Hesper's portrait shows two arms (canon: one). Her cast line avoids it; reroll when convenient.
- The two other cover picks ("four on the hill road", "the Tear over the skyline") are approved but unused: candidates for the web hero redraw and og:image.

## Next Session

1. Review PRs #25 (Story 04) and #26 (Story 01); merge (the second needs a small conflict fix in `fiction.js` and the bible), then publish.
2. Use the spare covers for the web hero redraw and social preview (og:image) images.
3. Optional rerolls: Hesper with one arm.
