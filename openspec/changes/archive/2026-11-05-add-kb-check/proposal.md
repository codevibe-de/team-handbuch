# Proposal

## Why

The handbook grows with every processed inbox item, and nothing checks the notes. Missing frontmatter, stray H1 headings, wikilinks into nowhere and notes nobody links to only show up when someone stumbles over them. Claude needs an objective check it can run itself — as a target for `/goal`, later as a hook.

## What Changes

- New command-line tool `tools/kb_check.py`, run with `uv run`, that checks the notes in `notes/` or single note files and reports every problem as `path:line: message`.
- Tests for every rule.
- The existing notes are brought into a state that passes the check.

## Capabilities

### New Capabilities
- `kb-check`: checking handbook notes for required frontmatter, headings, wikilinks and orphans

### Modified Capabilities

## Impact

- New files `tools/kb_check.py` and `tests/test_kb_check.py`
- New dependency PyYAML (inline script metadata and `pyproject.toml`), pytest as dev dependency
- Runs on Windows, macOS and Linux
