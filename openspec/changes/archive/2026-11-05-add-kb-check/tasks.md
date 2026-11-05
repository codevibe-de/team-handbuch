# Tasks

## 1. Tool

- [x] 1.1 Add PyYAML and pytest to `pyproject.toml`, configure pytest to find `tools/`
- [x] 1.2 Implement `tools/kb_check.py` with inline script metadata: frontmatter, H1, wikilinks, orphans, output and exit code

## 2. Tests

- [x] 2.1 One test per scenario in `tests/test_kb_check.py`, using a temporary handbook
- [x] 2.2 `uv run pytest` is green

## 3. Handbook

- [x] 3.1 Run `uv run tools/kb_check.py notes/` and fix every problem in the existing notes
