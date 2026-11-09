---
titel: Skill oder Rule?
typ: wissen
tags: [claude-code, kontext]
stand: 2026-10-29
quellen:
  - archive/2026-10-29-frage-skill-oder-rule.md
  - https://code.claude.com/docs/en/memory
  - https://code.claude.com/docs/en/skills
---

Die Frage von Deniz (29. Oktober 2026) lässt sich an zwei Fragen entscheiden: **Gilt es immer, oder nur bei einer bestimmten Aufgabe?** Und: **Ist es eine Vorgabe oder ein Ablauf?**

| | Rule | Skill |
|---|---|---|
| Inhalt | Vorgabe, die immer gilt | Ablauf mit Schritten, Vorlagen, Skripten |
| Im Kontext | immer — oder sobald passende Dateien angefasst werden (`paths`) | nur die Beschreibung; der Rest erst, wenn der Skill gebraucht wird |
| Aufruf | gar nicht, wirkt von selbst | automatisch über die Beschreibung oder per `/name` |

## Deniz' drei Fälle

1. **Namenskonvention für REST-Endpunkte** — Rule, auf die Controller-Dateien beschränkt (`paths`).
2. **Neues Werkzeug-Modul anlegen, sieben Schritte mit Vorlage** — Skill; die Vorlage liegt im Skill-Ordner.
3. **Tests immer mit JUnit 5** — Rule, oder eine Zeile in der [[claude-md]].

Faustregel: Was in jeder Session Tokens kostet, muss sich in jeder Session lohnen (siehe [[kontextfenster]]).
