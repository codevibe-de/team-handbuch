---
titel: Skills
typ: wissen
tags: [claude-code, kontext]
stand: 2026-10-22
quellen:
  - archive/2026-10-22-link-skills.md
  - https://code.claude.com/docs/en/skills
---

„Nur gespeicherte Prompts“ (Deniz, 22. Oktober 2026) stimmt nicht ganz. Ein Skill ist ein Ordner mit einer `SKILL.md` und beliebigen weiteren Dateien — Vorlagen, Beispiele, Skripte.

## Was ihn von einem gespeicherten Prompt unterscheidet

- **Nur bei Bedarf im Kontext.** Zu Beginn kennt Claude nur Name und Beschreibung. Den Rest lädt er erst, wenn der Skill passt — und weitere Dateien erst, wenn er sie braucht.
- **Automatisch oder per Befehl.** Claude wählt den Skill anhand der Beschreibung selbst aus; per `/name` lässt er sich gezielt aufrufen.
- **Mit Werkzeugen.** Ein Skill kann Skripte mitbringen, die Claude ausführt, statt alles selbst zu schreiben, und mit `allowed-tools` Freigaben für seine Dauer erteilen.
- **Auch abgeschottet.** Mit `context: fork` läuft er in einem eigenen Subagenten (siehe [[subagenten]]).

Orte: `.claude/skills/` im Repo fürs Team, `~/.claude/skills/` persönlich, oder als Teil eines [[plugins]].

Unser Beispiel ist `ingest`, der die Inbox verarbeitet. Wann Skill, wann Rule: siehe [[skill-oder-rule]].
