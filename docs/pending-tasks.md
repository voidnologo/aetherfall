# Pending Tasks

## Next Up
- [ ] **Decide the two small-printing plates.** `combat-2-attack` sets its node text at about 5.3pt and `spell-2-roll` at 6.9pt, against roughly 9.5pt for the other four. Information-density limits, not scaling bugs — a four-way branch and an eight-node chain. Either split them again (a content change, needs approval) or set them as landscape plates.
- [ ] **Close PR #3** (superseded Story 04 draft). `gh pr close` was denied by the permission classifier this session; needs the user, or a permission rule for `gh`.
- [ ] **Review and merge PR #46** (web layout pass, art placement rules, flowchart plates).
- [ ] **Proof the draft-print PDF** (241 pp, local only by choice; skim the Grimoire tables). The structure was audited this session — headings sit with their plates, the 13 text-free pages are the recto-break blanks — but nobody has read it. `POST /free` to ComfyUI first if it is running.
- [ ] **Web hero and social previews:** use the spare approved covers ("four on the hill road", "the Tear over the skyline") for a Deco web hero redraw and og:image cards.
- [ ] Reroll Hesper Brack's portrait with one arm (canon); then restore "One arm, one rule" in `web/_data/cast.json`
- [ ] Plan Story 05 (the Collective's retribution: agents in Ashwick, the flat compromised, the Veilwright Quarter as refuge; Sera's tunnel vision surfaces). Write it with `prose-check` from the first draft.
- [ ] Decide: spell names in Story 02 prose (Detect, Reveal, cantrip) vs the "no mechanics in fiction" rule

## Backlog
- [ ] **A standing layout check.** The responsive sweep that found the phone overflow was a throwaway in-browser harness and is not in the repo. Reading the CSS would not have found it: a table's min-content width is a render-time fact. Worth building properly if layout regressions matter.
- [ ] **Art clustering.** Placement is correct piece by piece, but several chapters front-load everything: magic's four pieces sit in the first 34%, state-of-the-world's five in the first 37%, and `grimoire.njk` (630 lines) has none at all. Fixing it means moving art between chapters — an editorial call, not a mechanical one.
- [ ] **`.plate-full` should break to verso**, not `page`, so a plate faces its chapter opener as `deco-suite-plan.md` §6 intended. The `@page :blank` rule it needs now exists. Changes pagination throughout, so it wants a visual pass.
- [ ] Print spots carry no `break-inside` or `clear`; the PDF build pins no WeasyPrint version
- [ ] Re-render the galvanic chapter frame with a margin at the top (its crown's rays meet the edge)
- [ ] Deco Tier 3 (deferred): chapter vignettes inside the PDF openers or under the web crowns
- [ ] Small school emblems beside `.spell-school` labels in the Grimoire spell list
- [ ] Palette-snap post-processing step (quantise to the six inks)
- [ ] Two Inks look for fiction reader openers? (frame kept)
- [ ] Cross-device reading test of published fiction reader (and justified text on a real phone)
- [ ] Set up S3 bucket for art sync (art binaries are gitignored)
- [ ] More GM tools: NPC, mission brief, and Society generators
- [ ] Design "Push Timing" and zone formation/shift mechanics
- [ ] Bestiary; simplified NPC stat blocks
- [ ] Spell compendium second pass
- [ ] Mobile sidebar UX testing on real devices
