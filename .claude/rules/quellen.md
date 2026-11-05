# Quellen und Widersprüche

- Jede Aussage in einer Notiz hat eine Quelle: der archivierte Eingang (`archive/…`) oder die URL, aus der sie stammt. Quellen stehen im Frontmatter unter `quellen`; im Text bei Bedarf mit Person und Datum, etwa „(Retro Sprint 42, 27. Oktober 2026)“.
- Protokolle, Mails und kopierte Artikel werden nie verändert. Sie wandern unverändert nach `archive/`, die Notiz fasst zusammen und verweist darauf.
- Ersetzt ein späterer Beschluss einen früheren ausdrücklich, wird die Notiz umgeschrieben und `stand` aktualisiert. Der alte Stand steht in der Git-Historie.
- Widerspricht eine neue Aussage einer vorhandenen, ohne sie ausdrücklich zu ersetzen, wird nichts überschrieben: Beide Aussagen bleiben mit Quelle stehen, die Notiz bekommt einen Abschnitt `## Offen` und `index.md` einen Eintrag unter „Offene Fragen“.
- Nichts erfinden. Was ein Eingang nicht hergibt, bleibt weg oder wird als offene Frage notiert.
