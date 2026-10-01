# Continuation Prompt

## Last Session (37): Wave 4 Art, Stories 01 and 04, and the Deco Fiction Reader
- Fiction reader matches the rulebook (crowns, drop caps, dividers, tailpiece, corners, justified prose). Canon settled: Gideon Marlow, Elara Pryce, Hollowmere, Fels's clove cigarettes, Quick Reload rounds up.
- Wave 4: 111 renders overnight in cool-down blocks; two rounds of picks on a click-to-pick page. **Placed:** 22 plates/scenes in 14 chapters, Laine's portrait, 3 spots, the "Faces of Ashwick" cast (7 portraits) on the fiction index, a full-bleed PDF cover.
- Written overnight, **on open PRs for review:** Story 01 "The Ashwick Job" (#26; the Quickstart as fiction, ends with Play This Story) and Story 04 "No Kinder Country" (#25; the combat story).

## Current State
- **Game:** Aetherfall (voidnologo/aetherfall). Eleventy 3.x, `npm run build`; PDF via `python3 scripts/build-pdf.py` (235 pp, 44.7 MB; `POST /free` to ComfyUI first if it's running, because WeasyPrint needs RAM).
- **Git:** one branch + PR per chunk, `gh pr merge --squash`. zsh noclobber (use `>|`). If the SSH agent won't sign, push with `git -c credential.helper= -c credential.helper='!gh auth git-credential' push https://github.com/voidnologo/aetherfall.git <branch>`.
- **Art pipeline:** prompts in `tools/deco_suite.py`; overnight batches via `tools/render_blocks.py` (run detached with `setsid nohup`; blocks + GPU rests); picks via `tools/wave_page.py` → selector artifact (tap to pick, copy codes); approved → `art/*/approved`, the rest → `archived` (never delete). Full-bleed web copies: `tools/plate_manifest.json` + `tools/plate_web.py` (fills, crops, border trim). Round spots: `tools/spot_manifest.json` + `recut_spots.py`. Print masters: `tools/upscale_print.py`. Place with `{% plate "name", "alt", "caption", "full|half" %}` or `{% spot … %}`.
- **Art rules:** no names in prompts, no lamp focus, cyan = Aether, amber = Engine, no real-world lettering.
- **CRITICAL:** rulebook text changes need explicit approval; art placements OK when asked.

## Immediate Next Task
1. Review PRs #26 and #25 with the user; merge (fix the `fiction.js`/bible conflict on the second), close draft #3, rebuild, check the reader.
2. Web hero redraw and og:image cards from the spare covers.
3. Reroll Hesper (one arm). Then plan Story 05.

## Key References
- Art: `docs/art/deco-suite-plan.md` (§5 standard, §6 Wave 4, §7 fiction reader), `docs/art/style-guide.md`, `docs/art/generation-log.md`
- Wave 4 selector: https://claude.ai/artifact/E47GCrji4ykVKy3TyJWm4z
- Fiction: `fiction/world/05-style-guide.md`, `06-series-bible.md`; stories in `fiction/stories/story-0N/` (PLAN.md + chapters); reader data `web/_data/fiction.js`, cast `web/_data/cast.json`
- Canon: `docs/requirements/CANON_DECISIONS.md` (§8 renames, §9 Quick Reload)
- Session records: `docs/sessions/session-37-notes.md`; pending: `docs/pending-tasks.md`

## Palette (Deco Lithograph)
Midnight `#0e1a2b` · Bone `#efe6d2` · Soot `#17140f` · Aether cyan `#3dc8e0` · Galvanic amber `#e8a825` · Oxblood `#8e2f23`
