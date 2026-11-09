---
titel: Plugins und Marketplace — Werkzeuge mit anderen Teams teilen
typ: how-to
tags: [claude-code, team]
stand: 2026-11-05
quellen:
  - archive/2026-11-04-link-plugins.md
  - archive/2026-11-05-frage-nachbarteam.md
  - https://code.claude.com/docs/en/plugins
---

Ein **Plugin** bündelt Skills, Agenten, Hooks und MCP-Server in einem Ordner mit einem Manifest `.claude-plugin/plugin.json`. Ein **Marketplace** ist ein Verzeichnis von Plugins, beschrieben in `.claude-plugin/marketplace.json` — meist einfach ein Git-Repo.

## Antwort ans Nachbarteam

Die Frage des Logistik-Teams (5. November 2026): Abschreiben ist nicht nötig. Dieses Repo ist selbst ein Marketplace, das Plugin `team-handbuch` enthält `ingest`, beide Agenten, den Prüf-Hook und den MCP-Server `kb-search`:

```bash
claude plugin marketplace add codevibe-de/team-handbuch
claude plugin install team-handbuch@codevibe-de
```

Im eigenen Repo braucht das Nachbarteam nur die Ordner `inbox/`, `notes/`, `archive/` und eine `index.md`. Der Skill heißt dort `/team-handbuch:ingest`. Updates kommen mit `claude plugin marketplace update`.

## Was ein Plugin nicht kann

Rules und CLAUDE.md lädt Claude Code aus Plugins nicht. Unsere Konventionen stecken deshalb im Skill selbst; was jedes Mal gelten muss, sichert der Hook (siehe [[hooks]] und [[skills]]).
