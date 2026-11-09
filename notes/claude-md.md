---
titel: CLAUDE.md schreiben
typ: how-to
tags: [claude-code, kontext]
stand: 2026-10-20
quellen:
  - https://code.claude.com/docs/en/memory
---

Die `CLAUDE.md` im Projektordner lädt Claude Code zu Beginn jeder Session automatisch in den Kontext. Was darin steht, gilt also immer — und kostet in jeder Session Tokens.

## Was hineingehört

- Zweck des Projekts in zwei, drei Sätzen
- Befehle, die Claude nicht erraten kann: Build, Tests, Lint
- Konventionen, die vom Üblichen abweichen
- Wo was liegt, wenn die Ordnerstruktur nicht selbsterklärend ist

## Was nicht hineingehört

- Alles, was Claude aus dem Code selbst ablesen kann
- Lange Anleitungen für seltene Aufgaben — dafür gibt es Skills
- Persönliche Vorlieben — die gehören in `~/.claude/CLAUDE.md` oder `CLAUDE.local.md`

Faustregel: Jede Zeile muss sich in jeder Session lohnen. Eine kurze CLAUDE.md wird besser befolgt als eine lange.

Siehe auch [[agent-loop]] und [[permissions]].
