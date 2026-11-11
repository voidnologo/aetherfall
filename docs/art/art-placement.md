# Art Placement Standard

## Document Status: ACTIVE — Locked rules
**Last Updated:** 2026-11-10 (Session 39)

`deco-suite-plan.md` §5 sets *how much* art a chapter carries. This file sets *where each piece goes* relative to headings, paragraphs and page breaks. Both apply.

The rules exist because the first art pass placed most pieces at section seams — immediately before a heading, or between a heading and its first paragraph — which reads as decoration separating sections rather than illustration belonging to one.

---

## 1. The four kinds of art

| Kind | Shortcode | Behaviour | Role |
|---|---|---|---|
| **Chapter plate** | `plate … "full"` | Own page in print (`break-before/after: page`) | Frontispiece. Sets the chapter's mood. |
| **Scene plate** | `plate … "half"` | Centered block, `break-inside: avoid` | Illustrates one section. |
| **Floated spot** | `spot … "right"` / `"left"` | Floats, 2.2in; text wraps beside it | Marginal illustration of the passage it sits in. |
| **Centered spot** | `spot … "center"` | Centered block, 1.8in; interrupts the column | Symmetrical or wide subjects — catalogue rows, balance scales, maps. |

A piece's behaviour decides where it may sit. A float and a block placed at the same point in the source produce different pages.

---

## 2. Placement rules

Each rule is marked **[convention]** where a style manual or press guideline backs it, or **[house]** where none does and we are choosing. Sources are listed in §6.

**R1 — Subject governs section. [convention]** A piece sits in the section whose subject it depicts. A piece that surveys a whole chapter belongs in the chapter introduction, never inside one of its subsections. A revolver-and-knife catalogue under *Melee Weapons* tells the reader the section is about guns.

**R2 — Never between a heading and its first content, unless it floats. [convention]** A centered spot or a plate placed there pushes the section's opening text down the page and reads as a caption to the heading. A floated spot may sit there: it moves into the margin and the first paragraph wraps beside it, which is the ordinary way a marginal illustration is set.

**R2b — Never between a colon lead-in and the block it introduces. [house]** A sentence ending in a colon points at the table, list or paragraph directly under it. Art placed in the gap takes the colon for itself: the reader is promised a list and meets a picture, and in print the lead-in can end up on the previous page from the thing it introduces. No manual found addresses this directly; it follows from the IEEE and APSA rule that a figure belongs after the text that refers to it, not inside it. The art goes after the block the sentence introduced.

**R3 — Never immediately before a heading. [house]** No style manual settles this either way, and the LaTeX `placeins` package exists because the opposite problem — floats drifting *past* a section boundary — is the one typesetters usually fight. We rule against it on Bringhurst's vertical-rhythm argument: the art's bottom margin and the heading's top margin stack into a gap that breaks the column. Art with no content after it also reads, to the eye, as belonging to the section that is ending. Mid-chapter art goes *inside* the section it illustrates. Three exceptions. The chapter frontispiece, which sits before the first heading by design. A **full plate**, which `print.css` gives its own page: with no text around it there is nothing for it to be misread as belonging to, and the seam between two sections is exactly where a page break is wanted — putting one mid-section instead splits that section across the plate and costs a page each time. And art followed by a heading one level *deeper*, which opens a subsection of the section the art is already in rather than a sibling, so the art still reads as belonging where it sits.

**R4 — A float needs text to float beside. [convention]** At least two body paragraphs must follow a floated spot before the next heading. Paragraphs inside a callout, a `{% scene %}` or a table do not count: the panel is its own box and the float runs past it. The one numeric authority found is the University of Utah thesis handbook's "at least six consecutive lines of text" beside a figure; two of our paragraphs clears that comfortably. A 2.2in float with one short paragraph beside it runs past the heading and collides with the next section. Where there isn't room: make it `center` and place it after the first paragraph, or move the piece to a section that has the text.

**R4a — A section with fewer than two paragraphs takes centered art, not a float. [house]** Reference chapters are mostly tables and callouts. A float there has nothing to wrap it and runs over the next heading; a centered spot sits between blocks and behaves.

**R4b — A float with a table against it becomes a centered spot. [house]** A table does not wrap a float: it is a block box that sits beside it and loses the width, or clears it and leaves a hole. Where the next block after a float is a table, the piece goes centered instead. This is what the centered spot is for.

**R5 — Alternate float sides. [house]** Consecutive floated spots within a chapter alternate right and left. A chapter whose spots all float right combs the whole page to one margin. No authority requires this, and there is a weak typographic argument the other way — a wrap reads best against a ragged edge, which would favour one consistent side. Our body text is justified, so both edges are flush and that argument does not apply.

**R6 — Two content blocks minimum between any two pieces. [house]** A paragraph, a table, a callout or a heading all count as separation. Floats that start within each other's height overlap.

