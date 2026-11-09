---
titel: Kontextfenster, Token, Kompaktierung
typ: glossar
tags: [grundlagen, kosten]
stand: 2026-10-30
quellen:
  - archive/2026-10-30-notiz-glossar.md
---

**Token** — die Einheit, in der Modelle Text zählen, grob 3 bis 4 Zeichen. Abgerechnet wird in Token, und das Kontextfenster ist in Token begrenzt.

**Kontextfenster** — alles, was das Modell in einem Aufruf sieht: System-Prompt, CLAUDE.md, bisheriger Verlauf und jedes Werkzeugergebnis. Was nicht darin steht, weiß das Modell nicht; was darin steht, kostet bei jedem Aufruf erneut.

**Kompaktierung** — wird der Kontext voll, fasst Claude Code den bisherigen Verlauf zusammen und macht damit weiter. Von Hand mit `/compact`, ganz neu anfangen mit `/clear`.

Siehe auch [[agent-loop]].
