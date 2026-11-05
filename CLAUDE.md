# CLAUDE.md

Team-Handbuch zur agentischen Entwicklung mit Claude Code — eine Wissensbasis aus Markdown-Notizen, kein Softwareprojekt. Inhalte sind auf Deutsch.

## Ablauf

Neues Material liegt in `inbox/`. Jeder Eingang wird zu einer Notiz in `notes/` verarbeitet (oder ergänzt eine vorhandene), in `index.md` verlinkt und danach nach `archive/` verschoben. Protokolle und Mails werden nie verändert, sondern unverändert archiviert und aus der Notiz heraus zitiert.

## Notizen

- Dateiname in kebab-case, ein Thema je Datei
- Frontmatter: `titel`, `typ` (`entscheidung`, `how-to`, `wissen`, `glossar`, `frage`), `tags`, `stand` (JJJJ-MM-TT), `quellen`
- Keine H1-Überschrift, der Titel steht im Frontmatter
- Verlinkung mit `[[dateiname]]`; jede Notiz ist in `index.md` verlinkt

## Werkzeuge

- `uv run tools/kb_check.py notes/` — prüft alle Notizen; nach jeder Änderung an `notes/` laufen lassen
- `uv run pytest` — Tests der Werkzeuge
- `uv run tools/export.py` — Tag-Statistik der Notizen
- `tools/kb_search.py` — MCP-Server `kb-search` für andere Projekte (eingebunden über `.mcp.json`)
- Spezifikationen liegen unter `openspec/specs/`
