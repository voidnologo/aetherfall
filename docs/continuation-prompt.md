# Continuation Prompt

## Last Session (34): Consistency Review, Canon Lock & Deco Lithograph Art Direction

- Full consistency review → ~150 approved fixes to the rulebook, pregens, fiction, and docs. Canon locked in `docs/requirements/CANON_DECISIONS.md` (Kael Dunn; Tear 50 years ago; crit rule; no rounds; not Earth).
- Art direction chosen: **D, Deco Lithograph** (six-ink palette; cyan = Aether, amber = Engine). Portraits of all four leads approved; one chapter frame per theme; sheet watermark.
- Art wired in: web chapter crowns, PDF chapter openers, Two Inks front matter, new sheet watermark. PDF Mermaid diagrams fixed.

## Current State
- **Game:** Aetherfall (voidnologo/aetherfall). Eleventy 3.x, `npm run build`; PDF via `python3 scripts/build-pdf.py` (WeasyPrint is a uv tool).
- **Art pipeline:** `tools/prototype_styles.py` (direction D2): `POST localhost:8188/free`, then `--queue-only`, then `--collect`. ComfyUI holds ~19 GB of RAM; don't leave background waiters running.
- **Approved art:** `art/characters/approved/` (Kael, Sera, Aldric, Mira ×2), `art/decorative/approved/` (4 theme frames, watermark, Two Inks front-matter frame). Web copies: `web/assets/art/`.
- **CRITICAL:** Rulebook changes need explicit approval. Art is never deleted (generated → approved or archived). Never put character names in prompts. Skin tone unspecified unless characterful.

## Immediate Next Task: Try Out the Artwork
1. Add the lead portraits to the quickstart pregen sections (`web/rules/quickstart.njk`) and the character sheets (`web/_includes/sheet.njk`, `web/_data/characters/*.json`). Ask which Mira image is the reference (2096254533 recommended).
2. Review the framed chapter crowns (web) and openers/front matter (PDF) with the user; tweak placement.
3. Plan the next Deco art suite (spot illustrations, header bands, dividers) with the user.

## Key References
- Canon: `docs/requirements/CANON_DECISIONS.md`
- Review: `docs/reviews/2026-09-26-consistency-review.md`
- Art: `docs/art/style-guide.md`, `docs/art/generation-log.md`, prototype page https://claude.ai/artifact/KLMQwvngArrLWZpTzRGHhL
- Session record: `docs/sessions/session-34-notes.md`; pending: `docs/pending-tasks.md`

## Palette (Deco Lithograph)
Midnight `#0e1a2b` · Bone `#efe6d2` · Soot `#17140f` · Aether cyan `#3dc8e0` · Galvanic amber `#e8a825` · Oxblood `#8e2f23`
