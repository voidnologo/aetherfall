# Continuation Prompt

## Last Sessions (35–36): The Deco Art Suite, then Cleanup
- **35:** lead portraits, alpha crowns, and Deco Waves 1–3 (dividers, drop caps, tailpiece, corners, emblems, badges, 34 spots). Every chapter meets the **chapter art standard** (plan §5), and the PDF carries the same art, with ~370 DPI frames.
- **36:** every spot re-cut clipped to its circle (stray stamps and signatures had stretched the outlines), portrait and frame edge artifacts cropped, and body text justified with hyphenation on web and print.
- All work lands as self-merged PRs (#4–#20); no direct pushes to `main`.

## Current State
- **Game:** Aetherfall (voidnologo/aetherfall). Eleventy 3.x, `npm run build`; PDF via `python3 scripts/build-pdf.py` (about 31 MB, ~200 pages).
- **Git:** one branch plus PR per discrete chunk, then `gh pr merge --squash --delete-branch` (`main` allows squash only). The shell has zsh noclobber on (use `>|`).
- **Art pipeline:** `tools/deco_suite.py` (`--queue-only`, then `--collect`) → pick on a comparison page → `tools/cutout.py` (round spots: `--circle`; record them in `tools/spot_manifest.json`, re-cut with `tools/recut_spots.py`) → web copies in `web/assets/art/` → place with `{% spot "name", "alt", "right|center" %}`. Print masters: `tools/upscale_print.py`. ComfyUI holds ~19 GB of RAM; `POST /free` before heavy work. Renders take ~1 min each in *performance* power mode (2–4 min in quiet).
- **Art rules:** never delete art (generated → approved or archived); no names in prompts; no lamp focus; cyan = Aether, amber = Engine.
- **CRITICAL:** Rulebook text changes need explicit approval. Art placements and templates are OK when asked.

## Immediate Next Task: Wave 4, Large Scene Artwork
1. Walk the user through the draft in `docs/art/deco-suite-plan.md` §6: plates vs half-page scenes, which chapters, web and PDF placement, and whether the leads appear. Candidates include the Tear 50 years ago, the leads in the Wet Ember, and a Wild Zone swallowing a rail yard.
2. Add a `PLATE_STYLE` (full-bleed, lamp-free) to `tools/deco_suite.py`, generate 3 seeds each, and publish a comparison page. Crop off edge lettering and stamps; plates stay rectangular.
3. Place them on the web and in the PDF (a full-page plate page type), then run the print upscale.
4. Later: corner ornament decision; content backlog (name-collision renames, Quick Reload rounding, series bible, combat story).

## Key References
- Art: `docs/art/deco-suite-plan.md` (standard in §5), `docs/art/style-guide.md`, `docs/art/generation-log.md`
- Comparison pages: Wave 1 https://claude.ai/artifact/DzMSi3MowVHYAvorNbuzTG · Wave 2 https://claude.ai/artifact/LMoRK39oGSYeVmuR2jLXEa · Wave 3 https://claude.ai/artifact/8HXMstEWtT1sacm9vWwmst
- Canon: `docs/requirements/CANON_DECISIONS.md`; review: `docs/reviews/2026-09-26-consistency-review.md`
- Session records: `docs/sessions/session-35-notes.md`, `session-36-notes.md`; pending: `docs/pending-tasks.md`

## Palette (Deco Lithograph)
Midnight `#0e1a2b` · Bone `#efe6d2` · Soot `#17140f` · Aether cyan `#3dc8e0` · Galvanic amber `#e8a825` · Oxblood `#8e2f23`
