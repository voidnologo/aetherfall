# Session 31: Fiction Landing + Reader — Story 02 Published to Web

**Date:** 2026-04-17
**Goal:** Title Story 02, build a mobile-optimized web reader for it, and wire the fiction into the site navigation

## Overview

Took Story 02 from markdown drafts in `fiction/stories/story-02/` and published it as a polished, mobile-first web experience at `/fiction/`. Two things the rulebook doesn't need but fiction does: a compact column width for long-form reading, and a chapter table of contents that gets out of the way.

Built a `_data/fiction.js` loader that reads the raw chapter markdown, renders it through markdown-it, and surfaces it to Nunjucks templates with POV metadata per chapter. Two new pages: `/fiction/` (landing with story card) and `/fiction/what-the-mill-remembered.html` (the full reader). Shared styles live in `/fiction/css/fiction.css` — independent from the rulebook's styles, tuned for reading rather than reference.

Wired the fiction into the rest of the site: hero button on the landing, end-of-page CTA on the landing, persistent link in the rulebook sidebar footer, and a CTA block at the end of the last rulebook chapter. Caught and fixed a subpath deployment bug (absolute `/...` paths don't get the Eleventy pathprefix applied — they need to be either relative or filtered through `| url`).

---

## Changes Made

### Story 02 Titled
- Title: **"What the Mill Remembered"** — A Tale of the Ash & Veil Society
- Literary register (Wellsian, quiet), fits the recognition-horror theme of the story

### Fiction Data Loader (`web/_data/fiction.js`)
- Reads all 10 chapter markdown files at build time
- Strips `# Chapter N` top-of-file headings (chapter heading is synthesized by the template)
- Renders remaining prose through markdown-it (paragraphs, `---` scene breaks, `*italics*`, `**bold**`)
- Attaches POV per chapter (Mira/Kael/Sera/Aldric rotation)
- Pre-computes `numberDisplay`, `wordsDisplay`, `readMinutes` etc. in the data layer so templates stay simple
- Exposes `fiction.stories` (array) and `fiction.storiesBySlug` (lookup map)

### Fiction Landing (`web/fiction/index.njk`)
- Top nav bar: ← Aetherfall (home) | The Rules → (with subtle alt styling)
- Wordmark graphic header (not plain text) with "FICTION" tracked-caps subtitle
- Single story card with blurb and "Begin Reading →" CTA
- Stats line (chapters / words / read time) intentionally removed — not useful or interesting for readers

### Story Reader (`web/fiction/what-the-mill-remembered.njk`)
- Sticky top bar (48px min, tap-friendly): TOC toggle + Fiction back-link | monogram + No. 02
- Thin scroll-progress line under the sticky bar (filled with aether→aether-dim gradient)
- Title block: Story No. 02 / Title / Subtitle — no stats
- Chapters iterated from data, each with heading (label + big numeral + POV badge) and prose body
- First paragraph of every chapter gets a drop cap (aether-colored, with subtle glow)
- `<hr>` scene breaks render as centered `• • •` ornaments via CSS pseudo-element
- End-of-story block: "The End" mark, aether gem, closing note, buttons to More Fiction / The Rules
- `scroll-margin-top` on chapter sections so anchor jumps clear the sticky bar

### Collapsible Chapter TOC
- Hamburger toggle in sticky bar opens a left-side drawer (slide-in transform)
- Drawer width: `min(86vw, 340px)` — generous on mobile, capped on desktop
- Each TOC item: padded number / Chapter N / POV sub-label
- First item: "Title Page" (anchors to `#top`). Last item: "The End" (anchors to `#story-end`)
- Active chapter highlighted with aether accent + left border + tinted background
- Scroll-spy: deterministic algorithm (picks deepest section whose top has crossed a 22%-viewport anchor line). Tried IntersectionObserver first but had edge-case misfires on anchor jumps; scroll-based is simpler and reliable.
- Close behaviors: tap TOC item, tap backdrop, tap close button, press Escape
- Body `overflow: hidden` while drawer open (no scroll bleed-through)

### Mobile-First Reading CSS (`web/fiction/css/fiction.css`)
- Independent stylesheet from rulebook — tuned for long-form reading
- Reading column: `max-width: 34rem` (~544px, ~66ch) — narrow enough to scan comfortably
- Base font: 17px on mobile, scaling up to 19px at wide viewports
- Body: Source Serif 4, `line-height: 1.8`, `hyphens: auto`
- Reduced drop cap size on narrow screens
- Respect `prefers-reduced-motion`

### Wiring Fiction Into the Site
- `web/index.html`: added "Read the Fiction" button to hero CTA and final CTA section
- `web/_includes/chapter.njk`: added "Read the Fiction →" link below "← Back to Aetherfall" in the rulebook sidebar footer (present on every rulebook page)
- `web/rules/css/styles.css`: `.sidebar-footer` set to `flex-direction: column` with gap so two links stack cleanly
- `web/rules/gm-tools.njk`: added a "Step Into the World" scene callout at the end of the last rulebook chapter, linking to /fiction/

### Subpath Deployment Fix
- Initial deploy to `voidnologo.com/aetherfall/` broke — CSS and images 404'd
- Root cause: fiction pages used absolute `/...` paths. Eleventy's `--pathprefix=/aetherfall/` only prepends the prefix to URLs that go through the `| url` filter. Raw `/foo` in HTML stays as `/foo` at serve time and resolves to domain root, not the subpath.
- Rulebook escapes this because `chapter.njk` uses either relative paths (`css/styles.css`) or the filter (`{{ '/assets/…' | url }}`)
- Fix: swapped all absolute `/...` paths in fiction pages to relative (`../assets/…`, `css/fiction.css`, `./`, `../rules/` etc.). Works at root deploy and at any subpath.
- Verified by serving `_site/` under `/aetherfall/` locally and running Playwright against it — all links, CSS, images, and nav destinations resolve correctly.

### Package Dependency
- `markdown-it` promoted from transitive (via eleventy) to a declared devDependency in `package.json` — avoids brittle transitive requires.

---

## Files Modified

| File | Change |
|------|--------|
| `web/_data/fiction.js` | New — loads story-02 markdown, renders chapters, exposes fiction data to templates |
| `web/fiction/index.njk` | New — fiction landing page with wordmark header and story card |
| `web/fiction/what-the-mill-remembered.njk` | New — reader page: sticky bar, TOC drawer, titleblock, 10 chapter sections, end block, scroll-spy JS |
| `web/fiction/css/fiction.css` | New — reading-optimized stylesheet (column, drop caps, scene-break ornaments, TOC drawer) |
| `eleventy.config.js` | Added passthrough for `web/fiction/css` |
| `web/index.html` | Added "Read the Fiction" hero button and final CTA button |
| `web/_includes/chapter.njk` | Added "Read the Fiction →" link in sidebar footer (every rulebook page) |
| `web/rules/css/styles.css` | `.sidebar-footer` now flex-column with gap so two links stack |
| `web/rules/gm-tools.njk` | Added "Step Into the World" CTA callout at end of last rulebook chapter |
| `package.json` | Declared `markdown-it ^14.1.0` as direct devDependency |
| `package-lock.json` | Updated to reflect markdown-it as a root dep |

## Key Design Decisions

- **Single-page reader, all chapters on one scroll** — rather than per-chapter pages. A 22k-word short story is meant to be read top-to-bottom; pagination adds clicks without value. Anchor-based TOC gives jump-to navigation when wanted.
- **No read-time / word-count stats displayed** — tempted to show them (signal of scope), but they frame the work as a task to complete rather than something to enjoy. The card blurb already sets expectations.
- **Drop caps per chapter, not just at story open** — each chapter is a fresh POV; the drop cap visually marks the voice shift. Cheap, effective period-appropriate signal.
- **Scroll-based scroll-spy instead of IntersectionObserver** — IO's ratio-based detection misfires on anchor jumps when two adjacent sections straddle the threshold band. A deterministic "deepest section whose top has crossed the anchor line" check is simpler to reason about and always picks the expected section.
- **Separate fiction.css from rulebook styles.css** — rulebook CSS is tuned for reference (wider column, denser callouts, two-force color themes). Fiction wants narrow columns, one palette, reading-first typography. Merging would compromise both.
- **Relative paths everywhere, not pathPrefix-via-filter** — the rulebook uses `| url` filter mixed with relative paths. Pure relative is simpler, harder to break, and works at any deploy path. Fewer moving pieces.
- **TOC drawer is overlay on all viewports** — considered making it persistent at desktop widths (like the rulebook's sidebar). Decided against: fiction is meant to be immersive, not navigated. The drawer is there when you want it, absent when you don't.

## Open Issues

- Story 02's chapter files still have no frontmatter and no chapter titles (just `# Chapter N`). Template synthesizes chapter headings from data. If we later want titled chapters, we'd need to either add frontmatter or maintain titles in `fiction.js`.
- No favicon / social preview image specific to the fiction section — currently uses the site-wide favicon and no og:image.
- The reader page and the landing both load the same three Google Fonts. Once we add more stories, consider consolidating font declarations or self-hosting.
- The fiction data loader is hard-coded to story 02. Generalizing to an array-of-stories pattern should happen when story 03 starts (not before — premature abstraction).
- No reader-side controls (font size adjustment, light theme toggle). Might be worth adding once we have user feedback.

## Next Session

- Consider a second short story — either continuing Ash & Veil or a standalone in a different zone
- Social preview images (og:image) for /fiction/ landing and the story reader
- Review Wave 1 art selection — still outstanding from session 30
- Run a cross-device reading test on the published reader (iPhone, iPad, desktop) for any remaining visual or tap-target issues
