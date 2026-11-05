# Übungen

Jede Übung fügt dem Handbuch einen Baustein hinzu. Zu jeder steht hier, **was** zu tun ist, **warum** gerade dieser Baustein, woran ihr merkt, dass ihr **fertig** seid, und welcher **Branch** die Musterlösung enthält. Die Zeiten sind Richtwerte. Wer früher fertig ist, nimmt sich eine Zusatzaufgabe.

Nach jeder Übung lohnt dieselbe Frage: Was davon gehört ins Repo und gilt für das ganze Team, was bleibt persönlich?

## Übung 1 — Ankommen im Handbuch (25 Min.)

1. Repo klonen, im Viewer ansehen, im Repo-Ordner `claude` starten.
2. `/init` eine CLAUDE.md erzeugen lassen und sie auf das Wesentliche kürzen (siehe [[claude-md]] im Handbuch selbst).
3. `tools/export.py` von Claude erklären lassen, Code Smells finden und beheben lassen. Das Skript muss danach dieselbe Ausgabe liefern.
4. Einen Eingang aus `inbox/` **nur per Prompt** zu einer Notiz verarbeiten lassen: Notiz in `notes/`, Link in `index.md`, Eingang nach `archive/`. Vorher und nachher `/context` aufrufen und den Verbrauch notieren — das ist der Ausgangswert für später.

- **Warum:** Erst sehen, wie weit ein guter Prompt allein kommt. Jeder spätere Baustein muss sich an dieser Handarbeit messen.
- **Fertig, wenn:** eine neue Notiz in `notes/`, der Eingang liegt in `archive/`, `uv run tools/export.py` läuft.
- **Kurzfassung (10 Min.)** für Teams, die Claude Code schon nutzen: nur Schritt 4.
- **Musterlösung:** `01-init`

## Übung 2 — `kb-check` per Spec bauen (35 Min.)

Ein Prüfwerkzeug für die Notizen, erst spezifiziert, dann gebaut:

1. Mit OpenSpec (`npm install -g @fission-ai/openspec@latest`, dann `openspec init`, dann `/opsx:propose`) oder im Plan Mode eine Spec schreiben lassen. Geprüft werden soll: Frontmatter mit den Pflichtfeldern `titel`, `typ`, `tags`, `stand`; erlaubte Werte für `typ`; keine H1-Überschrift; keine Wikilinks ins Leere; keine verwaisten Notizen, die weder `index.md` noch eine andere Notiz verlinkt.
2. Spec lesen und nachschärfen, dann umsetzen lassen — mit Tests.
3. Absichern mit `/goal`:
   `/goal uv run pytest ist grün und uv run tools/kb_check.py notes/ meldet keine Fehler; zeige beide Ausgaben; höchstens 20 Runden`
   Achtung: In den vorhandenen Notizen steckt ein Fehler, den das Werkzeug finden soll.
4. Mit `/diff` die Änderungen ansehen, dann `/code-review`.

- **Warum:** Erst aufschreiben, dann bauen lassen. Und `/goal` braucht eine objektive Prüfung — jetzt gibt es eine.
- **Fertig, wenn:** `uv run tools/kb_check.py notes/` läuft ohne Fehler, die Tests sind grün, das Review ist gelesen.
- **Musterlösung:** `02-kb-check`

## Übung 3 — Regeln und Grenzen (25 Min.)

1. Rules in `.claude/rules/` anlegen: `notizen.md` (Frontmatter, kein H1, Dateinamen in kebab-case, Sprache Deutsch, Verlinkung) und `quellen.md` (jede Aussage mit Quelle, Protokolle bleiben unverändert, Widersprüche nicht überschreiben).
2. Permissions in `.claude/settings.json`: Schreiben in `notes/`, `inbox/` und `archive/` erlauben, alles unter `.obsidian/` verbieten. Pfade relativ zum Projekt beginnen mit `/`, also `Edit(/notes/**)`.
3. Unter macOS, Linux oder WSL2: `/sandbox` einschalten. Unter nativem Windows gibt es keine Sandbox — dort reichen die Permissions.
4. Zwei weitere Eingänge per Prompt verarbeiten und prüfen, ob die Regeln greifen. Dann Claude bitten, eine Datei in `.obsidian/` zu ändern.

