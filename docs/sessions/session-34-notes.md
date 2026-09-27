# Session 34: Consistency Review, Canon Lock & Deco Lithograph Art Direction

**Date:** 2026-09-26
**Goal:** Full consistency review of game/fiction/design docs with the new model; clean up web + print PDF output; propose a distinct art style (several directions), discuss, then prototype samples in ComfyUI for approval ahead of a full art suite (chapter borders, header art, in-page illustrations).

## Overview

First session on Opus 5.5. Started with a full consistency read of the design docs, the built web rulebook, the pregen data, the fiction world docs, the series bible, and the Stories 02–03 spell usage. Then inspected the web and PDF output visually and proposed art directions.

- Consistency review written to `docs/reviews/2026-09-26-consistency-review.md`: 6 canon conflicts, 17 published-rule contradictions, 12 quickstart/pregen errors, fiction/bible drift, design-doc drift. **No rulebook content changed**; awaiting approval.
- Art direction proposals written to `docs/art/art-direction-proposals.md`: five directions (A Engraver's Folio, B Two Inks [recommended], C Woodcut Noir, D Deco Lithograph, E Scholar's Field Journal).

---

## Changes Made

### Build / output fixes (no content changes)
- WeasyPrint installed (`uv tool install weasyprint`); `scripts/build-pdf.py` falls back to `uvx` if absent.
- PDF printed raw Mermaid source for both Quick Reference flowcharts. `build-pdf.py` now pre-renders them via mermaid-cli (system chromium, neutral theme) to `print/diagrams/`; `.print-diagram` styles added to `print.css`.
- `.claude/skills/session-start` description updated from the old "Adventure" project name.

---

### Rulebook fixes (approved)
Kael Dunn made canonical across all rules examples (creating chapter rebuilt; alley combat example rewritten); timeline fixes; ~100 mechanical fixes across 14 chapters + quickstart + pregens; crit range locked (66 → 64–66); rounds → counts (1 round = 3 counts). Details in the review's Resolution Status and `docs/requirements/CANON_DECISIONS.md`.

### Art prototypes, round 1
24 images (A/B/D × header/frame/spot/portrait × 2 shared seeds) via `tools/prototype_styles.py`. Comparison page: https://claude.ai/artifact/KLMQwvngArrLWZpTzRGHhL. The runner was killed mid-batch by Claude Code's low-memory reaper; ComfyUI finished the queue and the outputs were collected via the history API.

## Files Modified

| File | Change |
|------|--------|
| `docs/reviews/2026-09-26-consistency-review.md` | New: full consistency review |
| `docs/art/art-direction-proposals.md` | New: five art directions + prototype plan |
| `scripts/build-pdf.py` | uvx fallback, Mermaid pre-render |
| `web/rules/css/print.css` | `.print-diagram` styles |
| `.claude/skills/session-start/SKILL.md` | Description fix |

## Key Design Decisions

- **Deco Lithograph over pen & ink:** it reads strongest, bridges the painted brand, and flat shapes stay consistent across generations. The Two Inks color rule (cyan = Aether, amber = Engine) carries over so every picture shows the balance.
- **Fiction is canon for the characters;** the pregens and rules follow it. Kael Dunn is the only Kael.
- **Skin tone is ambiguous by design;** the world isn't Earth, so real-world analogs are only reader shortcuts.
- **ComfyUI holds ~19 GB of RAM** and Claude Code reaps idle background shells, so use `/free`, then `--queue-only`, then `--collect`, with no waiters.

### Later in session (after the notes above)
- User chose **Direction D**; round 2 produced the leads, theme frames, and watermark. Approved: Kael 2439444224, Sera 3194702273, Aldric 3394774571, Mira 2096254533 + 4036712205, frames aether 131618214 / galvanic 1166265576 / split 2427297017 / neutral 1553240695, watermark 3200761920, Two Inks frame 3867070072 (PDF front matter). Everything else archived.
- Wired in: web chapter-hero crowns, PDF full-page chapter openers, Two Inks title and table-of-contents pages, and the original sheet watermark (third-party web copies removed).
- Canon additions: crit rule (66 → 64–66); 1 round = 3 counts; Sera = Aetheric + Transmutation; pregen Society stays The Ashwick Charter; skin tone unspecified; not-Earth rule.
- Pipeline fix: `--collect` had re-copied filed art; it now skips anything already filed (43 identical duplicates removed, log deduped).

## Open Issues

- Name collisions; Quick Reload rounding; Mira's reference image not yet designated; art needs upscaling for print; pushes to `main` bypass the PR rule; series bible needs Story 03 outcomes; design-doc drift (Tier 5).

## Next Session

Try out the artwork: portraits in the quickstart pregens and character sheets, review the frames and watermark in the browser and PDF, then plan the next Deco art suite.
