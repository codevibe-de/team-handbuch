# /// script
# requires-python = ">=3.12"
# dependencies = ["mcp>=2.3", "pyyaml>=6"]
# ///
"""MCP server that makes the team handbook searchable from any project.

Run:      uv run tools/kb_search.py
Project:  .mcp.json in this repo
Anywhere: claude mcp add --scope user kb-search -- uv run /absolute/path/to/tools/kb_search.py

The handbook root is the folder above tools/, or KB_ROOT if set.
"""

import os
from collections import Counter
from pathlib import Path

from mcp.server import MCPServer

from kb_check import parse_note, wikilinks

ROOT = Path(os.environ.get("KB_ROOT") or Path(__file__).resolve().parent.parent)
NOTES = ROOT / "notes"

mcp = MCPServer("kb-search", instructions="Search and read the team handbook on agentic development with Claude Code (German notes).")


def all_notes():
    return [parse_note(p) for p in sorted(NOTES.glob("*.md"))]


def title_of(note) -> str:
    return str((note.frontmatter or {}).get("titel") or note.path.stem)


@mcp.tool()
def search_notes(query: str, limit: int = 10) -> list[dict]:
    """Full-text search over the team handbook (case-insensitive, all words must occur in the note).

    Returns matching notes with title, type and the first matching lines.
    Use read_note to get the full text of a hit.
    """
    words = query.lower().split()
    hits = []
    for note in all_notes():
        text = note.path.read_text(encoding="utf-8")
        if not all(w in text.lower() for w in words):
            continue
        lines = [f"{n}: {line.strip()}" for n, line in note.body if any(w in line.lower() for w in words)]
        hits.append({
            "note": note.path.stem,
            "titel": title_of(note),
            "typ": (note.frontmatter or {}).get("typ"),
            "treffer": lines[:3],
        })
    return hits[:limit]


@mcp.tool()
def read_note(note: str) -> str:
    """Return the full Markdown text of a note, e.g. read_note("permissions")."""
    path = NOTES / f"{note.removesuffix('.md')}.md"
    if not path.is_file():
        raise ValueError(f"Keine Notiz '{note}'. search_notes oder list_tags helfen beim Finden.")
    return path.read_text(encoding="utf-8")


@mcp.tool()
def backlinks(note: str) -> list[str]:
    """List the notes (and index) that link to the given note with [[...]]."""
    target = note.removesuffix(".md")
    sources = [n for n in all_notes() if any(t == target for _, t in wikilinks(n))]
    index = ROOT / "index.md"
    names = [n.path.stem for n in sources if n.path.stem != target]
    if index.exists() and any(t == target for _, t in wikilinks(parse_note(index))):
        names.insert(0, "index")
    return names


@mcp.tool()
def list_tags() -> dict[str, int]:
    """All tags in the handbook with the number of notes carrying them, most used first."""
    counts = Counter()
    for note in all_notes():
        tags = (note.frontmatter or {}).get("tags") or []
        counts.update(tags if isinstance(tags, list) else [tags])
    return dict(counts.most_common())


if __name__ == "__main__":
    mcp.run()
