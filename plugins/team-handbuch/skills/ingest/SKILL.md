---
name: ingest
description: Verarbeitet Eingänge aus inbox/ zu Notizen im Team-Handbuch — einordnen, Notiz anlegen oder ergänzen, verlinken, index.md nachziehen, archivieren, prüfen. Richtet das Handbuch bei Bedarf erst ein. Verwenden, wenn die Inbox abgearbeitet werden soll oder ein bestimmter Eingang ins Handbuch soll.
argument-hint: "[datei ...]"
allowed-tools: Read Write Edit Glob Grep Agent Bash(uv run ${CLAUDE_PLUGIN_ROOT}/scripts/kb_check.py *) Bash(git mv *)
---

# Inbox verarbeiten

Verarbeite die übergebenen Dateien aus `inbox/` oder, ohne Argument, alle Dateien darin — eine nach der anderen, älteste zuerst. Ist die Inbox leer, sag das in einem Satz und hör auf.

**Einrichten:** Fehlen im Projekt `inbox/`, `notes/`, `archive/` oder `index.md`, lege sie an. `index.md` bekommt Frontmatter (`titel`, `typ: startseite`, `tags`, `stand`), einen Satz zum Zweck und die Abschnitte „Entscheidungen“, „How-tos“, „Wissen“, „Glossar“ und „Offene Fragen“.

## Konventionen

- Eine Datei je Thema in `notes/`, Dateiname in kebab-case ohne Umlaute.
- Frontmatter mit `titel`, `typ`, `tags` (Liste), `stand` (JJJJ-MM-TT, Datum der Quelle) und `quellen` (Liste).
- `typ` ist einer von `entscheidung`, `how-to`, `wissen`, `glossar`, `frage`.
- Keine H1-Überschrift, gegliedert wird mit `##`. Sprache wie der Rest des Handbuchs.
- Jede Notiz verlinkt mindestens eine verwandte Notiz mit `[[dateiname]]` und ist in `index.md` verlinkt.
- Jede Aussage hat eine Quelle: der archivierte Eingang `archive/<datei>` oder die URL.
- Protokolle, Mails und kopierte Artikel werden nie verändert, nur archiviert und zitiert.
- Ein ausdrücklich späterer Beschluss ersetzt den früheren: Notiz umschreiben, `stand` aktualisieren. Ein Widerspruch ohne ausdrückliche Ablösung wird nicht überschrieben: beide Aussagen mit Quelle stehen lassen, Abschnitt `## Offen`, Eintrag unter „Offene Fragen“ in `index.md`.
- Nichts erfinden.

## Für jeden Eingang

1. **Einordnen.** Link mit Auftrag → an den Agenten `recherchierer` aus diesem Plugin geben, die Webseite nicht selbst in den Kontext holen. Protokoll, Mail, Artikel → Beschlüsse und Fakten herausziehen. Notiz → übernehmen und glätten. Frage → beantworten, wenn eine verlässliche Quelle es hergibt, sonst `typ: frage`.
2. **Bestand prüfen.** Den Agenten `wissensarchitekt` aus diesem Plugin fragen: neu, Duplikat, Ergänzung, abgelöst oder Widerspruch? Seiner Empfehlung folgen.
3. **Schreiben** nach den Konventionen. Duplikat: nichts ändern.
4. **Startseite nachziehen.** Neue Notizen in `index.md` im passenden Abschnitt verlinken.
5. **Archivieren.** `git mv inbox/<datei> archive/<datei>` (ohne Git: verschieben).
6. **Prüfen.** `uv run ${CLAUDE_PLUGIN_ROOT}/scripts/kb_check.py notes/` und jede Meldung beheben.

## Zum Schluss

Eine kurze Tabelle: Eingang, was daraus wurde, betroffene Notizen. Widersprüche und offene Fragen ausdrücklich nennen.
