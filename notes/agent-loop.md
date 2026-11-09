---
titel: Agent Loop
typ: glossar
tags: [grundlagen]
stand: 2026-10-20
quellen:
  - https://code.claude.com/docs/en/how-claude-code-works
---

Der Agent Loop ist die Schleife, in der ein Coding-Agent arbeitet: Das Modell bekommt die Aufgabe samt [[kontextfenster]], entscheidet sich für ein Werkzeug (Datei lesen, Befehl ausführen, Datei schreiben), der Agent führt es aus und gibt das Ergebnis zurück. Das wiederholt sich, bis das Modell keine Werkzeuge mehr anfordert und antwortet.

Daraus folgt:

- Jedes Werkzeugergebnis landet im Kontext und kostet Tokens.
- Der Agent ist nur so gut wie die Rückmeldungen, die er bekommt — Tests und Prüfskripte sind seine Augen.
- Was der Agent nie tun soll, regelt man außerhalb der Schleife, über [[permissions]].
