---
titel: .env-Dateien vor Claude schützen
typ: how-to
tags: [claude-code, sicherheit]
stand: 2026-10-29
quellen:
  - archive/2026-10-29-frage-env-dateien.md
  - https://code.claude.com/docs/en/permissions
---

Ein Hinweis in der CLAUDE.md reicht nicht. Die CLAUDE.md ist eine Bitte an das Modell, die es im Einzelfall übersehen kann. Verlässlich ist nur eine Deny-Regel in den Permissions — die setzt Claude Code durch, bevor das Werkzeug läuft.

## So geht's

In `.claude/settings.json` im Repo, damit es für alle gilt:

```json
{
  "permissions": {
    "deny": ["Read(**/.env)", "Read(**/.env.*)"]
  }
}
```

Deny gewinnt immer: Eine Allow-Regel kann ein Verbot nicht wieder aufheben.

## Grenzen

Die Regel sperrt das Read-Werkzeug. Ein Shell-Befehl wie `cat .env` ist damit nicht automatisch gesperrt; wer das ausschließen will, verbietet zusätzlich die entsprechenden Bash-Befehle oder schaltet die Sandbox ein (macOS, Linux, WSL2).

Siehe auch [[permissions]] und [[claude-md]].
