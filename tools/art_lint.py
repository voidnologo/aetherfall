#!/usr/bin/env python3
"""Check art placement in the rulebook chapters against docs/art/art-placement.md.

Run with no arguments to check every chapter:

    python3 tools/art_lint.py

Exit status is 1 if any placement breaks a rule, so this can gate a merge.
"""

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RULES_DIR = ROOT / "web" / "rules"

ART = re.compile(r'\{%\s*(spot|plate)\s+"([a-z0-9-]+)"(.*?)%\}', re.S)
HEADING = re.compile(r"<(h[1-6])\b[^>]*>(.*?)</\1>", re.S)
PARAGRAPH = re.compile(r"^\s*<p[\s>]")
# Paired shortcodes and block containers that art must never sit inside.
BLOCK_OPEN = re.compile(r"\{%\s*(scene|gmnote|handler|warning|example|sidebar)\b")
BLOCK_CLOSE = re.compile(r"\{%\s*end(scene|gmnote|handler|warning|example|sidebar)\s*%\}")
TABLE_OPEN = re.compile(r"<table\b")
TABLE_CLOSE = re.compile(r"</table>")

MIN_PARAGRAPHS_BESIDE_FLOAT = 2
MIN_PARAGRAPHS_BETWEEN_ART = 2


class Placement:
    """One {% spot %} or {% plate %} call and the structure around it."""

    def __init__(self, line_no, kind, name, qualifier):
        self.line_no = line_no
        self.kind = kind
        self.name = name
        self.qualifier = qualifier
        self.heading_above = None
        self.heading_below = None
        self.paragraphs_above = 0
        self.paragraphs_below = 0
        self.inside_block = False
        self.blocks_below = 0
        self.blocks_above = 0
        self.gap_to_previous_art = None

    @property
    def floats(self):
        return self.kind == "spot" and self.qualifier in ("right", "left")

    @property
    def takes_own_page(self):
        """A full plate is given its own page by print.css, so it has no
        neighbouring text to be misread as belonging to."""
        return self.kind == "plate" and self.qualifier == "full"

    @property
    def is_frontispiece(self):
        """Any art in the chapter's front matter, above the first heading.

        There is no preceding section for it to be mistaken for, so R3 does not
        apply: it reads as the chapter's opening image, which is its job."""
        return self.heading_above is None

    def __str__(self):
        return f"{self.kind} {self.name!r} ({self.qualifier}) at line {self.line_no}"


def qualifier_for(kind, raw_args):
    """The last quoted keyword decides size for a plate and side for a spot."""
    found = re.findall(r'"(full|half|left|right|center)"', raw_args)
    if found:
        return found[-1]
    return "half" if kind == "plate" else "right"


def parse_chapter(path):
    """Walk a chapter once, recording each art call with the structure around it."""
    lines = path.read_text().splitlines()
    placements = []
    heading_above = None
    paragraphs_since_marker = 0
    block_depth = 0
    in_table = False
    last_art_index = None
    blocks_since_marker = 0

    for index, line in enumerate(lines):
        if TABLE_OPEN.search(line):
            in_table = True
        if TABLE_CLOSE.search(line):
            in_table = False
        if BLOCK_OPEN.search(line):
            block_depth += 1
        if BLOCK_CLOSE.search(line):
            block_depth = max(0, block_depth - 1)

        heading_match = HEADING.search(line)
        if heading_match:
            heading_above = (heading_match.group(1), strip_tags(heading_match.group(2)))
            paragraphs_since_marker = 0
            blocks_since_marker = 0
            continue

        if PARAGRAPH.match(line) and block_depth == 0 and not in_table:
            paragraphs_since_marker += 1
            blocks_since_marker += 1
        if TABLE_OPEN.search(line) or BLOCK_OPEN.search(line):
            blocks_since_marker += 1

        art_match = ART.search(line)
        if not art_match:
            continue

        placement = Placement(
            index + 1,
            art_match.group(1),
            art_match.group(2),
            qualifier_for(art_match.group(1), art_match.group(3)),
        )
        placement.heading_above = heading_above
        placement.paragraphs_above = paragraphs_since_marker
        placement.blocks_above = blocks_since_marker
        placement.inside_block = block_depth > 0 or in_table
        if last_art_index is not None:
            placement.gap_to_previous_art = count_blocks(lines, last_art_index + 1, index)
        placements.append(placement)
        last_art_index = index
        paragraphs_since_marker = 0
        blocks_since_marker = 0

    attach_following_context(lines, placements)
    return placements


