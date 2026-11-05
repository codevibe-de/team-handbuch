# Team-Handbuch Agentische Entwicklung

Übungsprojekt der Schulung „Agentische Entwicklung mit Claude Code“ von Codevibe IT-Seminare. Das Repo ist die Wissensbasis eines Entwicklungsteams, das Claude Code einführt: Entscheidungen, How-tos, Glossar. Neues Material landet in `inbox/`, Claude verarbeitet es zu Notizen in `notes/`, prüft sie und hält die Startseite `index.md` aktuell.

Über beide Seminartage kommt in jeder Übung genau ein Baustein dazu — CLAUDE.md, Spec, Rules und Permissions, MCP-Server, Skill, Agent, Hook, Plugin. Am Ende läuft das Handbuch ohne Handarbeit, und ihr nehmt eine Vorlage mit, die ihr im eigenen Team weiterführen könnt. Die Aufgaben stehen in [UEBUNGEN.md](UEBUNGEN.md).

## Voraussetzungen

- [Claude Code](https://code.claude.com/docs/en/setup), angemeldet mit Abo, Teams-Account oder API-Key
- Git
- [uv](https://docs.astral.sh/uv/getting-started/installation/) — führt die Python-Werkzeuge aus und installiert Python bei Bedarf selbst
- Node.js 20 oder neuer, nur für OpenSpec in Übung 2
- Optional [Obsidian](https://obsidian.md) als Viewer: den Repo-Ordner als Vault öffnen. Jeder andere Markdown-Viewer tut es auch.

Unter Windows läuft alles nativ; Claude Code braucht dort Git for Windows. Einzige Ausnahme ist die Sandbox, die es nur unter macOS, Linux und WSL2 gibt.

## Aufbau

```
team-handbuch/
├── inbox/               neue Eingänge: Links, Protokolle, Fragen, Notizen
├── notes/               verarbeitete Notizen, eine Datei je Thema
├── archive/             verarbeitete Eingänge, Protokolle unverändert
├── index.md             Startseite, verlinkt jede Notiz
├── tools/               Python-Werkzeuge, ausgeführt mit uv run
├── extras/              Material für spätere Übungen
└── .obsidian/           Viewer-Einstellungen, für Claude tabu
```

Eine Notiz hat Frontmatter mit `titel`, `typ` (`entscheidung`, `how-to`, `wissen`, `glossar` oder `frage`), `tags`, `stand` und `quellen`, und keine H1-Überschrift — der Titel steht im Frontmatter. Verlinkt wird mit `[[dateiname]]`.

## Stufen

Jede Übung hat einen Branch mit der Musterlösung. Wer hängen bleibt oder eine Übung verpasst hat, springt auf den Stand vor der nächsten Übung:

```bash
git stash -u            # eigene Änderungen beiseitelegen (oder committen)
git switch 04-mcp       # Stand nach Übung 4
```

| Branch | Stand nach | Kommt dazu |
|---|---|---|
| `main` = `00-start` | — | Ausgangsstand |
| `01-init` | Übung 1 | CLAUDE.md, aufgeräumtes `export.py`, erster Eingang verarbeitet |
| `02-kb-check` | Übung 2 | Spec und Prüfwerkzeug `kb-check` mit Tests |
| `03-rules` | Übung 3 | Rules, Permissions, zwei weitere Eingänge |
| `04-mcp` | Übung 4 | MCP-Server `kb-search` |
| `05-skill` | Übung 5 | Skill `ingest` |
| `06-agent` | Übung 6 | Agenten `recherchierer` und `wissensarchitekt` |
| `07-hook` | Übung 7 | Hook, der `kb-check` nach jedem Schreiben laufen lässt |
| `07b-plugin` | Team-Verteilung | Plugin `team-handbuch` im Marketplace dieses Repos |
| `08-final` | Übung 8 | Inbox leer, alle Notizen geprüft |

`git diff 03-rules 04-mcp` zeigt genau, was eine Stufe hinzufügt.

## Werkzeuge

```bash
uv run tools/export.py              # Tag-Statistik als Markdown-Tabelle
uv run tools/kb_check.py notes/     # Notizen prüfen (ab 02-kb-check)
uv run pytest                       # Tests (ab 02-kb-check)
```

## Plugin installieren

Ab `07b-plugin` ist dieses Repo zugleich ein Plugin-Marketplace. So holt sich ein anderes Team Skill, Agenten, Hook und MCP-Server in sein eigenes Repo:

```bash
claude plugin marketplace add codevibe-de/team-handbuch
claude plugin install team-handbuch@codevibe-de
```
