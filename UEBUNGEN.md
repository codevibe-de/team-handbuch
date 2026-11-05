# Übungen

Jede Übung fügt dem Handbuch einen Baustein hinzu. Bauen kann Claude das meiste in wenigen Minuten — lernen könnt ihr dabei nur, wenn ihr selbst urteilt. Deshalb hat jede Übung neben den Schritten diese Teile:

- **Vorher tippen:** Schreibt auf, was ihr erwartet, bevor ihr Claude loslasst. Danach vergleichen.
- **Warum:** wofür genau dieser Baustein da ist — die Antwort auf „wann nehme ich was?“
- **Fertig, wenn:** woran ihr selbst prüfen könnt, dass es läuft.
- **Prüfen:** eine Aufgabe, die Claude euch nicht abnehmen kann. Erst damit ist die Übung fertig.
- **In der Runde:** die Frage für den Vergleich. Neun Teilnehmende haben neun verschiedene Lösungen — der Unterschied ist der Stoff.
- **Für Schnelle:** eine schwierigere Aufgabe, nicht nur eine längere.
- **Musterlösung:** der Branch, auf den ihr springen könnt (siehe README).

Die Zeiten sind Obergrenzen. Nach jeder Übung lohnt dieselbe Frage: Was davon gehört ins Repo und gilt für das ganze Team, was bleibt persönlich? Notiert Zeit und Kontextverbrauch im [Messblatt](#messblatt) am Ende.

## Übung 1 — Ankommen im Handbuch (25 Min.)

1. Repo klonen, im Viewer ansehen, im Repo-Ordner `claude` starten und den Trust-Dialog bestätigen.
2. `/init` eine CLAUDE.md erzeugen lassen und sie auf das Wesentliche kürzen (siehe [[claude-md]] im Handbuch selbst).
3. `uv run tools/export.py > export-vorher.txt` ausführen. Dann `tools/export.py` von Claude erklären lassen, Code Smells finden und beheben lassen.
4. Einen Eingang aus `inbox/` **nur per Prompt** zu einer Notiz verarbeiten lassen: Notiz in `notes/`, Link in `index.md`, Eingang nach `archive/`. Vorher und nachher `/context` aufrufen und den Verbrauch notieren — das ist der Ausgangswert für später.

- **Vorher tippen:** Wie viele Werkzeugaufrufe braucht Claude für den einen Eingang, und welche Dateien fasst er an?
- **Warum:** Erst sehen, wie weit ein guter Prompt allein kommt. Jeder spätere Baustein muss sich an dieser Handarbeit messen.
- **Fertig, wenn:** eine neue Notiz in `notes/`, der Eingang liegt in `archive/`, `uv run tools/export.py` läuft.
- **Prüfen:** Claude sagt, das Skript liefere dieselbe Ausgabe wie vorher. Glaubt es nicht — vergleicht selbst mit `export-vorher.txt`. Unterschiede in der Reihenfolge: Fehler oder in Ordnung?
- **In der Runde:** Wie lang ist eure CLAUDE.md geworden, und was habt ihr gestrichen?
- **Für Schnelle:** Das alte `export.py` zählt manche Notizen falsch. Findet selbst eine Notiz, an der es scheitert (Tipp: YAML erlaubt mehr als eine Schreibweise für Listen), und lasst dafür einen Test schreiben, der mit dem alten Skript fehlschlägt.
- **Kurzfassung (10 Min.)** für Teams, die Claude Code schon nutzen: nur Schritt 4.
- **Musterlösung:** `01-init`

## Übung 2 — `kb-check` per Spec bauen (35 Min.)

Ein Prüfwerkzeug für die Notizen, erst spezifiziert, dann gebaut:

1. Mit OpenSpec (`npm install -g @fission-ai/openspec@latest`, dann `openspec init`, dann `/opsx:propose`) oder im Plan Mode eine Spec schreiben lassen. Geprüft werden soll: Frontmatter mit den Pflichtfeldern `titel`, `typ`, `tags`, `stand`; erlaubte Werte für `typ`; keine H1-Überschrift; keine Wikilinks ins Leere; keine verwaisten Notizen, die weder `index.md` noch eine andere Notiz verlinkt.
2. Spec lesen und nachschärfen — siehe **Prüfen** —, dann umsetzen lassen, mit Tests.
3. Absichern mit `/goal`:
   `/goal uv run pytest ist grün und uv run tools/kb_check.py notes/ meldet keine Fehler; zeige beide Ausgaben; höchstens 20 Runden`
   In den vorhandenen Notizen steckt ein Fehler, den das Werkzeug finden soll.
4. Mit `/diff` die Änderungen ansehen, dann `/code-review`.

- **Vorher tippen:** Welchen Fall wird die erste Fassung der Spec vergessen?
- **Warum:** Erst aufschreiben, dann bauen lassen. Und `/goal` braucht eine objektive Prüfung — jetzt gibt es eine.
- **Fertig, wenn:** `uv run tools/kb_check.py notes/` läuft ohne Fehler, die Tests sind grün, das Review ist gelesen.
- **Prüfen:** Vor dem Umsetzen findet ihr selbst einen Fall, den die Spec nicht regelt, und tragt ihn ein — etwa `[[ziel|Alias]]`, `# Kommentar` in einem Codeblock, `tags` als Text statt Liste, ein nicht geschlossenes Frontmatter. Nach dem Umsetzen schreibt ihr einen Test von Hand, den Claude nicht geschrieben hat. Besteht das Werkzeug ihn?
- **In der Runde:** Wer hat welche Regel anders festgelegt? Zählt zum Beispiel ein Link einer Notiz auf sich selbst gegen die Verwaisung?
- **Für Schnelle:** Eine Option `--fix`, die sicher behebbare Fehler selbst korrigiert (H1 → H2), als zweiter OpenSpec-Change mit eigener Delta-Spec. Wo zieht ihr die Grenze, was „sicher behebbar“ ist?
- **Musterlösung:** `02-kb-check`

## Übung 3 — Regeln und Grenzen (25 Min.)

1. Rules in `.claude/rules/` anlegen: `notizen.md` (Frontmatter, kein H1, Dateinamen in kebab-case, Sprache Deutsch, Verlinkung) und `quellen.md` (jede Aussage mit Quelle, Protokolle bleiben unverändert, Widersprüche nicht überschreiben).
2. Permissions in `.claude/settings.json`: Schreiben in `notes/`, `inbox/` und `archive/` erlauben, alles unter `.obsidian/` verbieten. Pfade relativ zum Projekt beginnen mit `/`, also `Edit(/notes/**)`.
3. Unter macOS, Linux oder WSL2: `/sandbox` einschalten. Unter nativem Windows gibt es keine Sandbox — dort reichen die Permissions.
4. Zwei weitere Eingänge per Prompt verarbeiten und prüfen, ob die Regeln greifen.

- **Vorher tippen:** Welche eurer Regeln bricht Claude als Erstes?
- **Warum:** Rules für das, was immer gilt. Permissions für das, was nie passieren darf — eine Regel kann Claude übersehen, eine Deny-Permission nicht.
- **Fertig, wenn:** die neuen Notizen bestehen `kb-check` ohne Nacharbeit, ein Schreibversuch in `.obsidian/` wird abgelehnt.
- **Prüfen:** Versucht, eure eigenen Grenzen zu umgehen. Bittet Claude, `.obsidian/app.json` per Shell-Befehl statt per Editor zu ändern, oder eine `.env` mit `cat` zu lesen. Was hält, was nicht? Was müsstet ihr zusätzlich sperren?
- **In der Runde:** Was steht bei wem als Rule, was als Permission, was in der CLAUDE.md — und warum?
- **Für Schnelle:** Ihr seid Admin für alle Teams der Firma. Welche drei Regeln würdet ihr als Managed Settings erzwingen, die kein Team überschreiben kann? Formuliert sie als JSON und begründet jede in einem Satz.
- **Musterlösung:** `03-rules`

## Übung 4 — MCP-Server `kb-search` (30 Min.)

1. Einen MCP-Server `tools/kb_search.py` bauen lassen: offizielles MCP-Python-SDK ab Version 2 (`MCPServer`, in 1.x hieß es `FastMCP`), Abhängigkeiten als Inline-Metadaten (PEP 723), gestartet mit `uv run`. Tools: `search_notes` (Volltextsuche mit Treffer-Ausschnitt), `backlinks` (wer verlinkt eine Notiz) und `list_tags`.
2. Im Projekt einbinden über `.mcp.json`, mit `/mcp` prüfen.
3. Im User-Scope einbinden (`claude mcp add --scope user …` mit absolutem Pfad), dann in einem **anderen** Projekt fragen: „Was sagt unser Handbuch zu Permissions?“

- **Vorher tippen:** Woran erkennt Claude im anderen Projekt, dass er `kb-search` benutzen soll, statt zu raten?
- **Warum:** Innerhalb des Handbuchs braucht Claude kein MCP, Dateien lesen genügt. Der Mehrwert entsteht erst, wenn andere Projekte auf das Wissen zugreifen.
- **Fertig, wenn:** `/mcp` zeigt den Server verbunden, und die Frage aus dem anderen Projekt wird mit einem Zitat aus einer Notiz beantwortet.
- **Prüfen:** Stellt eine Frage, die das Handbuch nicht beantworten kann. Sagt Claude das, oder erfindet er etwas? Und seht in `/context` nach, was die Tool-Beschreibungen eures Servers in jeder Session kosten.
- **In der Runde:** Wessen Tool-Beschreibung hat Claude zuverlässig zum Server geführt, wessen nicht?
- **Für Schnelle:** Ein Tool `open_questions`, das alle Notizen mit `typ: frage` und alle Abschnitte `## Offen` liefert — und eine Beschreibung, die Claude dazu bringt, es bei „was ist bei uns noch ungeklärt?“ zu benutzen.
- **Musterlösung:** `04-mcp`

## Übung 5 — Skill `ingest` (15 Min.)

1. Den Ablauf aus Übung 1 als Skill `.claude/skills/ingest/SKILL.md` festhalten: Eingang lesen und einordnen, Notiz schreiben oder ergänzen, verlinken, `index.md` nachziehen, Eingang archivieren, `kb-check` laufen lassen.
2. Einmal per `/ingest` aufrufen, einmal nur beschreiben („verarbeite die Inbox“) und schauen, ob Claude den Skill von selbst findet.
3. `/skill-doctor` über den Skill laufen lassen.

- **Vorher tippen:** Findet Claude den Skill bei „verarbeite die Inbox“? Und bei „räum mal die Eingänge auf“?
- **Warum:** ein wiederkehrender Ablauf, der Wissen und Schritte bündelt und nur bei Bedarf in den Kontext kommt.
- **Fertig, wenn:** drei Eingänge laufen mit einem einzigen `/ingest` durch.
- **Prüfen:** Schickt den Eingang `2026-11-02-notiz-claude-md-kurz.md` durch — er wiederholt nur, was schon in einer Notiz steht. Erkennt euer Skill das, oder entsteht eine zweite Notiz? Vergleicht außerdem den Kontextverbrauch mit dem Ausgangswert aus Übung 1.
- **In der Runde:** Wessen `description` löst den Skill zuverlässig aus, wessen nicht — und woran liegt es?
- **Für Schnelle:** Teilt den Skill: `SKILL.md` kurz, die Notiz-Konventionen in einer Datei daneben, die Claude nur bei Bedarf liest. Messt, ob sich das lohnt.
- **Musterlösung:** `05-skill`

## Übung 6 — Agent `recherchierer` (15 Min.)

1. Einen Subagenten `.claude/agents/recherchierer.md` anlegen: nur lesende Tools plus Web-Abruf, kleineres Modell, liefert eine Zusammenfassung mit Quellen zurück und schreibt selbst nichts.
2. `ingest` so ändern, dass er Link-Eingänge an den `recherchierer` gibt.
3. Einen Link-Eingang verarbeiten und mit `/context` vergleichen: Wie viel Kontext hat die Recherche diesmal im Hauptgespräch belegt?

- **Vorher tippen:** Wie viel Kontext spart der Agent — 10 %, 50 % oder 90 %?
- **Warum:** Recherche bläht den Hauptkontext auf. Ein Agent arbeitet abgeschottet und liefert nur das Ergebnis zurück.
- **Fertig, wenn:** ein Link-Eingang landet als Notiz mit Quellen, ohne dass die ganze Webseite im Hauptkontext stand.
- **Prüfen:** Lest die neue Notiz gegen die verlinkte Seite. Steht etwas drin, was die Seite nicht hergibt? Wenn ja: Liegt es am kleineren Modell, an eurem Agenten-Prompt oder an der Weiterverarbeitung im Hauptgespräch?
- **In der Runde:** Welches Modell habt ihr gewählt, und hat es gereicht?
- **Für Schnelle:** Den `wissensarchitekt` selbst bauen — ein Agent, der neues Material gegen den Bestand prüft — und am Duplikat aus Übung 5 testen.
- **Musterlösung:** `06-agent`

## Übung „Eigener Agent“ (20 Min.)

Baut einen Agenten für eine Aufgabe aus **eurem** Arbeitsalltag — nicht fürs Handbuch. Ideen:

- Infrastruktur: ein `log-analyst`, der Logdateien oder Ausgaben von `kubectl`/`docker` liest und eine Fehlerdiagnose liefert, ohne etwas zu ändern
- Infrastruktur: ein `config-reviewer` für Dockerfiles, Pipelines oder Terraform, der gegen eure Konventionen prüft
- Entwicklung: ein `test-schreiber`, der zu einer Klasse fehlende Tests ergänzt und nur unter `src/test/` schreiben darf
- Review: ein `security-pruefer`, der einen Diff auf Geheimnisse, Injection und unsichere Defaults durchsieht

Wichtig sind die Entscheidungen im Frontmatter: Welche Tools braucht er wirklich (`tools`, `disallowedTools`)? Welches Modell reicht (`model`)? Darf er ohne Rückfrage arbeiten (`permissionMode`)? Was gibt er zurück? Dann einmal aus dem Hauptgespräch aufrufen — automatisch über die Beschreibung und gezielt mit `@`.

- **Vorher tippen:** Mit welchen Tools kommt euer Agent mindestens aus?
- **Prüfen:** Gebt ihm eine Aufgabe, für die er ein Werkzeug bräuchte, das ihr ihm nicht gegeben habt. Was passiert — scheitert er sauber, umgeht er es, oder fragt er?
- **In der Runde:** Zwei, drei Agenten vorstellen: Aufgabe, Tools, Modell, und was beim Prüfen herauskam.
- **Für Schnelle:** Gebt dem Agenten ein Gedächtnis (`memory: project`) und lasst ihn zweimal hintereinander laufen. Was merkt er sich, und gehört das ins Repo?
- **Zweites Beispiel:** `06-agent` zeigt mit dem `wissensarchitekt` einen Agenten, der neues Material gegen den Bestand prüft und Duplikate und Widersprüche meldet.

## Übung 7 — Hook auf `kb-check` (15 Min.)

1. Einen PostToolUse-Hook auf `Write|Edit` einrichten, der nach jedem Schreiben unter `notes/` das Prüfwerkzeug laufen lässt und Fehler an Claude zurückgibt (Exit-Code 2, Meldung auf stderr).
2. Claude bitten, in eine Notiz eine H1-Überschrift einzubauen, und zusehen, was passiert.
3. Dieselbe Frage wie in Übung 1 stellen: Was kostet der Hook an Tokens, was spart er?

- **Vorher tippen:** Merkt Claude ohne Hook, dass eine Notiz kaputt ist?
- **Warum:** Was jedes Mal passieren muss, gehört nicht in einen Prompt, sondern in einen Hook — deterministisch statt „hoffentlich“.
- **Fertig, wenn:** der Hook meldet die H1, und Claude reagiert darauf — er korrigiert sie oder fragt nach, weil ihr sie ausdrücklich verlangt habt.
- **Prüfen:** Testet den Hook ohne Claude, mit einem eigenen Ereignis auf stdin:
  `echo '{"tool_input":{"file_path":"notes/plan-mode.md"}}' | uv run .claude/hooks/check_note.py; echo $?`
  Dann den Hook absichtlich kaputt machen (falscher Pfad). Was sieht Claude, und was seht ihr?
- **In der Runde:** Was würdet ihr in eurem Team per Hook erzwingen statt per Rule erbitten?
- **Für Schnelle:** Ein PreToolUse-Hook, der jeden Shell-Befehl blockiert, der `.env` enthält — damit ist die Lücke aus Übung 3 zu. Warum reicht dafür eine Permission nicht?
- **Musterlösung:** `07-hook`

## Übung „Team-Verteilung“ (30 Min.)

1. Skill, Agenten, Hook und MCP-Server als Plugin `team-handbuch` unter `plugins/team-handbuch/` verpacken; die Skripte gehören mit ins Plugin.
2. Das Repo zum Marketplace machen: `.claude-plugin/marketplace.json` im Wurzelordner, prüfen mit `claude plugin validate .`.
3. Eure Nachbarin oder euer Nachbar installiert das Plugin aus eurem Repo in einem eigenen, leeren Projekt und verarbeitet dort einen Eingang.

- **Vorher tippen:** Was fehlt im leeren Nachbarprojekt, damit euer Plugin dort funktioniert?
- **Warum:** So verteilt ein Team seine Werkzeuge, ohne dass jeder abschreibt — versioniert, mit einem Befehl installiert, mit einem Befehl aktualisiert.
- **Fertig, wenn:** im Nachbarprojekt erscheint `/team-handbuch:ingest` und läuft.
- **Prüfen:** Der Nachbar sucht einen Fehler in eurem Plugin — einen Pfad, der nur in eurem Repo stimmt, eine Regel, die im Plugin fehlt. Plugins bringen keine Rules und keine CLAUDE.md mit: Wo stehen eure Konventionen jetzt?
- **In der Runde:** Was gehört ins Plugin, was bleibt im Repo?
- **Für Schnelle:** Version im Plugin erhöhen, etwas ändern, pushen — der Nachbar holt das Update mit `claude plugin marketplace update` und prüft, ob es ankommt.
- **Musterlösung:** `07b-plugin`

## Übung 8 — Abnahme (40 Min.)

1. Die fünf neuen Eingänge aus `extras/abnahme-inbox/` nach `inbox/` kopieren. Darunter sind ein Duplikat und ein Widerspruch.
2. `/loop 5m /ingest` die Inbox überwachen lassen.
3. Absichern: `/goal inbox/ ist leer und uv run tools/kb_check.py notes/ meldet keine Fehler; zeige die Ausgabe; höchstens 30 Runden`
4. Zum Schluss `/code-review` über alle Änderungen des Tages, dann committen.

- **Vorher tippen:** Welcher der fünf Eingänge geht schief, und wie?
- **Warum:** Alle Bausteine laufen ohne Zutun zusammen. Was jetzt noch Handarbeit braucht, zeigt, welcher Baustein fehlt.
- **Fertig, wenn:** die Inbox ist leer, `kb-check` meldet keine Fehler, `index.md` verlinkt alle neuen Notizen.
- **Prüfen:** `git diff` auf die Notiz, die der Widerspruch betrifft. Steht die alte Aussage noch da, mit Quelle, oder wurde sie still überschrieben? `kb-check` ist grün, so oder so — welche Prüfung fehlt also noch?
- **In der Runde:** Wie ist Claude mit Duplikat und Widerspruch umgegangen — erkannt oder einfach überschrieben?
- **Für Schnelle — und für alle mit eigenem leeren Repo:** Richtet dort das Handbuch für euer eigenes Team ein, per Plugin aus der Übung „Team-Verteilung“, und füllt es mit echtem Wissen: Architekturentscheidungen, Onboarding, Betriebswissen.
- **Musterlösung:** `08-final`

## Zusatzaufgaben

- **Statusline:** `/statusline` eine Statuszeile mit Modell, Kontextfüllstand und Branch bauen lassen.
- **Harness:** Im eigenen Agenten-Harness ([codevibe-de/agent-harness-py](https://github.com/codevibe-de/agent-harness-py), Stufe `03-tools`) ein Tool `kb_search` ergänzen, das den Code aus Übung 4 wiederverwendet.
- **Persönlicher Assistent:** dasselbe Muster für die eigenen Notizen, ergänzt um Kalender, Aufgaben und Mail per MCP.
- **Codex zum Vergleich:** die Abnahme einmal mit Codex und `AGENTS.md` wiederholen.

## Messblatt

Zum Ausfüllen während der Übungen. Die Kontextwerte stammen aus `/context` nach der Übung, die Tipps aus „Vorher tippen“.

| Übung | Minuten | Kontext nach der Übung | Getippt | Tatsächlich |
|---|---|---|---|---|
| 1 Ankommen | | | | |
| 2 `kb-check` | | | | |
| 3 Regeln | | | | |
| 4 MCP | | | | |
| 5 Skill | | | | |
| 6 Agent | | | | |
| Eigener Agent | | | | |
| 7 Hook | | | | |
| Team-Verteilung | | | | |
| 8 Abnahme | | | | |
