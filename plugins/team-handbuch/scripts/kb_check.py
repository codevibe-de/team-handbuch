# /// script
# requires-python = ">=3.12"
# dependencies = ["pyyaml>=6"]
# ///
"""Check handbook notes for frontmatter, headings, broken wikilinks and orphans.

Usage:
    uv run tools/kb_check.py [PATH ...]     (default: notes/)

A directory is checked note by note and for orphans. A single file is checked
on its own; orphans are only detected when a whole directory is checked.
Exit code 0 when everything is fine, 1 when problems were found.
"""

import datetime as dt
import re
import sys
from dataclasses import dataclass
from pathlib import Path

import yaml

REQUIRED_FIELDS = ("titel", "typ", "tags", "stand")
NOTE_TYPES = {"entscheidung", "how-to", "wissen", "glossar", "frage"}
INDEX_FILE = "index.md"

WIKILINK = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")
FENCE = re.compile(r"^\s*(```|~~~)")


@dataclass(frozen=True, order=True)
class Problem:
    path: str
    line: int
    message: str

    def __str__(self) -> str:
        return f"{self.path}:{self.line}: {self.message}"


@dataclass
class Note:
    path: Path
    frontmatter: dict | None
    frontmatter_error: str | None
    body: list[tuple[int, str]]  # (line number, text) outside code fences


def parse_note(path: Path) -> Note:
    lines = path.read_text(encoding="utf-8").splitlines()
    frontmatter, error, body_start = None, None, 0
    if lines and lines[0].strip() == "---":
        end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
        if end is None:
            error = "Frontmatter wird nicht mit --- geschlossen"
        else:
            body_start = end + 1
            try:
                loaded = yaml.safe_load("\n".join(lines[1:end])) or {}
                if isinstance(loaded, dict):
                    frontmatter = loaded
                else:
                    error = "Frontmatter ist keine Zuordnung von Feldern"
            except yaml.YAMLError as exc:
                error = f"Frontmatter ist kein gültiges YAML: {exc.problem or exc}"
    body, in_code = [], False
    for number, text in enumerate(lines[body_start:], start=body_start + 1):
        if FENCE.match(text):
            in_code = not in_code
        elif not in_code:
            body.append((number, text))
    return Note(path, frontmatter, error, body)


def wikilinks(note: Note) -> list[tuple[int, str]]:
    return [(n, m.group(1).strip()) for n, text in note.body for m in WIKILINK.finditer(text)]


def check_frontmatter(note: Note, shown: str) -> list[Problem]:
    if note.frontmatter_error:
        return [Problem(shown, 1, note.frontmatter_error)]
    if note.frontmatter is None:
        return [Problem(shown, 1, "Frontmatter fehlt")]
    fm, problems = note.frontmatter, []
    for field in REQUIRED_FIELDS:
        if fm.get(field) in (None, "", []):
            problems.append(Problem(shown, 1, f"Pflichtfeld '{field}' fehlt"))
    typ = fm.get("typ")
    if typ and typ not in NOTE_TYPES:
        allowed = ", ".join(sorted(NOTE_TYPES))
        problems.append(Problem(shown, 1, f"typ '{typ}' ist nicht erlaubt ({allowed})"))
    tags = fm.get("tags")
    if tags and not isinstance(tags, list):
        problems.append(Problem(shown, 1, "tags muss eine Liste sein"))
    stand = fm.get("stand")
    if stand and not isinstance(stand, dt.date):
        problems.append(Problem(shown, 1, f"stand '{stand}' ist kein Datum im Format JJJJ-MM-TT"))
    return problems


def check_note(note: Note, targets: set[str], shown: str) -> list[Problem]:
    problems = check_frontmatter(note, shown)
    for number, text in note.body:
        if text.startswith("# "):
            problems.append(Problem(shown, number, "H1-Überschrift — der Titel gehört ins Frontmatter"))
    for number, target in wikilinks(note):
        if target not in targets:
            problems.append(Problem(shown, number, f"Wikilink [[{target}]] zeigt ins Leere"))
    return problems


def link_targets(notes_dir: Path) -> set[str]:
    """Names a wikilink may point to: notes, plus Markdown files in the root above."""
    return {p.stem for p in notes_dir.glob("*.md")} | {p.stem for p in notes_dir.parent.glob("*.md")}


def display(path: Path) -> str:
    try:
        return path.resolve().relative_to(Path.cwd()).as_posix()
    except ValueError:
        return path.as_posix()


def check_directory(notes_dir: Path) -> list[Problem]:
    notes = [parse_note(p) for p in sorted(notes_dir.glob("*.md"))]
    targets = link_targets(notes_dir)
    problems = [pr for note in notes for pr in check_note(note, targets, display(note.path))]

    linked = {target for note in notes for _, target in wikilinks(note) if target != note.path.stem}
    index = notes_dir.parent / INDEX_FILE
    if index.exists():
        linked |= {target for _, target in wikilinks(parse_note(index))}
    for note in notes:
        if note.path.stem not in linked:
            problems.append(Problem(display(note.path), 1, f"verwaist — weder {INDEX_FILE} noch eine andere Notiz verlinkt sie"))
    return problems


def check_paths(paths: list[Path]) -> tuple[list[Problem], int]:
    problems, count = [], 0
    for path in paths:
        if path.is_dir():
            problems += check_directory(path)
            count += len(list(path.glob("*.md")))
        elif path.suffix == ".md" and path.exists():
            problems += check_note(parse_note(path), link_targets(path.parent), display(path))
            count += 1
        else:
            problems.append(Problem(display(path), 0, "keine Markdown-Datei und kein Ordner"))
    return sorted(set(problems)), count


def main(argv: list[str]) -> int:
    paths = [Path(arg) for arg in argv] or [Path("notes")]
    problems, count = check_paths(paths)
    for problem in problems:
        print(problem)
    if problems:
        print(f"{len(problems)} Problem(e) in {count} Notiz(en)", file=sys.stderr)
        return 1
    print(f"OK — {count} Notiz(en) geprüft")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