**R7 — Full plates fall at section boundaries, introducing the section they illustrate. [house]** `plate-full` takes its own page and forces the next element onto a fresh one, so put it where a page break helps the reader: the chapter front, or after the closing paragraph of a major section. Never inside a worked example, a run of tables, or a numbered procedure — it splits the thing the reader is following.

**R8 — Never inside a table, callout or paired shortcode. [convention]** Never inside a table, callout, `{% scene %}`, `{% gmnote %}`, `{% handler %}`, stat block or other paired shortcode. Art goes between blocks, never within one.

**R9 — Captions. [convention]** Plates carry a caption; it names the place or the moment. Spots carry none — they are marginalia, and a caption makes a margin drawing look like a figure the text should have referenced. This matches the split the manuals draw: art the text points at by number gets a number and a caption; decorative art gets neither, and carries its description in alt text instead. The `spot` shortcode has no caption parameter, which enforces it.

**R10 — Order of preference for a new piece. [convention]** After the paragraph that first mentions its subject → after the section's first paragraph → at the section's end if nothing else fits. Never before the section's heading.

---

## 3. Chapter front matter order

A chapter's opening is fixed, so every chapter starts the same way:

1. `<p class="flavor">` — the epigraph
2. `{% handler %}` callout, where the chapter has one
3. Body paragraphs of the introduction
4. **Chapter plate** (`full`)
5. First section heading

The frontispiece comes after the introduction rather than before it so the reader meets the chapter's argument before its mood piece, and so the drop cap lands on real text.

---

## 4. Checking a chapter

A placement is wrong if any of these is true:

- There is no content at all between the art and the next heading, and it is not the chapter frontispiece.
- It is a centered spot or a plate, and there is no body text between the heading above and the art.
- Fewer than two body paragraphs follow a floated spot before the next heading, counting body text only.
- It sits between a sentence ending in a colon and the block that sentence introduces.
- It floats and the next block under it is a table.
- The subject does not appear in the section it sits in.
- Two pieces sit within two paragraphs of each other.
- It sits inside a table, callout or paired shortcode.

`tools/art_lint.py` checks all of these except the subject match, which needs a reader: a piece can sit in a structurally perfect position and still illustrate the wrong thing. The Thornfield Communion plate passed every mechanical check from inside a section about offshore islands. Run the linter before an art change merges, and read the caption against the heading above it yourself.

---

## 5. Known gaps in the print pipeline

Found while writing this standard; not fixed here, and worth a session of their own:

- **`.plate-full` uses `break-before: page`.** The recorded intent (`deco-suite-plan.md` §6) is that a plate *faces* a chapter opener, which needs `break-before: verso` (or `left`) plus a `@page :blank` rule to strip running heads from the pages a side-specific break skips. `page` cannot choose a side of the spread.
- **Print spots carry no `break-inside` or `clear`.** They are plain floats. WeasyPrint has handled float fragmentation since v54, but the build pins no version — `scripts/build-pdf.py` falls back to whatever `uvx` resolves.
- **`break-inside: avoid` is advisory.** CSS Fragmentation §4.4 drops the avoid rules, together, when a span has no legal break point. `h2 { break-after: avoid }` followed directly by a figure with `break-inside: avoid` creates such a span, so a tall figure can stran its heading at a page foot *and* split anyway. Keep the avoid-chain to one adjacency and size figures to fit.
- **`.section-divider` has no break property**, so it can land at the head or foot of a page.

## 6. Sources

- IEEE Editorial Style Manual for Authors, §II.F — figures sit "as close to their first mention as possible, but preferably after the mention."
- Chicago Manual of Style §3.8 (placement relative to text), §3.13 (working numbers for unnumbered illustrations), §3.21 (captions). CMOS Shop Talk: the tolerance is the page, not the paragraph.
- APSA Style Manual — placement "should not precede where they are mentioned in the text."
- University of Utah Graduate School thesis handbook — a figure "is never placed in the middle of a page between two paragraphs"; it begins or ends the page and carries "at least six consecutive lines of text."
- NDSU Center for Writers — "non-text items should not immediately follow after a heading," because the item would not have been referenced yet.
- Bringhurst, *The Elements of Typographic Style* §2.2.2 — vertical space from headings, illustrations and captions should resolve to the baseline rhythm.
- University Press of Mississippi; Getty Quire — decorative art carries no caption but does carry alt text.
- Princeton UP; Edinburgh UP — plates are numbered separately from in-text figures.
- Clayton Notestine, Explorer's Design, on *Brindlewood Bay* and *Mörk Borg* — full-page art on the verso facing a recto chapter opener, as a navigation aid.
- CSS Fragmentation Module Level 3 §3.1, §4.4; CSS Paged Media Level 3 §4.2.3 — break properties, their advisory nature, and `:blank`.
