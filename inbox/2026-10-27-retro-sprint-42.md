Protokoll Retro Sprint 42, 27. Oktober 2026
Anwesend: Anna, Ben, Carla, Deniz, Emil
Protokoll: Ben

Was lief gut
- Plan Mode bei größeren Änderungen hat sich bewährt (siehe Carlas Blogbeitrag)
- Erste Tests mit dem Figma MCP laufen

Was lief schlecht
- Jede/r hat andere Freigaben für Claude, Emil hatte `rm` erlaubt, Anna musste jeden `git status` bestätigen
- Zwei Mal hat Claude eine `.env` gelesen und den Inhalt in die Antwort geschrieben
- Token-Verbrauch im Oktober fast verdoppelt

Beschlüsse
1. Permissions werden vereinheitlicht: Die gemeinsamen Freigaben und Verbote stehen ab sofort in `.claude/settings.json` im Repo. `.claude/settings.local.json` nur noch für persönliche Ausnahmen. Verantwortlich: Deniz.
2. Lesen von `.env`-Dateien wird für alle verboten (Deny-Regel). Verantwortlich: Deniz.
3. Anna schaut sich bis Sprint 44 an, wie wir den Token-Verbrauch senken.
