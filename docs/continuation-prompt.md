# Continuation Prompt

## Last Session (39): Rules Consistency, the Art Placement Standard, Deco Flowcharts
- Closed issue #38 and the "design-doc drift" backlog item: `docs/requirements/` now agrees with the published rulebook (#39). The rulebook then got its own pass (#40), which fixed two real defects — the printable sheet never rendered Casting Target on any sheet, and the character builder was missing Enchant so no buildable caster could make an artifact.
- PDF rebuilt at 239 pp and audited page by page (#41, #43): 16 pages were blank but for a running head; three of those were a tailpiece spilling onto its own page.
- Art: `docs/art/art-placement.md` + `tools/art_lint.py` (60/60 clean) and a reflow of every piece (#42). Before it, 22 of 22 plates sat immediately before a heading and 34 of 37 spots immediately after one.
- New rule, user's design: the **imprint** — what a place remembers of a working, lifetime = (accumulation)² hours, read-only, never carries *who*. Distinct from wild-effect **residue**.

## Current State
- **Game:** Aetherfall (voidnologo/aetherfall). Eleventy 3.x, `npm run build`; PDF via `python3 scripts/build-pdf.py` (239 pp, 49.3 MB; rebuild `_site` first — the PDF reads `_site/rules/*.html`, not the `.njk` sources). `POST /free` to ComfyUI first if it is running.
- **Open PRs:** #44 (flowchart Deco styling, ready), #26 and #25 (stories, awaiting user), #3 (draft, close).
- **Git:** one branch + PR per chunk, `gh pr merge --squash`. zsh noclobber (use `>|`). Pages deploys on push to main touching `web/**`.
- **Art pipeline:** prompts in `tools/deco_suite.py`; batches via `tools/render_blocks.py`; picks via `tools/wave_page.py`; approved → `art/*/approved`, rest → `archived` (never delete). Web copies: `plate_manifest.json`/`plate_web.py`, `spot_manifest.json`/`recut_spots.py`.
- **Art rules:** no names in prompts, no lamp focus, cyan = Aether, amber = Engine, no real-world lettering. **Placement is now a standard with a linter — run `python3 tools/art_lint.py` before committing art moves.**
- **CRITICAL:** rulebook text changes need explicit approval; art placements OK when asked.
- **Prose:** run `python3 tools/prose_lint.py --summary <files>` before committing prose (rulebook: `tools/rulebook_prose.py DIR` first). No ", and" chains, no "the way X does Y", no "Not X. Y.", no em-dash overuse.

## Immediate Next Task
1. **Web rulebook styling and layout pass** — the PDF has had three passes, the web none. Check the reflowed art at desktop and phone width, float/clear behaviour, the 500px breakpoint, and how chapters read with art in its new positions.
2. **Flowchart proportions** — neither orientation fits a page (3:1 and 5:1 tall, or 1:7 and 1:12 wide). Split into stages or re-author with subgraphs. Merge #44 first.
3. Proof the PDF; review #26/#25 and close #3.

## Key References
- Art: `docs/art/art-placement.md` (**placement standard, house vs convention labelled**), `docs/art/deco-suite-plan.md` (§5 density, §6 Wave 4), `docs/art/style-guide.md`
- Canon: `docs/requirements/CANON_DECISIONS.md` (§10 drift-cleanup calls, §11 the imprint)
- Consistency precedent: `docs/reviews/2026-09-26-consistency-review.md` — **the web is the source of truth, design docs follow**
- Fiction: `fiction/world/05-style-guide.md`, `06-series-bible.md`; reader data `web/_data/fiction.js`, cast `web/_data/cast.json`
- Prose: `docs/writing/natural-prose.md`, `.claude/skills/prose-check/`
- Session records: `docs/sessions/session-39-notes.md`; pending: `docs/pending-tasks.md`

## Palette (Deco Lithograph)
Midnight `#0e1a2b` · Bone `#efe6d2` · Soot `#17140f` · Aether cyan `#3dc8e0` · Galvanic amber `#e8a825` · Oxblood `#8e2f23`