- **Warum:** Rules für das, was immer gilt. Permissions für das, was nie passieren darf — eine Regel kann Claude übersehen, eine Deny-Permission nicht.
- **Fertig, wenn:** die neuen Notizen bestehen `kb-check` ohne Nacharbeit, der Schreibversuch in `.obsidian/` wird abgelehnt.
- **Musterlösung:** `03-rules`

## Übung 4 — MCP-Server `kb-search` (30 Min.)

1. Einen MCP-Server `tools/kb_search.py` bauen lassen: offizielles MCP-Python-SDK ab Version 2 (`MCPServer`, in 1.x hieß es `FastMCP`), Abhängigkeiten als Inline-Metadaten (PEP 723), gestartet mit `uv run`. Tools: `search_notes` (Volltextsuche mit Treffer-Ausschnitt), `backlinks` (wer verlinkt eine Notiz) und `list_tags`.
2. Im Projekt einbinden über `.mcp.json`, mit `/mcp` prüfen.
3. Im User-Scope einbinden (`claude mcp add --scope user …` mit absolutem Pfad), dann in einem **anderen** Projekt fragen: „Was sagt unser Handbuch zu Permissions?“

- **Warum:** Innerhalb des Handbuchs braucht Claude kein MCP, Dateien lesen genügt. Der Mehrwert entsteht erst, wenn andere Projekte auf das Wissen zugreifen.
- **Fertig, wenn:** `/mcp` zeigt den Server verbunden, und die Frage aus dem anderen Projekt wird mit einem Zitat aus einer Notiz beantwortet.
- **Musterlösung:** `04-mcp`

## Übung 5 — Skill `ingest` (15 Min.)

1. Den Ablauf aus Übung 1 als Skill `.claude/skills/ingest/SKILL.md` festhalten: Eingang lesen und einordnen, Notiz schreiben oder ergänzen, verlinken, `index.md` nachziehen, Eingang archivieren, `kb-check` laufen lassen.
2. Einmal per `/ingest` aufrufen, einmal nur beschreiben („verarbeite die Inbox“) und schauen, ob Claude den Skill von selbst findet.
3. `/skill-doctor` über den Skill laufen lassen.

- **Warum:** ein wiederkehrender Ablauf, der Wissen und Schritte bündelt und nur bei Bedarf in den Kontext kommt.
- **Fertig, wenn:** drei Eingänge laufen mit einem einzigen `/ingest` durch.
- **Musterlösung:** `05-skill`

## Übung 6 — Agent `recherchierer` (15 Min.)

1. Einen Subagenten `.claude/agents/recherchierer.md` anlegen: nur lesende Tools plus Web-Abruf, kleineres Modell, liefert eine Zusammenfassung mit Quellen zurück und schreibt selbst nichts.
2. `ingest` so ändern, dass er Link-Eingänge an den `recherchierer` gibt.
3. Einen Link-Eingang verarbeiten und mit `/context` vergleichen: Wie viel Kontext hat die Recherche diesmal im Hauptgespräch belegt?

- **Warum:** Recherche bläht den Hauptkontext auf. Ein Agent arbeitet abgeschottet und liefert nur das Ergebnis zurück.
- **Fertig, wenn:** ein Link-Eingang landet als Notiz mit Quellen, ohne dass die ganze Webseite im Hauptkontext stand.
- **Musterlösung:** `06-agent`

## Übung „Eigener Agent“ (20 Min.)

Baut einen Agenten für eine Aufgabe aus **eurem** Arbeitsalltag — nicht fürs Handbuch. Ideen:

- Infrastruktur: ein `log-analyst`, der Logdateien oder Ausgaben von `kubectl`/`docker` liest und eine Fehlerdiagnose liefert, ohne etwas zu ändern
- Infrastruktur: ein `config-reviewer` für Dockerfiles, Pipelines oder Terraform, der gegen eure Konventionen prüft
- Entwicklung: ein `test-schreiber`, der zu einer Klasse fehlende Tests ergänzt und nur unter `src/test/` schreiben darf
- Review: ein `security-pruefer`, der einen Diff auf Geheimnisse, Injection und unsichere Defaults durchsieht

