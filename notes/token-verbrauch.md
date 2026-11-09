---
titel: Token-Verbrauch senken
typ: how-to
tags: [kosten, kontext]
stand: 2026-10-23
quellen:
  - archive/2026-10-27-retro-sprint-42.md
  - archive/2026-10-23-link-kosten.md
  - https://code.claude.com/docs/en/costs
---

Der Token-Verbrauch des Teams hat sich im Oktober 2026 fast verdoppelt (Retro Sprint 42, 27. Oktober 2026). Was hilft, nach den Empfehlungen von Anthropic:

## Kontext klein halten

- Zwischen unabhängigen Aufgaben `/clear`; lange Sessions mit `/compact` zusammenfassen (siehe [[kontextfenster]]).
- Die [[claude-md]] kurz halten; seltene Anleitungen als Skill, der nur bei Bedarf geladen wird (siehe [[skills]]).
- Nur die MCP-Server einbinden, die gebraucht werden — jede Tool-Beschreibung kostet Kontext (siehe [[mcp]]).
- Ausführliche Arbeiten wie Recherche oder Log-Analyse an [[subagenten]] geben; zurück kommt nur das Ergebnis.

## Gezielter arbeiten

- Konkrete Prompts mit Datei und Ziel statt „schau mal, was du findest“.
- Größere Änderungen im [[plan-mode]] — ein falscher Ansatz wird verworfen, bevor er Tokens kostet.
- Das Modell passend wählen: Sonnet als Standard, Haiku für einfache Subagenten (siehe [[standard-agent]]).

## Messen

`/context` zeigt, was gerade im Kontext steckt, `/usage` den Verbrauch. Anna wertet bis Sprint 44 aus, was davon im Team wirkt.
