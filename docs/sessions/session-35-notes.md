# Session 35: The Deco Art Suite — Portraits, Ornaments, Spots, and Print

**Date:** 2026-09-26 to 2026-09-28
**Goal:** Pick up from the continuation prompt: lead portraits in the quickstart pregens and character sheets, review crowns/openers/watermark, plan the next Deco art suite. Work lands as squash-merged PRs (one per discrete chunk) instead of direct commits to `main`.

## Overview

A long art session that took the Deco Lithograph direction from four approved portraits and four frames to a complete, consistent art suite across the web rulebook and the print PDF. The lead portraits went onto the quickstart and the pregen sheets. The chapter crowns were rebuilt with alpha so their ornaments aren't cropped flat. A Deco suite plan was written and approved. Three waves then produced 3 dividers, 3 drop-cap tiles, a tailpiece, 2 corner ornaments, 6 school emblems, 3 zone badges and 34 spot illustrations, all chosen by the user from comparison pages. The user asked for consistency, so an explicit chapter art standard now puts a crown, drop cap, dividers (via a build transform), 1–3 spots, corners and a tailpiece in every chapter, and the PDF carries the same set.

Supporting work: all approved art was upscaled 4× for print, the PDF uses ~370 DPI frames, and a PDF build that had been broken since the portrait PR was found and fixed. Work landed as 13 self-merged PRs (#4–#6, #8–#17), replacing direct pushes to `main`. User feedback shaped the art along the way: whole ornaments with no flat crops, no lamp in every picture, more varied scenes, and one consistent standard.

---

## Changes Made

### Lead portraits — PR #4
- Quickstart pregen stat blocks get a portrait column (a banner on phones ≤500px).
- Sheet page 2: the Notes box is split into note lines plus a framed portrait panel. The blank sheet shows an empty "Portrait" sketch box.
- `portrait` field on the pregen JSONs; web copies in `web/assets/art/portraits/`.
- Mira reference image: 2096254533 (user's choice); 4036712205 stays approved as an alternate.

### Chapter crowns with alpha — PR #5
- The user saw the web crowns as cut off: the old crowns were a rectangular crop inside the frames' faint bone margin, which flattened the ivy, the aether apex, and the compass point.
- `tools/crown_alpha.py` clears the bone margin to alpha (edge flood in a 48 px band) instead of cropping, so the ornaments keep their full shape. CSS keeps each crown's own aspect ratio.
- A Flux outpaint attempt failed (it painted new scenery around the bordered frame). That image is archived; the other seeds were cancelled.

### Deco suite plan — PR #6
- `docs/art/deco-suite-plan.md`: ornament kit (dividers, drop-cap tiles, corners, tailpiece, school sigils, zone badges), ~24 spots per chapter, pipeline changes (`tools/deco_suite.py`, `tools/cutout.py`, spot shortcode), four waves.
- User decisions: Wave 1 = kit + two spots (The Tear; revolver misfire); vignettes skipped for now; drop caps = art tile + typeset letter; spot list approved.

### Deco suite Wave 1 — ornaments shipped (PR #8), spots in round 2
- `tools/deco_suite.py` (queue/collect, isolated-on-bone prompts) and `tools/cutout.py` (edge flood keying of bone to alpha, fringe removal, stray-mark/signature removal).
- 27 renders (9 pieces × 3 seeds) in `art/decorative/generated/` and `art/spots/generated/`. Comparison page: https://claude.ai/artifact/DzMSi3MowVHYAvorNbuzTG
- Findings: the ornaments work. The Engine dividers drift into teal (palette breach). Both spots are weak (rectangular fills; the Tear came out amber, not cyan), so a reroll is recommended. Navy ink nearly vanishes on the dark web background.
- User picks: 1c 2a 3b 4b 5b 6c 7c approved and wired into every chapter by theme (dividers, drop cap on the opening paragraph, tailpiece). Neutral divider recoloured navy → bone for the web only (user approved).
- Spots re-rendered as v02 (4 seeds each; the Tear as a round vignette, the misfire down an empty alley). Round 2 is on the same comparison page. Fallbacks: 8c (Tear v01), 9a (misfire v01).
- Hiccups: the auto-mode safety check went down mid-session (the user ran a helper script with `!`); an SSH agent signing failure blocked one push, which a retry cleared. PR #7 (landing page mobile fix, from another session) landed on main in between; the branch was rebased cleanly.

### Deco Wave 1 spots — PR #9
- User picks: Tear 8a or 8d (8a used, 8d approved alternate), misfire 9c. New `{% spot %}` shortcode; the Tear sits in Ch 02 beside "The Tear", the misfire in Ch 11 beside "The Malfunction System".
- `cutout.py` gained `--hull` (round vignettes stay whole) and `--light-to-cyan` (the Tear's bone-white crack shifted to Aether cyan).
- **Wave 1 is complete.**

### Deco Wave 2 (awaiting picks) + print upscale (PR #10)
- Wave 2 defined in `tools/deco_suite.py`: 13 spots (chapters 01–11) and six school sigils (one medallion frame, one symbol per school); 57 renders queued. Spot prompts now ask for a round vignette by default.
- Print upscale: `tools/upscale_print.py` queues every approved PNG (except the transparent wordmark) through ComfyUI's RealESRGAN_x4plus_anime_6B into `art/{type}/print/{stem}_x4.png` (gitignored; masters untouched). It is queued behind Wave 2, because a separate GPU process would not fit next to Flux (11.1 of 12.2 GB VRAM in use).
- The web frame crop was recovered by image matching: each master trimmed to 782×1168 at (24–26, 24), i.e. ~25 px per side. `scripts/build-pdf.py` now cuts 4× print frames (3128×4672, ~370 DPI on letter) from the print masters and overrides the opener and front-matter page backgrounds, falling back to the web copies. It also rewrites `../assets/` image paths so spots print.
- Wave 2 comparison page: https://claude.ai/artifact/LMoRK39oGSYeVmuR2jLXEa. Flags: dice came out six-sided with pips (Flux ignored d10); the street-between spots miss the Aether half (reroll recommended); some sigils stray into amber and oxblood.
- Print: all 24 upscales done. The PDF build had been broken since PR #4: the pregen portrait's print grid crashed WeasyPrint (`assert not page_is_empty`), found by bisecting variants. A float didn't work either, so the portrait is now absolutely positioned. The PDF builds again (191 pages, 15.2 MB) with ~370 DPI openers and front matter, and the spots and portraits print.

### Deco Wave 2 shipped (PR #11)
- Picks: 1b 2c 3a 4c 6c 7b 8a 9b 10c 11a (+11c alt) 13a; emblems 14a 15c 16c 17c 18b 19a. 12a approved as a fallback; dice (5) and street (12) re-rendering as v02.
- **User feedback: a lamp in every spot.** The lamps came from my subject prompts plus the D2 prefix's light/lamp language. `SPOT_STYLE` now has its own lamp-free prefix and varied light. The approved Wave 2 spots still have lamps; the user approved them regardless.
- Skills spots use a new centred `{% spot %}` variant (a full-width table follows each heading). School emblems are CSS-only on the Grimoire headings and the Ch 08 list.

### Dice + chapter art standard (PRs #12, #13); Wave 3 rendering
- PR #12: dice 5b placed (six-sided dice are fine, per the user). The user liked none of street v02, so 12z is in as a stand-in; street v03 (no buildings on the Aether side) and a balance-scale alternative are queued.
- The user asked for consistency across the whole book. Audit: dividers on only 3 of 20 pages, spots 0–3 per chapter, no corners. The standard is recorded in the plan (§5). PR #13 adds a build transform that inserts dividers between top-level sections in every chapter, plus a lead portrait row on the Character Sheet page.
- Wave 3 (reworked with the user; variety rule, no lamp focus): 18 spots bring every chapter up to the standard, plus corners (to try on both stat blocks and callouts) and zone badges. 69 renders queued.
- Memory saved: no lamp focus; power profile quiet mode slows renders.

### World Between final + Wave 3 (PRs #14, #15)
- PR #14: street v03 12b (12a alternate) and balance scale 13c in Ch 10.
- PR #15: 17 Wave 3 spots bring every chapter up to the standard (1–3 each). Corner ornaments (Nouveau in Aether chapters, Deco elsewhere) go on every callout and stat block; pregen cards keep only the top-right corner. Zone badges on the quickstart location labels. Very few lamps in Wave 3, per the variety rule.
- The catalogue plate (7) was re-rendered (v02); the user picked 7c. It's centred above the Melee Weapons table (PR #16). **Wave 3 complete; every chapter meets the art standard.**

### PDF ornaments (PR #17)
- The PDF now carries the full ornament set by chapter theme. The print drop cap is a raised initial (WeasyPrint doesn't wrap text around a floated `::first-letter`), and print keeps the navy neutral divider. Corners shrank to fit inside the padding on web and print (the bottom-left corner had crowded callout text). The Grimoire emblem bug (`background` shorthand beating the id-suffix rules) was fixed.
- Print upscale re-run: 70 masters in `art/*/print/`.

---

## Files Modified

| File | Change |
|------|--------|
| `web/rules/quickstart.njk` | Pregen portraits; foundry and tunnels spots |
| `web/rules/*.njk` (17 chapters) | `{% spot %}` placements; Character Sheet lead-portrait row |
| `web/_includes/sheet.njk` | Portrait panel in the page-2 Notes box |
| `web/_includes/chapter.njk` | Tailpiece before the chapter nav |
| `web/_data/characters/{kael,sera,aldric,mira}.json` | `portrait` field |
| `web/rules/css/styles.css` | Crown aspect ratios; dividers, drop cap, tailpiece, spots (float and centre), corners, school emblems, zone badges, portrait card and row |
| `web/rules/css/print.css` | Print versions of all of the above; absolutely positioned pregen portraits (WeasyPrint fix) |
| `eleventy.config.js` | `spot` shortcode; `section-dividers` transform |
| `scripts/build-pdf.py` | 4× print frames with the recovered crop; image-path rewrite; chapter `data-theme` |
| `tools/crown_alpha.py` | New: crowns with the bone margin cleared to alpha |
| `tools/deco_suite.py` | New: Deco suite generation (queue/collect, per-piece versions, lamp-free `SPOT_STYLE`), Waves 1–3 |
| `tools/cutout.py` | New: bone-to-alpha cut-out with stray removal, `--hull`, `--main-only`, `--navy-to-bone`, `--light-to-cyan` |
| `tools/upscale_print.py` | New: 4× RealESRGAN print masters via ComfyUI |
| `web/assets/art/{portraits,spots,sigils,badges,ornaments}/` | New web cut-outs |
| `web/assets/art/frames/*-crown.webp` | Rebuilt with alpha |
| `.gitignore` | `art/*/print/` |
| `docs/art/deco-suite-plan.md` | New: suite plan, chapter art standard (§5), Wave 3 list |
| `docs/art/generation-log.md` | Every pick, archive, and pipeline change |
| `docs/art/prototype-runs.jsonl` | Render log |
| `docs/pending-tasks.md`, `docs/continuation-prompt.md` | Session wrap |

## Key Design Decisions

- **Git workflow:** each discrete chunk goes on a branch and a PR, squash-merged with `gh` (the `main` ruleset allows squash only; 0 approvals, no CODEOWNERS). The user prefers reviewing chunks over granular commits.
- **Sheet portrait on page 2, beside Notes** (user's choice). Page 1 has no room; splitting Notes keeps all 13 lines.
- **Generate cut-outs on a flat bone field with margin, then key to alpha.** Rectangular crops flatten ornaments (the crown lesson), and outpainting a finished frame with flux1-dev doesn't work.
- **Drop caps are an art tile with the letter typeset on top.** Flux can't spell. Print uses a raised initial because WeasyPrint won't wrap text around a floated `::first-letter`.
- **Chapter art standard** (plan §5): consistency comes from templates and a build transform, not hand placement. Dividers go between top-level sections (h2 if the chapter has two or more, else h3), unless the text already groups sections with `<hr>`. Spots run about one per four sections, 1–3 per chapter.
- **Variety rule (user):** lamps and lamplight are never the focus; mix people, places, and daylight. `SPOT_STYLE` uses a lamp-free prefix, because the portrait prefix's light and lamp language caused the problem.
- **Web-only recolours:** navy ink goes to bone on the dark web page (neutral divider), and print keeps navy. The Tear's crack was shifted to cyan per the palette rule.
- **The print upscale runs inside ComfyUI's queue**, because a second GPU process won't fit beside Flux (12 GB VRAM). The PDF uses the web cut-outs for ornaments and spots (sharp enough at print size) and the 4× masters only for full-page frames.

## Open Issues

- **Corner ornaments:** they're on both callouts and stat blocks, and the user wanted to compare. Decide whether to keep both or trim to one.
- **Galvanic crown:** its rays still meet the top edge (there's no margin to clear). Fixing it needs a regenerated frame.
- **Approved Wave 2 spots still feature lamps** (the kit, the wounded man, timing, and others). The user said they're OK; don't repeat the pattern.
- **Deferred art:** chapter vignettes (Tier 3) and full-page plates (Tier 4).
- **Alternates on file:** Tear 8d, wild caster 11c, street 12a (v03), street v01, Mira 4036712205.
- **Environment:** the auto-mode safety check went down for a stretch; the SSH agent failed to sign once; the power profile in quiet mode made renders 2–4× slower (now in memory); low memory killed one stale background shell.

## Next Session

The art suite is complete. Decide on corners, then return to the content backlog: the name-collision renames, the Quick Reload rounding decision, series bible updates for Story 03, and planning the combat-focused story. Optionally, re-render the galvanic crown or start Tier 4 plates.
