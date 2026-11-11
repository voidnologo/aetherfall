# Session 40: The Web Layout Pass, and the Flowcharts Redrawn

**Date:** 2026-11-10
**Goal:** Merge the open PRs, then give the web rulebook the styling and layout pass it had never had, and fix the flowcharts — which turned into redrawing them.

## Overview

The PDF had three passes in session 39 and the web none, so the web went first. Measuring every chapter in a browser at 1440, 760 and 390px found one defect worth the whole exercise: **seven chapters scrolled the entire document sideways on a phone**, by up to 192px. Nothing in the markup says so, and no amount of reading the CSS would have found it.

The art pass then went somewhere the linter could not. The user pointed at the Thornfield Communion plate sitting inside the section about the offshore archipelago — right chapter, wrong subsection — which passed every mechanical check the standard has. Looking for that shape of error turned up a second class the linter *could* catch, and both are now rules.

The flowcharts took the rest of the session. Splitting them into stages fixed the geometry, but the user's judgment on the result was that Mermaid boxes with accent colours are not the house style and not what a published book should carry. They are now drawn.

---

## Changes Made

### PRs merged

- **#44** flowchart Deco styling, **#26** Story 01, **#25** Story 04. #25 conflicted in `web/_data/fiction.js` once #26 landed; resolved to `[STORY_04, STORY_03, STORY_02, STORY_01]` and all four stories load.
- **#3** (superseded draft) could not be closed: the permission classifier denied `gh pr close`. Still open.

### The phone overflow

A rules table cannot shrink below its own min-content width, so a 560px table in a 350px column dragged the page with it. Tables now build into a scroll container (`eleventy.config.js`, transform `table-scroll`), and `print.css` makes the wrapper inert so pagination is unchanged. The quick reference's cards overflowed their own grid track for the same reason — a grid item's automatic minimum is its min-content width — fixed with `min-width: 0`. Formulas carried `white-space: nowrap` and now wrap at phone width.

Final sweep: 20 chapters × 3 widths, no overflow, no float collisions, no starved floats.

### Art placement

- **The Thornfield Communion plate** moved out of *The Archipelago of Wonders* to the faction table that names it. The caption now sits beside the row that defines the Communion.
- **R2b [house]** — art never sits between a sentence ending in a colon and the block that sentence introduces. Six pieces did: `airship`, `tunnels`, `barrier`, `scales`, `sootborn`, `wounded`. Each moved below the block it introduced.
- **R4b [house]** — a float with a table directly under it becomes a centered spot. A table does not wrap a float.
- `count_paragraphs` counted `<p>` inside callouts, so a float with a table and a `{% street %}` panel after it looked like it had text beside it. Body paragraphs only now.
- Five floats had nothing to wrap them and are centered spots: `wounded`, `timing`, `dice`, `barrier`, `operatives`, plus `airship` which measured as a real collision.

60 placements, 0 violations.

### The flowcharts

Neither chart fitted a portrait page at any orientation — measured 3.58:1 and 2.13:1 top-down — which is why the Combat Flowchart heading stranded at p205. Each is now three staged diagrams, and they are **drawn rather than themed**.

`tools/flowcharts.py` holds the node wording (the rulebook's own), lets `dot` place it, and emits SVG with every silhouette, rule, rivet, arrowhead, frame and title block drawn to the style guide. The SVG carries **no colour**: every element has a class, and `styles.css` paints it midnight for the web while `print.css` paints the same asset bone for the book. Mermaid and its CDN runtime are gone, which also closes the "bundle Mermaid locally" backlog item.

---

## Files Modified

| File | Change |
|---|---|
| `eleventy.config.js` | `table-scroll` transform; `flowplate` inline-SVG shortcode |
| `web/rules/css/styles.css` | `.table-scroll`; the flowplate paint-up for the web |
| `web/rules/css/print.css` | wrapper made inert; flowplate repainted for bone paper; stage label hidden |
| `web/rules/reference.njk` | both charts staged and swapped to drawn plates; Mermaid runtime removed; formulas wrap on phones |
| `tools/flowcharts.py` | **New.** The plate generator |
| `web/assets/diagrams/*.svg` | **New.** Six plates |
| `tools/art_lint.py` | R2b, R4b; body-paragraph counting |
| `docs/art/art-placement.md` | R2b and R4b documented; checklist says plainly that subject match needs a reader |
| `web/rules/*.njk` (7 files) | the art moves above |
| `scripts/build-pdf.py` | Mermaid pre-render removed |
| `web/rules/mermaid-deco.json` | **Deleted.** Superseded |

---

## Key Design Decisions

**One drawing system, two inks (user's call).** The first pass gave each chart its own shape language, Deco for Combat and Nouveau for Spellcasting. The user judged the Deco better, so both are drawn that way and colour carries the distinction, which is how the rest of the book already works: amber is only ever the Engine, cyan only ever the Aether. A reader learns one vocabulary of shapes instead of two.

**The plate carries its own header.** A stage label set above the diagram in the page stranded at a page foot, and `break-after: avoid` could not hold it: a tall figure with `break-inside: avoid` leaves the span no legal break point, so CSS Fragmentation §4.4 drops the whole avoid-chain. The same mechanism gave the chapter's tailpiece a page of its own. Both are solved by construction — the stage name is drawn inside the plate, and the generator sizes each plate in inches to fit a box with room left under it.

**The linter keeps only the rules it can decide.** R4b first checked two blocks below a float and flagged three placements that measure clean in a browser: whether a table further down collides depends on how tall the intervening paragraph renders, which the markup does not say. It was narrowed back to the block directly below.

**Subject match needs a reader.** The Thornfield plate passed every mechanical check from inside the wrong section. The standard now says so where the checklist is, rather than implying the linter is sufficient.

---

## Open Issues

- **PR #3 is still open.** `gh pr close` was denied by the permission classifier.
- **Two plates print small.** `combat-2-attack` sets its node text at about 5.3pt and `spell-2-roll` at 6.9pt, against roughly 9.5pt for the rest. Both are information-density limits, not scaling bugs: the attack plate carries a four-way branch and the roll plate an eight-node chain, and uniform scaling cannot raise the text without taking more inches. Fixing either means splitting it again (a content change) or setting it as a landscape plate.
- `.plate-full` still uses `break-before: page` where the recorded intent needs `verso`. Untouched.
- Art clustering across chapters is untouched.
- The responsive measuring was done with a throwaway in-browser harness. It found what reading the CSS would not, and it is not in the repo; a standing layout check would want building properly.

## Next Session

The two small-printing plates, if the user wants them at parity. Then the remaining backlog: `.plate-full` to verso, art clustering, and the web hero and og:image cards from the spare approved covers.