def attach_following_context(lines, placements):
    """Fill in the heading that follows each placement and the text before it."""
    for placement in placements:
        start = placement.line_no
        for index in range(start, len(lines)):
            heading_match = HEADING.search(lines[index])
            if heading_match:
                placement.heading_below = (
                    heading_match.group(1),
                    strip_tags(heading_match.group(2)),
                )
                placement.paragraphs_below = count_paragraphs(lines, start, index)
                placement.blocks_below = count_blocks(lines, start, index)
                break
        else:
            placement.paragraphs_below = count_paragraphs(lines, start, len(lines))
            placement.blocks_below = count_blocks(lines, start, len(lines))


def count_paragraphs(lines, start, end):
    return sum(1 for line in lines[start:end] if PARAGRAPH.match(line))


def count_blocks(lines, start, end):
    """Content blocks between two points: paragraphs, tables and callouts.

    R6 guards against art stacking with nothing in between. A table or a callout
    separates two pieces just as well as a paragraph does, so all three count."""
    blocks = 0
    depth = 0
    for line in lines[start:end]:
        if TABLE_OPEN.search(line) or BLOCK_OPEN.search(line):
            blocks += 1
            depth += 1
            continue
        if TABLE_CLOSE.search(line) or BLOCK_CLOSE.search(line):
            depth = max(0, depth - 1)
            continue
        if HEADING.search(line):
            blocks += 1
            continue
        if PARAGRAPH.match(line) and depth == 0:
            blocks += 1
    return blocks


def strip_tags(text):
    return re.sub(r"<[^>]*>", "", text).strip()


def check(placement):
    """Return the rule violations for one placement, as (rule, message) pairs."""
    problems = []
    if placement.inside_block:
        problems.append(("R8", "sits inside a table or paired shortcode"))

    # A heading one level deeper opens a subsection of the section the art is
    # already in, so the art is not orphaned ahead of a sibling: it still reads
    # as belonging where it sits.
    opens_subsection = (
        placement.heading_above is not None
        and placement.heading_below is not None
        and placement.heading_below[0] > placement.heading_above[0]
    )
    orphaned = (
        placement.heading_below
        and placement.blocks_below == 0
        and not placement.is_frontispiece
        and not opens_subsection
        and not placement.takes_own_page
    )
    if orphaned:
        problems.append(
            ("R3", f"nothing between it and the next heading, {placement.heading_below[1]!r}")
        )

    splits_heading = (
        placement.heading_above is not None
        and placement.blocks_above == 0
        and not placement.floats
    )
    if splits_heading:
        problems.append(
            ("R2", f"block art between {placement.heading_above[1]!r} and its first content")
        )

    short_of_text = (
        placement.floats
        and placement.heading_below
        and placement.paragraphs_below < MIN_PARAGRAPHS_BESIDE_FLOAT
    )
    if short_of_text:
        problems.append(
            ("R4", f"only {placement.paragraphs_below} paragraph(s) beside a float before the next heading")
        )

    crowded = (
        placement.gap_to_previous_art is not None
        and placement.gap_to_previous_art < MIN_PARAGRAPHS_BETWEEN_ART
    )
    if crowded:
        problems.append(
            ("R6", f"only {placement.gap_to_previous_art} content block(s) since the previous piece")
        )

    return problems


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="*", help="chapter files (default: every chapter)")
    parser.add_argument("--quiet", action="store_true", help="only print the summary")
    args = parser.parse_args()

    paths = [Path(f) for f in args.files] or sorted(RULES_DIR.glob("*.njk"))
    total_art = 0
    total_problems = 0

    for path in paths:
        placements = parse_chapter(path)
        if not placements:
            continue
        total_art += len(placements)
        reported = []
        for placement in placements:
            problems = check(placement)
            total_problems += len(problems)
            if problems:
                reported.append((placement, problems))
        if reported and not args.quiet:
            print(f"\n{path.name}")
            for placement, problems in reported:
                print(f"  {placement}")
                for rule, message in problems:
                    print(f"      {rule}: {message}")

    print(f"\n{total_art} placements checked, {total_problems} rule violation(s).")
    return 1 if total_problems else 0


if __name__ == "__main__":
    sys.exit(main())
