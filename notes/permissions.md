---
titel: Permissions im Team
typ: entscheidung
tags: [claude-code, sicherheit, team]
stand: 2026-10-27
quellen:
  - archive/2026-10-27-retro-sprint-42.md
  - Team-Absprache vom 12. März 2026
---

Die gemeinsamen Freigaben und Verbote für Claude Code stehen in `.claude/settings.json` im Repo und gelten damit für alle. `.claude/settings.local.json` ist nur noch für persönliche Ausnahmen da und wird nicht eingecheckt (Retro Sprint 42, 27. Oktober 2026; verantwortlich Deniz).

## Warum

Bis Oktober hatte jede und jeder eigene Freigaben in `settings.local.json` (Team-Absprache vom 12. März 2026). Das ging schief: Emil hatte `rm` erlaubt, Anna musste jeden `git status` bestätigen, und zweimal hat Claude den Inhalt einer `.env` in eine Antwort geschrieben.

## Was gemeinsam gilt

- Lesen von `.env`-Dateien ist für alle verboten, per Deny-Regel — siehe [[env-dateien-schuetzen]].
- Keine Freigabe für `git push`, siehe [[git-workflow]].
- Kein Löschen von Dateien außerhalb des Projekts.

Siehe auch [[claude-md]].
