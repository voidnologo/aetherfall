# Continuation Prompt

## Last Session (35): The Deco Art Suite — Portraits, Ornaments, Spots, and Print
- Lead portraits went onto the quickstart pregens and sheets. The web chapter crowns were rebuilt with alpha, so no ornament is cropped flat.
- Deco suite Waves 1–3 shipped: themed dividers, drop-cap tiles, a tailpiece, corners, six school emblems, zone badges, and 34 spots. Every chapter now meets the **chapter art standard** (plan §5).
- The PDF carries the same ornaments. Frames print at ~370 DPI from 4× upscales, and the WeasyPrint crash from the portrait grid is fixed.
- Work lands as self-merged PRs (#4–#17 this session); no direct pushes to `main`.

## Current State
- **Game:** Aetherfall (voidnologo/aetherfall). Eleventy 3.x, `npm run build`; PDF via `python3 scripts/build-pdf.py` (about 31 MB, ~200 pages).
- **Git:** one branch plus PR per discrete chunk, then `gh pr merge --squash --delete-branch` (`main` allows squash only). The shell has zsh noclobber on (use `>|`).
- **Art pipeline:** `tools/deco_suite.py` (`--queue-only`, then `--collect`) → pick on a comparison page → `tools/cutout.py` → web copies in `web/assets/art/` → place with `{% spot "name", "alt", "right|center" %}`. Print masters: `tools/upscale_print.py`. ComfyUI holds ~19 GB of RAM; `POST /free` before heavy work. Renders take ~1 min each in *performance* power mode (2–4 min in quiet).
- **Art rules:** never delete art (generated → approved or archived); no names in prompts; no lamp focus; cyan = Aether, amber = Engine.
- **CRITICAL:** Rulebook text changes need explicit approval. Art placements and templates are OK when asked.

## Immediate Next Task
1. Ask the user whether to keep corner ornaments on both callouts and stat blocks, or trim to one.
2. Content backlog: name-collision renames (Aldric Voss, Elara Voss, "Thornfeld", thin-cigar smokers), then the Quick Reload rounding decision.
3. Update the series bible with Story 03 outcomes; plan the combat-focused story.

## Key References
- Art: `docs/art/deco-suite-plan.md` (standard in §5), `docs/art/style-guide.md`, `docs/art/generation-log.md`
- Comparison pages: Wave 1 https://claude.ai/artifact/DzMSi3MowVHYAvorNbuzTG · Wave 2 https://claude.ai/artifact/LMoRK39oGSYeVmuR2jLXEa · Wave 3 https://claude.ai/artifact/8HXMstEWtT1sacm9vWwmst
- Canon: `docs/requirements/CANON_DECISIONS.md`; review: `docs/reviews/2026-09-26-consistency-review.md`
- Session record: `docs/sessions/session-35-notes.md`; pending: `docs/pending-tasks.md`

## Palette (Deco Lithograph)
Midnight `#0e1a2b` · Bone `#efe6d2` · Soot `#17140f` · Aether cyan `#3dc8e0` · Galvanic amber `#e8a825` · Oxblood `#8e2f23`
