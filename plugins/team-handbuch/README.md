# Plugin team-handbuch

Macht aus einem beliebigen Repo ein Team-Handbuch: Material in `inbox/` ablegen, `/team-handbuch:ingest` aufrufen, fertig.

| Baustein | Was er tut |
|---|---|
| Skill `ingest` | verarbeitet die Inbox zu Notizen, richtet das Handbuch beim ersten Aufruf ein |
| Agent `recherchierer` | fasst Links zusammen, ohne den Hauptkontext zu füllen |
| Agent `wissensarchitekt` | prüft neues Material auf Duplikate und Widersprüche |
| Hook | prüft jede geschriebene Notiz in `notes/` mit `kb-check` |
| MCP-Server `kb-search` | Volltextsuche, Backlinks und Tags im Handbuch des Projekts |

Installation:

```bash
claude plugin marketplace add codevibe-de/team-handbuch
claude plugin install team-handbuch@codevibe-de
```

Voraussetzung ist [uv](https://docs.astral.sh/uv/). Die Skripte unter `scripts/` sind Kopien aus `tools/` und `.claude/hooks/` des Handbuch-Repos.
