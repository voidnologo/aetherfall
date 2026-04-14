# Art Direction — Aetherfall

This document covers **project-specific art needs** — logo, web assets, and integration plans. For the full visual identity, prompt engineering, and generation pipeline, see:

- `docs/art/style-guide.md` — Master visual identity (pen & ink, B&W, Art Nouveau/Deco)
- `docs/art/consistency-rules.md` — Enforcement rules, quality checklist, generation logging
- `docs/art/prompt-engineering/prompt-templates.md` — Reusable prompt structures
- `docs/art/prompt-engineering/negative-prompts.md` — Avoidance guide
- `docs/art/prompt-engineering/generation-settings.md` — Model/LoRA/parameter configs

---

## 1. Logo Design Brief

### Context

The logo is a **special case** in the art system. The interior art is black-and-white pen & ink (per the style guide). The logo uses the **brand colors** (Aether cyan + Galvanic amber) and is typographic rather than illustrative. However, it should feel like it belongs in the same visual world — the Art Deco/Art Nouveau tension, the 1920s industrial-meets-arcane aesthetic, the sense of two forces in balance.

### The Duality

The game's core tension is Aetheric vs. Galvanic — magic vs. technology. The logo should express this tension visually. Not one side winning — the balance between them.

### Color Palette

| Token | Hex | Role |
|-------|-----|------|
| Aether | `#3dc8e0` | Cyan/teal — magic, mystery, cool |
| Galvanic | `#e8a825` | Amber/gold — technology, industry, warm |
| Background | `#080b14` | Deep void black (web dark theme) |
| Text bright | `#eef0f5` | Light text on dark |
| Text dim | `#8a92a4` | Secondary text |

### Typography Reference

The web rulebook uses:
- **Playfair Display** — serif, headings (elegant, editorial)
- **Source Serif 4** — body text (readable, warm)
- **Cormorant Garamond** — labels and small caps (refined, classical)

The logo can use custom lettering but should harmonize with these typefaces.

### Tone

- Serious but not grim
- Elegant but not precious
- Industrial but not steampunk-cliché (no gears-on-everything)
- Mysterious but not horror
- "Aetherfall" is evocative — the Aether _fell_, like rain, like a collapse, like something that changed everything

### What the Logo Should NOT Be

- Generic fantasy (swords, dragons, shields)
- Pure steampunk (cogs, goggles, brass everything)
- Horror/dark (skulls, blood, grimdark)
- Overly complex (must read at 32px)
- A literal illustration — it's a wordmark/logotype with optional iconography

### Exploration Directions

**Direction A: Split Wordmark**
"AETHERFALL" in Art Deco lettering, with a visual split or gradient — the left side trending Aether (cool, flowing, ethereal) and the right side trending Galvanic (warm, structured, industrial). The transition point is the tension.

**Direction B: Monogram + Wordmark**
A stylized "A" or "AF" monogram embodying the duality (one half magical, one half mechanical), paired with "AETHERFALL" below. The monogram doubles as a favicon.

**Direction C: The Fall**
"AETHERFALL" with letters subtly descending or fracturing — evoking the moment the Aether fell. Particles or energy fragments drifting from the text. Restrained, not chaotic.

**Direction D: Sigil**
A circular or shield-shaped emblem containing both Aetheric and Galvanic symbols in tension. "AETHERFALL" arcs around or sits below. Works as a stamp, seal, or badge.

### Deliverables

1. **Primary logo** — Full wordmark, horizontal, for web header and landing page
2. **Icon/monogram** — Square, works at 32px (favicon) and 512px (app icon)
3. **Print variant** — Single-color (black on white) for character sheets and print
4. **Dark background variant** — For the site (`#080b14` background)
5. **Light background variant** — For print (white background)

### Format Requirements

- SVG preferred (scalable, can be themed with CSS)
- PNG fallbacks at 1x and 2x for web
- Favicon: ICO or PNG at 32x32 and 180x180 (Apple touch icon)

---

## 2. Logo Prompt Template

Follows the structure from `docs/art/prompt-engineering/prompt-templates.md` but adapted for logo/typographic design rather than pen & ink illustration.

### Style Prefix (Logo-Specific)

```
Art Deco logotype design. Elegant typographic wordmark with 1920s
industrial and arcane influences. Clean vector-quality rendering
suitable for logo use. Dual-tone color scheme: cyan (#3dc8e0) and
amber (#e8a825) on dark background (#080b14).
```

### Template: Wordmark Logo

```
[LOGO STYLE PREFIX]

The word "AETHERFALL" rendered as an Art Deco wordmark. Strong
geometric letterforms inspired by Playfair Display serif typography.
[Direction-specific: visual split between cool cyan left side and
warm amber right side / descending fracture effect / etc.]

The lettering conveys tension between organic flowing energy and
angular industrial precision. Subtle decorative elements: [fine
lines, geometric accents, faint energy particles, Art Deco
sunburst motifs — choose one, keep restrained].

Horizontal layout, dark background (#080b14). The word is the
primary element. Any decorative elements are subordinate to
readability. Must work at small scale.

Clean, sharp, professional logotype. Not an illustration — a
wordmark. Minimal ornamentation. The tension between the two
visual languages IS the design.
```

### Template: Monogram/Icon

```
[LOGO STYLE PREFIX]

A stylized letter "A" monogram for the game "Aetherfall." The
letterform is split or blended between two visual languages:
one side organic and flowing (representing magical Aether,
rendered in cyan #3dc8e0), the other side geometric and
angular (representing industrial technology, rendered in
amber #e8a825).

Square composition, centered. Works as a favicon at 32px and
an app icon at 512px. Simple enough to read at small scale,
detailed enough to reward inspection at large scale. Dark
background (#080b14).

Minimal — this is an icon, not an illustration. Clean edges,
strong contrast, geometric precision.
```

### Avoidance (Logo-Specific)

- No photorealistic elements or textures
- No illustration (characters, creatures, scenes)
- No steampunk clichés (gears, cogs, goggles)
- No generic fantasy symbols (swords, shields, dragons)
- No 3D effects, drop shadows, or bevels
- No busy backgrounds or patterns
- Keep it flat, clean, scalable

---

## 3. Integration Plan (After Logo Approval)

Once a logo is approved:

1. **Web header** — Replace text "Aetherfall" in `.header-logo` with SVG logo
2. **Landing page** — Replace text title in hero section with logo
3. **Character sheets** — Add monochrome logo to header area of `sheet.njk`
4. **Favicon** — Add to `web/` root and reference in chapter.njk `<head>`
5. **Sidebar** — Replace text "Aetherfall" in `.sidebar-title` with logo or icon
6. **Print** — Monochrome variant in character sheet header

---

## 4. Future Art Priorities (After Logo)

Ordered by impact on the published rulebook:

1. **Character sheet watermark** — Faint background art for the sheet template
2. **Chapter header decorative borders** — Art Deco/Nouveau frames for chapter openings
3. **Pre-gen character portraits** — Kael, Sera, Aldric, Mira (for quickstart adventure)
4. **Spot illustrations** — 3-5 key concepts (casting, combat, zone effects, exotics)
5. **Landing page hero image** — Atmospheric scene for the site front page
6. **Full-page plates** — Chapter openers (highest effort, most impactful)

These follow the existing art pipeline phases in `docs/art/prompt-engineering/generation-settings.md` §Batch Generation Strategy.
