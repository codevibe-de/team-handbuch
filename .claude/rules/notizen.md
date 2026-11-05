---
paths:
  - "notes/**/*.md"
---

# Notizen im Handbuch

- Eine Datei je Thema, Dateiname in kebab-case ohne Umlaute: `env-dateien-schuetzen.md`.
- Frontmatter mit `titel`, `typ`, `tags` (Liste), `stand` (JJJJ-MM-TT, Datum der Quelle) und `quellen` (Liste).
- `typ` ist einer von: `entscheidung` (was das Team beschlossen hat, mit Begründung), `how-to` (wie man etwas tut), `wissen` (wie etwas funktioniert), `glossar` (Begriffe), `frage` (offen, noch ohne Antwort).
- Keine H1-Überschrift. Gliedern mit `##`.
- Sprache Deutsch, sachlich, kurz. Fachbegriffe und Befehle bleiben im Original.
- Jede Notiz verlinkt mindestens eine verwandte Notiz mit `[[dateiname]]` und ist in `index.md` im passenden Abschnitt verlinkt.
- Vor dem Anlegen prüfen, ob es schon eine Notiz zum Thema gibt — dann diese ergänzen statt eine zweite anlegen.
- Nach jeder Änderung `uv run tools/kb_check.py notes/` ausführen und alle Meldungen beheben.
