---
titel: Subagenten
typ: wissen
tags: [claude-code, kontext, kosten]
stand: 2026-10-22
quellen:
  - archive/2026-10-22-link-subagents.md
  - https://code.claude.com/docs/en/sub-agents
---

Ein Subagent ist ein eigener Claude mit eigenem Kontextfenster, eigenem System-Prompt, eigenen Werkzeugen und auf Wunsch eigenem Modell. Der Hauptagent gibt ihm eine Aufgabe, er arbeitet sie für sich ab und liefert nur das Ergebnis zurück — alles, was er unterwegs gelesen hat, bleibt draußen.

## Wann sich ein eigener Agent lohnt

- Eine Teilaufgabe würde den Kontext füllen: Webseiten lesen, Logs durchsuchen, viele Dateien sichten.
- Eine Aufgabe braucht weniger Rechte als das Hauptgespräch, etwa nur lesen.
- Ein kleineres Modell reicht, zum Beispiel Haiku zum Suchen und Zusammenfassen (siehe [[standard-agent]]).
- Mehrere unabhängige Teilaufgaben sollen parallel laufen.

Nicht lohnend ist er für kleine Schritte, die das Ergebnis des Hauptgesprächs direkt brauchen — die Übergabe kostet selbst Tokens.

## Definition

Eine Markdown-Datei in `.claude/agents/` (fürs Team, im Repo) oder `~/.claude/agents/` (persönlich). Das Frontmatter legt mindestens `name` und `description` fest, dazu nach Bedarf `tools`, `model` und `permissionMode`; der Text darunter ist der System-Prompt. Claude wählt den Agenten anhand der `description` selbst aus, gezielt aufrufen lässt er sich mit `@`.

Unsere Agenten: `recherchierer` (Links zusammenfassen, Haiku, nur lesen und Web) und `wissensarchitekt` (neues Material gegen den Bestand prüfen, nur lesen).

Siehe auch [[kontextfenster]] und [[skill-oder-rule]].
