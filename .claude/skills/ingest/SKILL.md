---
name: ingest
description: Verarbeitet Eingänge aus inbox/ zu Notizen im Team-Handbuch — einordnen, Notiz anlegen oder ergänzen, verlinken, index.md nachziehen, archivieren, prüfen. Verwenden, wenn die Inbox abgearbeitet werden soll oder ein bestimmter Eingang ins Handbuch soll.
argument-hint: "[datei ...]"
allowed-tools: Read Write Edit Glob Grep Bash(uv run tools/kb_check.py *) Bash(git mv *)
---

# Inbox verarbeiten

Verarbeite die übergebenen Dateien aus `inbox/` oder, ohne Argument, alle Dateien darin — eine nach der anderen, älteste zuerst (der Dateiname beginnt mit dem Datum). Ist die Inbox leer, sag das in einem Satz und hör auf.

## Für jeden Eingang

1. **Lesen und einordnen.** Was ist es?
   - **Link** mit Auftrag: Seite abrufen, das Gefragte herausziehen, Quelle ist die URL.
   - **Protokoll, Mail oder kopierter Artikel:** Beschlüsse und Fakten herausziehen. Das Original wird nicht verändert.
   - **Notiz oder Stichpunkte:** Inhalt übernehmen und glätten.
   - **Frage:** beantworten, wenn das Handbuch oder eine verlässliche Quelle die Antwort hergibt, sonst als `typ: frage` festhalten.
2. **Bestand prüfen.** Mit Grep in `notes/` nach dem Thema suchen. Gibt es eine passende Notiz, wird sie ergänzt, nicht verdoppelt. Ein Eingang darf mehrere Notizen berühren.
3. **Widersprüche erkennen.** Ersetzt der Eingang einen früheren Beschluss ausdrücklich, Notiz umschreiben und `stand` aktualisieren. Widerspricht er einer Aussage nur, beide stehen lassen, Abschnitt `## Offen` anlegen und in `index.md` unter „Offene Fragen“ eintragen (siehe Rule „Quellen und Widersprüche“).
4. **Schreiben** nach der Rule „Notizen im Handbuch“: Frontmatter, kein H1, mindestens ein Link auf eine verwandte Notiz. In `quellen` steht der archivierte Eingang `archive/<dateiname>` und gegebenenfalls die URL.
5. **Startseite nachziehen.** Neue Notizen in `index.md` im passenden Abschnitt verlinken, mit einer Zeile, worum es geht.
6. **Archivieren.** `git mv inbox/<datei> archive/<datei>` — den Eingang unverändert verschieben, nicht kopieren.
7. **Prüfen.** `uv run tools/kb_check.py notes/` ausführen und jede Meldung beheben, bevor der nächste Eingang drankommt.

## Zum Schluss

Eine kurze Tabelle: Eingang, was daraus wurde (neu, ergänzt, umgeschrieben, Frage offen), betroffene Notizen. Widersprüche und offene Fragen ausdrücklich nennen.
