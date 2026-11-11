# Continuation Prompt

## Last Session (40): The Web Layout Pass, and the Flowcharts Redrawn
- Merged #44, #26 and #25 (both stories are live; `web/_data/fiction.js` carries all four). #3 is still open — `gh pr close` was denied by the permission classifier.
- **Seven chapters scrolled the whole document sideways on a phone**, up to 192px: a rules table cannot shrink below its own min-content width. Tables now build into a scroll container that print.css makes inert. 20 chapters × 3 widths now measure clean.
- Art: the Thornfield Communion plate sat in the section about the offshore archipelago and passed every mechanical check. Moved, and two rules added (**R2b** no art between a colon lead-in and the block it introduces; **R4b** a float with a table under it becomes centered). 60/60 clean.
- **The flowcharts are drawn, not themed.** `tools/flowcharts.py` takes the rulebook's node wording, lets `dot` place it, and emits SVG carrying no colour — painted midnight for the web, bone for print. One Deco system, amber/cyan carrying Engine/Veil. Mermaid is gone.
- Book rebuilt at 241 pp: both flowchart headings sit with their first plate, every plate whole, the 13 text-free pages are the recto-break blanks.

## Current State
- **Game:** Aetherfall (voidnologo/aetherfall). Eleventy 3.x, `npm run build`; PDF via `python3 scripts/build-pdf.py` (241 pp, 48.6 MB; rebuild `_site` first — the PDF reads `_site/rules/*.html`, not the `.njk` sources). `POST /free` to ComfyUI first if it is running.
- **Open PRs:** #46 (this session's work, ready), #3 (superseded draft, needs closing).
- **Git:** one branch + PR per chunk, `gh pr merge --squash`. zsh noclobber (use `>|`). Pages deploys on push to main touching `web/**`.
- **Diagrams:** `python3 tools/flowcharts.py` regenerates `web/assets/diagrams/*.svg` after any node-wording change. The SVG holds no colour; both stylesheets paint it. Needs graphviz (`dot`).
- **Art pipeline:** prompts in `tools/deco_suite.py`; batches via `tools/render_blocks.py`; picks via `tools/wave_page.py`; approved → `art/*/approved`, rest → `archived` (never delete).
- **Art rules:** no names in prompts, no lamp focus, cyan = Aether, amber = Engine, no real-world lettering. **Run `python3 tools/art_lint.py` before committing art moves** — and read the caption against its heading yourself, which the linter cannot do.
- **CRITICAL:** rulebook text changes need explicit approval; art placements OK when asked.
- **Prose:** run `python3 tools/prose_lint.py --summary <files>` before committing prose (rulebook: `tools/rulebook_prose.py DIR` first). No ", and" chains, no "the way X does Y", no "Not X. Y.", no em-dash overuse.

## Immediate Next Task
1. **The two small-printing plates** — `combat-2-attack` at ~5.3pt and `spell-2-roll` at ~6.9pt against ~9.5pt elsewhere. Split again (content change) or set landscape.
2. **Close #3; review and merge #46.**
3. **Proof the PDF** — the structure is audited, nobody has read it.

## Key References
- Diagrams: `tools/flowcharts.py` (node wording, both registers, print fitting)
- Art: `docs/art/art-placement.md` (**standard, R1–R9 with house vs convention labelled**), `docs/art/deco-suite-plan.md` (§5 density, §6 Wave 4), `docs/art/style-guide.md` (§3 the Deco/Nouveau split)
- Canon: `docs/requirements/CANON_DECISIONS.md` (§10 drift-cleanup calls, §11 the imprint)
- Consistency precedent: `docs/reviews/2026-09-26-consistency-review.md` — **the web is the source of truth, design docs follow**
- Fiction: `fiction/world/05-style-guide.md`, `06-series-bible.md`; reader data `web/_data/fiction.js`, cast `web/_data/cast.json`
- Prose: `docs/writing/natural-prose.md`, `.claude/skills/prose-check/`
- Session records: `docs/sessions/session-40-notes.md`; pending: `docs/pending-tasks.md`

## Palette (Deco Lithograph)
Midnight `#0e1a2b` · Bone `#efe6d2` · Soot `#17140f` · Aether cyan `#3dc8e0` · Galvanic amber `#e8a825` · Oxblood `#8e2f23`
