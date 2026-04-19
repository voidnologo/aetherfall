# Continuation Prompt

## Last Session (32) — Story 03 Plan: "The Lamplighter's Price"

- Created 8-chapter plan for Story 03 — Fels blackmails the Society into retrieving Syndicate cargo from the foundry tunnels
- Key narrative beats: tunnels transforming like the mill (same agency, beneath a Galvanic factory), Kael-Mira trust crack, Sera's secret vision of a network beneath the city
- Fels is blackmailing them (not collecting a debt) — they cost him during the Ashwick Job and he has information leverage
- Plan includes character status trackers, society status, and seed tracking tables

## Previous Session (31) — Fiction Landing + Reader Published

- Titled Story 02 **"What the Mill Remembered — A Tale of the Ash & Veil Society"**
- Built `/fiction/` landing and single-page reader at `/fiction/what-the-mill-remembered.html` (sticky bar, scroll-progress, drop caps, scene-break ornaments, collapsible chapter TOC drawer)
- Wired fiction links from main landing + rulebook sidebar footer + end of gm-tools
- Fixed subpath deploy bug: raw `/...` paths bypass Eleventy's `--pathprefix` — swapped to relative paths

## Current State
- **Game title:** Aetherfall (repo: voidnologo/aetherfall)
- **Build:** Eleventy 3.x — `npm run dev` / `npm run build` — deploys via GitHub Action with `--pathprefix=/aetherfall/`
- **Path rule:** use relative paths in new pages, or run absolute paths through the `| url` filter. Raw `/foo` breaks at the subpath.
- **Website:** 18 chapters + quickstart (.njk) + character sheets + interactive tools + `/fiction/` landing + reader
- **Fiction:** 6 world reference docs in `fiction/world/`; Story 02 published as "What the Mill Remembered"; Story 03 planned as "The Lamplighter's Price"
- **Fiction data loader:** `web/_data/fiction.js` — hard-coded to story 02 for now; generalize when story 03 ships
- **Art pipeline:** `art/{type}/{generated|approved|archived}/` — art NEVER deleted, only moved
- **Art generation:** `python tools/comfyui_generate.py` — builds flux-dev workflows, queues via ComfyUI API
- **Founding event:** "The Tear" (was "the Eruption" — renamed session 27)
- **CRITICAL RULE:** Rulebook content must NEVER be changed without explicit user approval.
- **CRITICAL RULE:** Art is NEVER deleted. Moves through generated -> approved or generated -> archived.

## Immediate Next Tasks
- Update series bible with Story 02 outcomes (new NPCs, deadlock site, seeds planted) before writing Story 03
- Write Story 03 chapters from `fiction/stories/story-03/PLAN.md`
- Cross-device reading test of the published fiction reader
- Social preview images (og:image) for /fiction/ landing and story reader
- Review Wave 1 art and select golden reference set

## Key References
- Fiction world docs: `fiction/world/01-the-world.md` through `06-series-bible.md`
- Story 02 plan: `fiction/stories/story-02/PLAN.md`
- Story 02 chapters: `fiction/stories/story-02/ch01.md` through `ch10.md`
- Story 03 plan: `fiction/stories/story-03/PLAN.md`
- Fiction web data: `web/_data/fiction.js`
- Fiction web templates: `web/fiction/index.njk`, `web/fiction/what-the-mill-remembered.njk`
- Fiction styles: `web/fiction/css/fiction.css`
- Style guide: `fiction/world/05-style-guide.md`
- Character sheets (game data): `web/_data/characters/*.json`

## Color Reference
- **Aether:** `#3dc8e0` | **Galvanic:** `#e8a825` | **Background:** `#080b14`
- **Fonts:** Playfair Display (headings), Source Serif 4 (body), Cormorant Garamond (labels)
