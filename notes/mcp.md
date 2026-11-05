---
titel: MCP
typ: wissen
tags: [claude-code, mcp]
stand: 2026-10-23
quellen:
  - archive/2026-10-23-link-mcp.md
  - https://code.claude.com/docs/en/mcp
---

Das Model Context Protocol ist ein offener Standard, über den Claude Code externe Werkzeuge und Datenquellen anbindet. Ein MCP-Server bietet Tools an; Claude ruft sie auf wie seine eingebauten Werkzeuge.

## Arten und Ebenen

- **Lokal (stdio):** Claude Code startet den Server als Prozess, etwa `uv run tools/kb_search.py`.
- **Entfernt (HTTP):** der Server läuft beim Anbieter, angemeldet wird per OAuth.
- **Ebenen:** `local` (nur ich, dieses Projekt), `project` (`.mcp.json` im Repo, für alle) und `user` (ich, alle Projekte). Hinzufügen mit `claude mcp add`, prüfen mit `/mcp`.

## Bei uns

| Server | Wofür | Stand |
|---|---|---|
| Figma | Designs in Code umsetzen | angebunden |
| `kb-search` | dieses Handbuch aus anderen Projekten durchsuchen | im Repo, `.mcp.json` |
| Jira | Tickets lesen und aktualisieren | Idee; Anbieter und Anmeldung noch zu prüfen |

Jeder Server kostet Kontext, weil seine Tool-Beschreibungen geladen werden — nur einbinden, was gebraucht wird (siehe [[token-verbrauch]]). Siehe auch [[settings-ebenen]].
