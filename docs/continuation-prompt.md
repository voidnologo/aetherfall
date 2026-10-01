# Continuation Prompt

## Last Session (38): Natural Prose — AI-ism Guide, Prose Skills, Line Edits
- Researched AI prose tells and wrote `docs/writing/natural-prose.md`, `tools/prose_lint.py` (per-1k rates plus antislop lists), the `prose-check` skill, and a portable user-level `natural-prose` skill (backup in `tools/skills/natural-prose/`). CLAUDE.md now requires a prose check.
- Line-edited without changing content: Stories 01 (#26) and 04 (#25), still open; the published 02/03 (#33, merged); the whole rulebook (#34, merged: em dashes 21.5 → 0.6 per 1k, wording only, numbers verified).

## Current State
- **Game:** Aetherfall (voidnologo/aetherfall). Eleventy 3.x, `npm run build`; PDF via `python3 scripts/build-pdf.py` (235 pp, 44.7 MB; `POST /free` to ComfyUI first if it's running, because WeasyPrint needs RAM).
- **Git:** one branch + PR per chunk, `gh pr merge --squash`. zsh noclobber (use `>|`). If the SSH agent won't sign, push with `git -c credential.helper= -c credential.helper='!gh auth git-credential' push https://github.com/voidnologo/aetherfall.git <branch>`.
- **Art pipeline:** prompts in `tools/deco_suite.py`; overnight batches via `tools/render_blocks.py` (run detached with `setsid nohup`; blocks + GPU rests); picks via `tools/wave_page.py` → selector artifact (tap to pick, copy codes); approved → `art/*/approved`, the rest → `archived` (never delete). Full-bleed web copies: `tools/plate_manifest.json` + `tools/plate_web.py` (fills, crops, border trim). Round spots: `tools/spot_manifest.json` + `recut_spots.py`. Print masters: `tools/upscale_print.py`. Place with `{% plate "name", "alt", "caption", "full|half" %}` or `{% spot … %}`.
- **Art rules:** no names in prompts, no lamp focus, cyan = Aether, amber = Engine, no real-world lettering.
- **CRITICAL:** rulebook text changes need explicit approval; art placements OK when asked.
- **Prose:** run `python3 tools/prose_lint.py --summary <files>` on any fiction or prose before committing (rulebook: `tools/rulebook_prose.py DIR` first). The user strongly dislikes AI tics: ", and" chains, "the way X does Y", "Not X. Y.", em-dash overuse.

## Immediate Next Task
1. Proof the draft-print PDF (built, local only by choice; skim the Grimoire tables).
2. User reviews #26 and #25 (new stories); merge (fix the `fiction.js`/bible conflict on the second), close draft #3.
3. Web hero and og:image cards; Hesper reroll; plan Story 05 (written with `prose-check`).

## Key References
- Art: `docs/art/deco-suite-plan.md` (§5 standard, §6 Wave 4, §7 fiction reader), `docs/art/style-guide.md`, `docs/art/generation-log.md`
- Wave 4 selector: https://claude.ai/artifact/E47GCrji4ykVKy3TyJWm4z
- Fiction: `fiction/world/05-style-guide.md`, `06-series-bible.md`; stories in `fiction/stories/story-0N/` (PLAN.md + chapters); reader data `web/_data/fiction.js`, cast `web/_data/cast.json`
- Prose: `docs/writing/natural-prose.md`, `.claude/skills/prose-check/`, `tools/prose_lint.py`, `tools/rulebook_prose.py`
- Canon: `docs/requirements/CANON_DECISIONS.md` (§8 renames, §9 Quick Reload)
- Session records: `docs/sessions/session-38-notes.md`; pending: `docs/pending-tasks.md`

## Palette (Deco Lithograph)
Midnight `#0e1a2b` · Bone `#efe6d2` · Soot `#17140f` · Aether cyan `#3dc8e0` · Galvanic amber `#e8a825` · Oxblood `#8e2f23`
