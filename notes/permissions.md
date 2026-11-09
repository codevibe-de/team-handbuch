---
titel: Permissions im Team
typ: entscheidung
tags: [claude-code, sicherheit, team]
stand: 2026-03-12
quellen:
  - Team-Absprache vom 12. März 2026
---

Claude Code fragt vor jedem Werkzeugaufruf nach, der nicht ausdrücklich erlaubt ist. Damit das im Alltag nicht nervt, legt jede Entwicklerin und jeder Entwickler die eigenen Freigaben in `.claude/settings.local.json` fest. Diese Datei wird nicht eingecheckt.

Begründung: Jeder arbeitet anders, und eine gemeinsame Liste müsste ständig abgestimmt werden.

Gemeinsam gilt nur: keine Freigabe für `git push` und keine für das Löschen von Dateien außerhalb des Projekts.

Siehe auch [[claude-md]].
