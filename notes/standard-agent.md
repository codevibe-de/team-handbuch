---
titel: Claude Code als Standard-Agent, Modellwahl
typ: entscheidung
tags: [claude-code, team, kosten]
stand: 2026-10-28
quellen:
  - archive/2026-10-28-protokoll-architekturrunde.md
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

Siehe auch [[kontextfenster]].
