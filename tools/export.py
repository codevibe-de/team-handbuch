"""Print tag and type statistics of the handbook notes as Markdown or CSV.

Usage: uv run tools/export.py [csv]
"""

import sys
from collections import Counter
from pathlib import Path

NOTES_DIR = Path(__file__).resolve().parent.parent / "notes"


def read_frontmatter(text: str) -> dict[str, str]:
    """Return the top-level `key: value` pairs of a note's frontmatter."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    fields = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        key, sep, value = line.partition(":")
        if sep and not line.startswith((" ", "-")):
            fields[key.strip()] = value.strip()
    return fields


def parse_inline_list(value: str) -> list[str]:
    """Parse a YAML inline list like `[a, b]` into its items."""
    items = value.strip().removeprefix("[").removesuffix("]").split(",")
    return [item.strip() for item in items if item.strip()]


def collect(notes_dir: Path) -> tuple[Counter, Counter, int]:
    tags, types = Counter(), Counter()
    notes = sorted(notes_dir.glob("*.md"))
    for note in notes:
        fields = read_frontmatter(note.read_text(encoding="utf-8"))
        tags.update(parse_inline_list(fields.get("tags", "")))
        if fields.get("typ"):
            types[fields["typ"]] += 1
    return tags, types, len(notes)


def as_markdown(title: str, counts: Counter, total: int) -> list[str]:
    rows = [f"| {title} | Anzahl | Anteil |", "|---|---|---|"]
    for name, count in counts.most_common():
        rows.append(f"| {name} | {count} | {round(count / total * 100, 1)} % |")
    return rows


def as_csv(title: str, counts: Counter) -> list[str]:
    return [f"{title};count"] + [f"{name};{count}" for name, count in counts.most_common()]


def main() -> None:
    tags, types, total = collect(NOTES_DIR)
    if total == 0:
        print("Keine Notizen gefunden.")
        return
    if sys.argv[1:] == ["csv"]:
        lines = as_csv("tag", tags) + [""] + as_csv("typ", types)
    else:
        lines = as_markdown("Tag", tags, total) + [""] + as_markdown("Typ", types, total)
        lines += ["", f"Notizen: {total}"]
    print("\n".join(lines))


if __name__ == "__main__":
    main()
