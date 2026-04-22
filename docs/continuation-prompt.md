# Continuation Prompt

## Last Session (33) — Story 03 "The Lamplighter's Price" Written

- Revised Story 03 plan to foreground game mechanics as lived narrative (Record of Lodoss War model)
- Updated series bible with full Story 02 outcomes (NPCs, locations, character tracker, seeds)
- Wrote all 8 chapters of Story 03 — magic system showcase: Sera's wild casting (river) vs Aldric's scholarly casting (lattice), exhaustion spiral, backlash, Aether/Galvanic tech interference
- Key beat: Sera's almost-involuntary Amplify on the artifact — tears herself free, develops first caution toward the magic
- PR open: https://github.com/voidnologo/aetherfall/pull/2 — user reading draft in GitHub, will leave editing notes

## Previous Session (32) — Story 03 Plan Created

- Created initial 8-chapter plan for "The Lamplighter's Price"
- Fels blackmails the Society into retrieving Syndicate cargo from the foundry tunnels

## Current State
- **Game title:** Aetherfall (repo: voidnologo/aetherfall)
- **Build:** Eleventy 3.x — `npm run dev` / `npm run build` — deploys via GitHub Action with `--pathprefix=/aetherfall/`
- **Path rule:** use relative paths in new pages, or run absolute paths through the `| url` filter. Raw `/foo` breaks at the subpath.
- **Website:** 18 chapters + quickstart (.njk) + character sheets + interactive tools + `/fiction/` landing + reader
- **Fiction:** 6 world reference docs in `fiction/world/`; Story 02 published as "What the Mill Remembered"; Story 03 draft on PR branch `story-03-lamplighters-price`
- **Fiction data loader:** `web/_data/fiction.js` — hard-coded to story 02 for now; generalize when story 03 ships
- **Art pipeline:** `art/{type}/{generated|approved|archived}/` — art NEVER deleted, only moved
- **Art generation:** `python tools/comfyui_generate.py` — builds flux-dev workflows, queues via ComfyUI API
- **Founding event:** "The Tear" (was "the Eruption" — renamed session 27)
- **CRITICAL RULE:** Rulebook content must NEVER be changed without explicit user approval.
- **CRITICAL RULE:** Art is NEVER deleted. Moves through generated -> approved or generated -> archived.

## Immediate Next Tasks
- Address editing notes from PR #2 (user reviewing Story 03 in GitHub)
- Merge Story 03 PR after edits
- Build web reader page for Story 03, generalize `web/_data/fiction.js`
- Update series bible with final Story 03 outcomes
- Plan the combat-focused story (next in series — Kael-heavy, damage, timing track, Galvanic devices)

## Key References
- Fiction world docs: `fiction/world/01-the-world.md` through `06-series-bible.md`
- Story 02 chapters: `fiction/stories/story-02/ch01.md` through `ch10.md`
- Story 03 plan: `fiction/stories/story-03/PLAN.md`
- Story 03 chapters: `fiction/stories/story-03/ch01.md` through `ch08.md`
- Fiction web data: `web/_data/fiction.js`
- Fiction web templates: `web/fiction/index.njk`, `web/fiction/what-the-mill-remembered.njk`
- Style guide: `fiction/world/05-style-guide.md`
- Magic system: `docs/requirements/MAGIC_SYSTEM.md`
- Spell compendium: `docs/requirements/SPELL_COMPENDIUM.md`
- Character sheets: `web/_data/characters/*.json`

## Color Reference
- **Aether:** `#3dc8e0` | **Galvanic:** `#e8a825` | **Background:** `#080b14`
- **Fonts:** Playfair Display (headings), Source Serif 4 (body), Cormorant Garamond (labels)
