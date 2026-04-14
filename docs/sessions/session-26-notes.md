# Session 26: Rules Site Wordmark & Branding Update

**Date:** 2026-04-14
**Goal:** Update the web rules site to use the new wordmark and match the landing page branding

## Overview

Updated branding across the rules site and character sheets. Replaced monogram with wordmark in sidebar, generated proper favicon files, renamed Chapter 01, and gave the character sheets an art deco visual overhaul with the wordmark and fantasy watermark.

---

## Changes Made

### Rules Site Branding
- Sidebar: replaced monogram with full wordmark (200px wide, cyan glow)
- Header: kept monogram + "Aetherfall RPG" text (wordmark too small at header height)
- Fixed asset paths from relative to absolute (`/assets/logo/...`) — they were silently broken before
- Generated proper `favicon.ico` (32x32) and `apple-touch-icon.png` (180x180) from monogram
- Updated both rules template and landing page to use new favicon files

### Chapter 01 Rename
- "Welcome to the Age of Wonder" renamed to "Welcome to Aetherfall" (conflicts with video game title)

### Character Sheet Art Deco Overhaul
- Replaced Arial/Segoe UI with Playfair Display (headings) and Cormorant Garamond (body)
- Art deco styling: uppercase letter-spaced section titles, sharp geometric corners, double-line page borders
- Added wordmark at top of page 1 (centered, 3in wide, `filter: brightness(0)` for B&W print)
- Added fantasy.jpg watermark (full page height, 6% opacity, 5% on print)
- Upscaled fantasy.jpg from 382x600 to 2400x3770 for print resolution
- Warm parchment tones on reference boxes

---

## Files Modified

| File | Change |
|------|--------|
| `web/_includes/chapter.njk` | Sidebar wordmark, header monogram, absolute asset paths, new favicon |
| `web/_includes/sheet.njk` | Art deco styling, wordmark, watermark, font overhaul |
| `web/rules/css/styles.css` | Sidebar logo sizing for wordmark, header logo restored |
| `web/_data/pages.json` | Ch01 title: "Welcome to Aetherfall" |
| `web/index.html` | Updated favicon references |
| `eleventy.config.js` | (unchanged, passthrough already covers assets) |
| `web/assets/logo/favicon.ico` | New 32x32 favicon from monogram |
| `web/assets/logo/apple-touch-icon.png` | New 180x180 touch icon from monogram |
| `web/assets/logo/wordmark-dark.png` | Dark wordmark variant (experimental, unused) |
| `web/assets/art/fantasy.jpg` | Upscaled fantasy watermark for sheets |

## Key Design Decisions

- Header keeps monogram+text, sidebar gets wordmark — wordmark is too detailed for 28px header height
- Character sheet wordmark uses CSS `filter: brightness(0)` for B&W print rather than a separate dark image file
- Dark banner approach rejected — sheets are primarily for B&W printing
- Fantasy watermark covers full page height at very low opacity to not interfere with content

## Open Issues

- Character sheet content still flows over/under watermark bottom decorations (text wrapping around them not yet implemented)
- Embossed "A" design still pending revisit
- Character sheet art/watermarks could use further iteration

## Next Session
