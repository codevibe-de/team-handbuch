---
titel: Claude Code als Standard-Agent, Modellwahl
typ: entscheidung
tags: [claude-code, team, kosten]
stand: 2026-10-28
quellen:
  - archive/2026-10-28-protokoll-architekturrunde.md
  - archive/2026-11-04-mail-modellwahl.md
---

Claude Code ist unser Standard-Coding-Agent (Architekturrunde, 28. Oktober 2026).

## Warum

Getestet wurden Claude Code, GitHub Copilot und Codex über je zwei Wochen. Claude Code lieferte die besten Ergebnisse bei Refactorings über mehrere Dateien; [[plan-mode]], Skills und Hooks passen zu unserem Ablauf, und die Claude-Teams-Lizenz ist schon vorhanden. Copilot bleibt in der IDE für die Vervollständigung erlaubt.

## Modellwahl

| Modell | Wofür |
|---|---|
| Sonnet | Standard |
| Opus | nur für Architekturfragen und große Refactorings, bewusst per `/model` gewählt |
| Haiku | Subagenten, die nur suchen oder zusammenfassen |

Nächste Architekturrunde am 25. November 2026.

## Offen

Welches Modell ist ab Dezember Standard? Zwei Aussagen stehen gegeneinander:

- „Standardmodell ist Sonnet. Opus nur für Architekturfragen und große Refactorings“ (Architekturrunde, 28. Oktober 2026)
- „ab dem 1. Dezember 2026 [stellen wir] das Standardmodell auf Opus um“, weil die Qualität bei Refactorings besser und die Kosten über die Teams-Lizenz abgedeckt seien (Mail der Teamleitung, 4. November 2026)

Die Mail nennt den Beschluss der Architekturrunde nicht und steht gegen die offene Frage zum [[token-verbrauch]]. Zu klären in der Architekturrunde am 25. November 2026; bis dahin gilt Sonnet.

Siehe auch [[kontextfenster]].