Wichtig sind die Entscheidungen im Frontmatter: Welche Tools braucht er wirklich (`tools`, `disallowedTools`)? Welches Modell reicht (`model`)? Darf er ohne Rückfrage arbeiten (`permissionMode`)? Was gibt er zurück? Dann einmal aus dem Hauptgespräch aufrufen — automatisch über die Beschreibung und gezielt mit `@`.

Im Handbuch zeigt `06-agent` mit dem `wissensarchitekt` ein zweites Beispiel: ein Agent, der eine neue Notiz gegen den Bestand prüft und Duplikate und Widersprüche meldet.

## Übung 7 — Hook auf `kb-check` (15 Min.)

1. Einen PostToolUse-Hook auf `Write|Edit` einrichten, der nach jedem Schreiben unter `notes/` das Prüfwerkzeug laufen lässt und Fehler an Claude zurückgibt (Exit-Code 2, Meldung auf stderr).
2. Claude bitten, in eine Notiz eine H1-Überschrift einzubauen, und zusehen, was passiert.
3. Dieselbe Frage wie in Übung 1 stellen: Was kostet der Hook an Tokens, was spart er?

- **Warum:** Was jedes Mal passieren muss, gehört nicht in einen Prompt, sondern in einen Hook — deterministisch statt „hoffentlich“.
- **Fertig, wenn:** der Hook meldet die H1, und Claude reagiert darauf — er korrigiert sie oder fragt nach, weil ihr sie ausdrücklich verlangt habt. Beides zeigt: Die Prüfung läuft, ohne dass jemand daran denken muss.
- **Musterlösung:** `07-hook`

## Übung „Team-Verteilung“ (30 Min.)

1. Skill, Agenten, Hook und MCP-Server als Plugin `team-handbuch` unter `plugins/team-handbuch/` verpacken; die Skripte gehören mit ins Plugin.
2. Das Repo zum Marketplace machen: `.claude-plugin/marketplace.json` im Wurzelordner.
3. Eure Nachbarin oder euer Nachbar installiert das Plugin aus eurem Repo in einem eigenen, leeren Projekt und verarbeitet dort einen Eingang.

- **Warum:** So verteilt ein Team seine Werkzeuge, ohne dass jeder abschreibt — versioniert, mit einem Befehl installiert, mit einem Befehl aktualisiert.
- **Fertig, wenn:** im Nachbarprojekt erscheint `/team-handbuch:ingest` und läuft.
- **Musterlösung:** `07b-plugin`

## Übung 8 — Abnahme (40 Min.)

1. Die fünf neuen Eingänge aus `extras/abnahme-inbox/` nach `inbox/` kopieren. Darunter sind ein Duplikat und ein Widerspruch.
2. `/loop 5m /ingest` die Inbox überwachen lassen.
3. Absichern: `/goal inbox/ ist leer und uv run tools/kb_check.py notes/ meldet keine Fehler; zeige die Ausgabe; höchstens 30 Runden`
4. Zum Schluss `/code-review` über alle Änderungen des Tages, dann committen.

Wer ein eigenes leeres Repo hat, richtet dort stattdessen das Handbuch für das eigene Team ein — per Plugin aus Übung „Team-Verteilung“ — und füllt es mit echtem Wissen, etwa Architekturentscheidungen oder Onboarding.

- **Warum:** Alle Bausteine laufen ohne Zutun zusammen. Was jetzt noch Handarbeit braucht, zeigt, welcher Baustein fehlt.
- **Fertig, wenn:** die Inbox ist leer, `kb-check` meldet keine Fehler, `index.md` verlinkt alle neuen Notizen.
- **In der Runde:** Wie ist Claude mit Duplikat und Widerspruch umgegangen — erkannt oder einfach überschrieben?
- **Musterlösung:** `08-final`

## Zusatzaufgaben

- **Statusline:** `/statusline` eine Statuszeile mit Modell, Kontextfüllstand und Branch bauen lassen.
- **Harness:** Im eigenen Agenten-Harness ([codevibe-de/agent-harness-py](https://github.com/codevibe-de/agent-harness-py), Stufe `03-tools`) ein Tool `kb_search` ergänzen, das den Code aus Übung 4 wiederverwendet.
- **Persönlicher Assistent:** dasselbe Muster für die eigenen Notizen, ergänzt um Kalender, Aufgaben und Mail per MCP.
- **Codex zum Vergleich:** die Abnahme einmal mit Codex und `AGENTS.md` wiederholen.
