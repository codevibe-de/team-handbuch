---
titel: Ebenen der Einstellungen
typ: wissen
tags: [claude-code, team, sicherheit]
stand: 2026-10-21
quellen:
  - archive/2026-10-21-link-settings.md
  - https://code.claude.com/docs/en/settings
---

Claude Code liest Einstellungen aus mehreren Dateien. Bei Konflikten gewinnt die höhere Ebene:

| Rang | Ebene | Ort | Für wen |
|---|---|---|---|
| 1 | Managed | vom Admin verteilt, z. B. über die Teams-Organisation oder eine Systemdatei | ganze Organisation, nicht überschreibbar |
| 2 | Kommandozeile | Optionen beim Start von `claude` | diese Session |
| 3 | Lokal im Projekt | `.claude/settings.local.json` | nur ich, nur dieses Projekt, nicht eingecheckt |
| 4 | Projekt | `.claude/settings.json` | alle im Repo, eingecheckt |
| 5 | Benutzer | `~/.claude/settings.json` | ich, in allen Projekten |

Permissions werden über die Ebenen hinweg zusammengeführt; ein Deny gewinnt immer, gleich auf welcher Ebene.

## Was bei uns ins Repo gehört

`.claude/settings.json` mit den gemeinsamen Permissions und Hooks, dazu `.mcp.json` für gemeinsame MCP-Server. Persönliches gehört in `.claude/settings.local.json` oder `~/.claude/settings.json`. Siehe [[permissions]] und [[mcp]].
