---
titel: Git-Workflow mit Claude
typ: how-to
tags: [claude-code, git, arbeitsweise]
stand: 2026-10-30
quellen:
  - archive/2026-10-30-notiz-git-workflow.md
---

So arbeiten wir mit Git, wenn Claude Code beteiligt ist (Stichpunkte Emil, 30. Oktober 2026):

- Commit-Messages schreibt Claude, im Format Conventional Commits (`feat:`, `fix:`, `refactor:` …). Vor dem Commit liest sie ein Mensch.
- Die PR-Beschreibung schreibt ebenfalls Claude, immer mit einem Abschnitt „Wie getestet“.
- Vor jedem Pull Request läuft einmal `/code-review`; die Regeln dazu stehen in [[code-review-regeln]].
- Claude pusht nie, schon gar nicht mit `--force`. Das gehört als Deny-Regel in die Permissions, nicht nur als Bitte in die CLAUDE.md (siehe [[permissions]]).

Siehe auch [[plan-mode]].
