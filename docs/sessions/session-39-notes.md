# Session 39: Rules Consistency, the Art Placement Standard, and Deco Flowcharts

**Date:** 2026-11-09 / 2026-11-10
**Goal:** Resolve issue #38 (13 numeric contradictions across the rules docs, plus a 3-item addendum), find whatever else disagreed, then fix the published rulebook, rebuild the PDF, and bring the art placement up to a professional standard.

## Overview

Issue #38 turned out to be the backlog item "Design-doc drift cleanup (review Tier 5)". Session 34 had fixed the published rulebook and recorded in `docs/reviews/2026-09-26-consistency-review.md` that the internal design docs were outside the approved scope; a year of edits later they had drifted a long way. That settled the direction for everything that followed: **`web/rules/*.njk` and `web/_data/characters/*.json` are the source of truth, and `docs/requirements/` follows them.**

The work ran in four passes. First the design docs (#39), then the published rulebook once the user approved touching it (#40), then the PDF, then the art. Each pass turned up more than the brief: the rulebook pass found two bugs players would have hit, and the art pass found that essentially no art in the book was placed according to any standard, because no placement standard existed.

---

## Changes Made

### Pass 1 — design docs, PR #39 (merged, closes #38)

All 16 issue items, plus what a cross-doc audit found:

- **Combat skills:** Melee/Brawl/Athletics are BR, Ranged is PC, guns use Firearms (CANON §4).
- **Weapon tables:** `COMBAT_PROCEDURE` §11 was a stale copy — reload times, the exotic Galvanic column and the crossbow rows now match `FIREARMS_EQUIPMENT` §3.
- **Reliability:** rolled under, every shot, 2 per net point (the 3% in the cheat sheet was the only survivor of a Session 8 change).
- **Casting times** come from `SPELL_COMPENDIUM`: Force 2ct, Reveal 4ct, Reshape 5ct, Mend 5ct. Reshape also disagreed, which the issue missed.
- **Armor existed in three incompatible models.** COMBAT and PROJECT_SPEC used a single Soak, ECONOMY had invented its own Ballistic/Martial values, the rulebook had a third. All now carry the rulebook's two ratings.
- **`ECONOMY.md` §11.1** opened by promising it changed no weapon or armor statistics, then disagreed with every melee Speed and Damage.
- **`GM_CHAPTER`** filed Melee and Athletics under PC, ran the dockmaster example on stats neither character has, and had Sera casting Detect — Divination is not one of her schools.
- Spell count 37 → 38, Ley Weaving 5 → 6 (Enchant). Tier hard-caps were off by one at both ends. 13 legacy "rounds" converted at 1 round = 3 counts. Non-skills removed: Running, Swimming, Metalworking, Repair, Conceal, Interrogation.
- **Starter module pregens rebuilt** from the character JSON, with skill levels shown so every target derives from `((10 + stat) × level) + 30`.

### Pass 2 — published rulebook, PR #40 (merged)

Two defects with real player impact:

- **The printable character sheet never rendered Casting Target on any sheet ever printed.** `sheet.njk:902` matched a skill literally named `Casting`; the data uses `Scholarly Casting` / `Wild Casting`. Fixed, and it now applies the wild +10 (Sera 64, Aldric 63).
- **The character builder was missing Enchant**, leaving Ley Weaving at five spells and making it impossible to build a caster who can create any artifact. It also hard-capped wild casters at two schools regardless of PW.

Plus: hard-cap table off by one and missing its Weak band; death saves undefined on exactly 50; malfunction severity capped at 10 where Galvanic adds +1 and Unstable +2; zone bands with +6, +13 and +21 belonging to no zone; healing potions a die step above the Mend spell they are brewed from; the stat check `(5 + stat) × 10` defined once and missing from every quick reference. Several worked examples contradicted their own characters.

### Pass 3 — PDF (#41, #43)

- `scripts/build-pdf.py` held **its own copies of the subtitle**, so the 1920s dating survived the web fix and reappeared on the rebuilt book.
- A page-by-page audit of the 239-page PDF found **16 pages blank except for a running head and folio**. Thirteen were the pages a forced recto break skips; a `@page :blank` rule strips the margin boxes. The other three were not blank at all — `pdfimages` showed two images and no text on each: the previous chapter's **tailpiece ornament had spilled onto a page of its own**.
- Confirmed correct: all 12 full plates on their own page, all 20 chapter openers on a recto, no split figures.

### Pass 4 — art placement, PR #42 (merged) and #44 (open)

Measured before any change: **22 of 22 plates sat immediately before a heading, 34 of 37 spots immediately after one**, 30 of those between a heading and its first paragraph. Nothing was embedded in body prose, so for 48 of 59 pieces the nearest text belonged to the previous section.

- `docs/art/art-placement.md` — the standard. `deco-suite-plan.md` §5 already set how much art a chapter carries; this sets where each piece goes.
- `tools/art_lint.py` — checks six conditions, exits non-zero. **60 placements, 0 violations.**
- Every piece now sits in the section whose subject it depicts; two near-duplicate pairs separated; float sides alternate (17/11/10 against 31/0/6); `spots/ford.webp`, shipped in Wave 4 and referenced by nothing, is placed.
- **Flowcharts (#44, open):** the printed charts had no styling at all — the build stripped every `classDef` and `:::class` and rendered with the stock `neutral` theme. Both media now share Source Serif 4 node text, letterspaced JetBrains Mono edge labels, square corners, straight connectors and the aether/galvanic palette.

---

## Files Modified

| File | What changed |
|---|---|
| `docs/requirements/*.md` (12 files) | The drift cleanup; see PR #39 |
| `docs/requirements/CANON_DECISIONS.md` | §10 the cleanup's locked calls, §11 the imprint rule |
| `docs/requirements/FIREARMS_EQUIPMENT.md` | §5.4 rewritten: the imprint, its lifetime table, its readers |
| `docs/requirements/WORLD_DESIGN.md` | §7.3 zone forensics rebuilt on the two clocks |
| `web/rules/*.njk` (18 files) | Rulebook corrections, then the art reflow |
| `web/_includes/sheet.njk` | Casting Target renders; wild +10; spells-known split by path |
| `web/rules/tools/character-builder.html` | Enchant added; wild schools derive from PW; wild +10 |
| `web/_data/characters/mira.json` | Derringer reload 2; arc pistol gains the Arcing keyword |
| `web/rules/css/print.css` | `@page :blank`; tailpiece and diagram keeps; `.plate-half` |
| `web/rules/css/styles.css` | `.plate-half` documented |
| `web/rules/mermaid-deco.json` | **New.** Print half of the shared flowchart theme |
| `scripts/build-pdf.py` | Subtitle; keeps `:::class`; uses the Deco config |
| `docs/art/art-placement.md` | **New.** The placement standard |
| `tools/art_lint.py` | **New.** The gate for it |
| `simulations/*.py` | Marked historical rather than updated |

---

## Key Design Decisions

**The imprint (user call, this session).** Magic leaves two traces. The **balance** is mechanical, decays 1 point per minute, and is the only one weapons and casters feel. The **imprint** is the place's memory of the working and is only ever read. **Lifetime = (accumulation generated)² hours.** Squaring it against a linear balance is what produces the user's three bands: a Weak spell fades by morning, a night of ritual work keeps five weeks, a catastrophe stays legible for decades, and the Tear sits off the end of the scale.

Naming: "residue" had been carrying two unrelated meanings — the place-trace and the wild-effect trace a caster carries until a long rest. The place sense became the **imprint**; residue keeps only the wild-effect meaning. Note the count given to the user when they chose was wrong: it was taken from the rulebook only, and across the design docs the place sense was the more entrenched of the two, including in both glossaries.

**An imprint never carries *who*.** `WORLD_DESIGN` §7.3 already ruled that forensics cannot identify a caster. The new §5.4 had promised Read would give a matchable signature; the setting rule won, and putting a name to a working stays conventional detective work.

**Two of the art rules are house decisions, and say so.** The research found no authority anywhere against art immediately before a heading — LaTeX's `placeins` exists because typesetters fight the *opposite* problem — and none requiring alternating float sides. Both are marked `[house]` in the standard with the reasoning stated. The rules that are backed cite IEEE, Chicago, NDSU and Utah.

**Full plates are exempt from the no-art-before-a-heading rule.** `print.css` gives `.plate-full` both `break-before: page` and `break-after: page`, so a plate inside a section throws the text before it onto one page and the text after onto another. The seam is where it belongs. This was wrong on the first pass and corrected.

**The web is the source of truth, the design docs follow.** Set by the Session 34 precedent and now written into `CANON_DECISIONS` §10 so the next reader does not have to re-derive it.

---

## Open Issues

- **The flowcharts do not fit a portrait page at any orientation.** Measured: top-down gives roughly 3:1 and 5:1 tall, so each fills most of a page and strands the heading above it; left-to-right inverts to about 1:7 and 1:12 wide, which would set the labels around 1in tall. Needs splitting into stages or re-authoring with subgraphs. PR #44 styles them but does not solve this.
- **The Combat Flowchart heading still strands** at p205, for the above reason.
- **`.plate-full` uses `break-before: page`** where the recorded intent ("a plate faces a chapter opener") needs `verso` plus the `@page :blank` rule that now exists. Changes pagination throughout, so it wants a visual pass.
- Print spots carry no `break-inside` or `clear`; the build pins no WeasyPrint version.
- Chapter-level art **clustering** is untouched. Several chapters front-load everything: magic's four pieces sit in the first 34%, state-of-the-world's five in the first 37%, and `grimoire.njk` (630 lines) has none at all. Fixing it means moving art between chapters, which is an editorial call.
- NPC skill targets in `quickstart.njk` were made to derive; the pregen JSONs were already correct.
- Issue #38's own line references are now stale, since the files were rewritten.

---

## Next Session

**The web rulebook's own styling and layout**, which this session only touched for correctness. The PDF has had three passes and the web has had none. Worth checking: how the reflowed art actually sits on the page at desktop and phone width, whether the float/clear behaviour holds, the 500px breakpoint where spots stop floating, and whether the chapters read well with their new art positions. Then the flowchart proportions, which are a web problem as much as a print one.
