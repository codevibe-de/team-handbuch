---
titel: Hooks
typ: wissen
tags: [claude-code, automatisierung]
stand: 2026-10-21
quellen:
  - archive/2026-10-21-link-hooks.md
  - https://code.claude.com/docs/en/hooks-guide
---

Ein Hook ist ein Befehl, den Claude Code bei einem bestimmten Ereignis selbst ausführt — nicht das Modell entscheidet darüber, sondern die Konfiguration. Was jedes Mal passieren muss, gehört deshalb in einen Hook statt in einen Prompt.

## Ereignisse, die wir brauchen

- `PreToolUse` — vor einem Werkzeugaufruf; kann ihn blockieren
- `PostToolUse` — nach einem Werkzeugaufruf; kann Claude eine Rückmeldung geben
- `SessionStart`, `UserPromptSubmit`, `Stop`, `Notification` für Einstieg, Prompt, Ende und Benachrichtigungen

Gibt der Befehl Exit-Code 2 zurück, landet seine Fehlerausgabe bei Claude, und Claude reagiert darauf.

## Beispiele aus unserem Alltag

- **Handbuch:** Nach jedem Schreiben in `notes/` läuft `kb-check`; Fehler gehen an Claude zurück, der sie sofort behebt (`.claude/settings.json`).
- **Code:** Nach jeder Änderung an einer Java-Datei den Formatter laufen lassen.
- **Sicherheit:** Vor jedem Bash-Befehl prüfen, ob er Produktionsdaten berührt, und ihn dann blockieren.

Hooks laufen mit den Rechten des Benutzers. Fremde Hooks vor dem Einchecken lesen. Siehe auch [[permissions]] und [[skills]].
