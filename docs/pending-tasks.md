# Pending Tasks

## Next Up
- [ ] **Web rulebook styling and layout pass.** The PDF has had three passes this session and the web has had none. Check the reflowed art at desktop and phone width, the float/clear behaviour, the 500px breakpoint where spots stop floating, and whether chapters read well with their new art positions.
- [ ] **Flowchart proportions.** Both Mermaid charts fit no portrait page: top-down is roughly 3:1 and 5:1 tall, left-to-right about 1:7 and 1:12 wide. Split each into stages or re-author with subgraphs. PR #44 styles them to match the book but does not fix this, and it is why the Combat Flowchart heading strands at p205.
- [ ] **Review and merge PR #44** (flowchart Deco styling).
- [ ] **Proof the draft-print PDF** (239 pp, local only by choice; skim the Grimoire tables). `POST /free` to ComfyUI first if it is running.
- [ ] **Review and merge the new stories:** PR #26 (Story 01, 10.9k words) and PR #25 (Story 04, 23.0k). Whichever merges second needs a small conflict fix in `web/_data/fiction.js` (keep `[STORY_04, STORY_03, STORY_02, STORY_01]`) and the series bible. Then close draft PR #3.
- [ ] **Web hero and social previews:** use the spare approved covers ("four on the hill road", "the Tear over the skyline") for a Deco web hero redraw and og:image cards.
- [ ] Reroll Hesper Brack's portrait with one arm (canon); then restore "One arm, one rule" in `web/_data/cast.json`
- [ ] Plan Story 05 (the Collective's retribution: agents in Ashwick, the flat compromised, the Veilwright Quarter as refuge; Sera's tunnel vision surfaces). Write it with `prose-check` from the first draft.
- [ ] Decide: spell names in Story 02 prose (Detect, Reveal, cantrip) vs the "no mechanics in fiction" rule

## Backlog
- [ ] **Art clustering.** Placement is now correct piece by piece, but several chapters front-load everything: magic's four pieces sit in the first 34%, state-of-the-world's five in the first 37%, and `grimoire.njk` (630 lines) has none at all. Fixing it means moving art between chapters — an editorial call, not a mechanical one.
- [ ] **`.plate-full` should break to verso**, not `page`, so a plate faces its chapter opener as `deco-suite-plan.md` §6 intended. The `@page :blank` rule it needs now exists. Changes pagination throughout, so it wants a visual pass.
- [ ] Print spots carry no `break-inside` or `clear`; the PDF build pins no WeasyPrint version.
- [ ] Re-render the galvanic chapter frame with a margin at the top (its crown's rays meet the edge)
- [ ] Deco Tier 3 (deferred): chapter vignettes inside the PDF openers or under the web crowns
- [ ] Small school emblems beside `.spell-school` labels in the Grimoire spell list
- [ ] Palette-snap post-processing step (quantise to the six inks)
- [ ] Two Inks look for fiction reader openers? (frame kept)
- [ ] Cross-device reading test of published fiction reader (and justified text on a real phone)
- [ ] Set up S3 bucket for art sync (art binaries are gitignored)
- [ ] Bundle Mermaid.js locally for offline web flowcharts
- [ ] More GM tools: NPC, mission brief, and Society generators
- [ ] Design "Push Timing" and zone formation/shift mechanics
- [ ] Bestiary; simplified NPC stat blocks
- [ ] Spell compendium second pass
- [ ] Mobile sidebar UX testing on real devices
