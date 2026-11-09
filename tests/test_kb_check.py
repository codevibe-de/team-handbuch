from pathlib import Path

import pytest

import kb_check

VALID = """---
titel: Beispiel
typ: wissen
tags: [test]
stand: 2026-11-05
---

Text mit Link auf [[andere]].
"""

OTHER = """---
titel: Andere
typ: glossar
tags: [test]
stand: 2026-11-05
---

Verweist zurück auf [[beispiel|das Beispiel]].
"""


@pytest.fixture
def handbook(tmp_path: Path, monkeypatch) -> Path:
    """A minimal handbook: index.md plus notes/ with two notes linking each other."""
    monkeypatch.chdir(tmp_path)
    notes = tmp_path / "notes"
    notes.mkdir()
    (notes / "beispiel.md").write_text(VALID, encoding="utf-8")
    (notes / "andere.md").write_text(OTHER, encoding="utf-8")
    (tmp_path / "index.md").write_text("- [[beispiel]]\n", encoding="utf-8")
    return notes


def messages(problems) -> list[str]:
    return [p.message for p in problems]


def test_valid_handbook_has_no_problems(handbook):
    problems, count = kb_check.check_paths([handbook])
    assert problems == []
    assert count == 2


def test_missing_frontmatter(handbook):
    (handbook / "beispiel.md").write_text("Nur Text, verlinkt [[andere]].\n", encoding="utf-8")
    problems, _ = kb_check.check_paths([handbook])
    assert "Frontmatter fehlt" in messages(problems)


def test_missing_required_field(handbook):
    (handbook / "beispiel.md").write_text(VALID.replace("typ: wissen\n", ""), encoding="utf-8")
    problems, _ = kb_check.check_paths([handbook])
    assert "Pflichtfeld 'typ' fehlt" in messages(problems)


def test_unknown_type(handbook):
    (handbook / "beispiel.md").write_text(VALID.replace("typ: wissen", "typ: roman"), encoding="utf-8")
    problems, _ = kb_check.check_paths([handbook])
    assert any(m.startswith("typ 'roman' ist nicht erlaubt") for m in messages(problems))


def test_stand_must_be_a_date(handbook):
    (handbook / "beispiel.md").write_text(VALID.replace("2026-11-05", "gestern"), encoding="utf-8")
    problems, _ = kb_check.check_paths([handbook])
    assert any("ist kein Datum" in m for m in messages(problems))


def test_invalid_yaml(handbook):
    (handbook / "beispiel.md").write_text(VALID.replace("tags: [test]", "tags: [test"), encoding="utf-8")
    problems, _ = kb_check.check_paths([handbook])
    assert any("kein gültiges YAML" in m for m in messages(problems))


def test_h1_is_reported_with_line_number(handbook):
    (handbook / "beispiel.md").write_text(VALID + "\n# Überschrift\n", encoding="utf-8")
    problems, _ = kb_check.check_paths([handbook])
    h1 = [p for p in problems if p.message.startswith("H1")]
    assert len(h1) == 1 and h1[0].line == 10


def test_h1_inside_code_block_is_ignored(handbook):
    (handbook / "beispiel.md").write_text(VALID + "\n```bash\n# Kommentar\n```\n", encoding="utf-8")
    problems, _ = kb_check.check_paths([handbook])
    assert problems == []


def test_broken_wikilink(handbook):
    (handbook / "beispiel.md").write_text(VALID + "\nSiehe [[gibt-es-nicht]].\n", encoding="utf-8")
    problems, _ = kb_check.check_paths([handbook])
    assert "Wikilink [[gibt-es-nicht]] zeigt ins Leere" in messages(problems)


def test_wikilink_with_heading_and_alias_resolves(handbook):
    (handbook / "beispiel.md").write_text(VALID + "\n[[andere#Abschnitt|dort]]\n", encoding="utf-8")
    problems, _ = kb_check.check_paths([handbook])
    assert problems == []


def test_wikilink_to_root_file_resolves(handbook):
    (handbook / "beispiel.md").write_text(VALID + "\nZurück zum [[index]].\n", encoding="utf-8")
    problems, _ = kb_check.check_paths([handbook])
    assert problems == []


def test_orphan_is_reported(handbook):
    (handbook / "allein.md").write_text(VALID.replace("Beispiel", "Allein"), encoding="utf-8")
    problems, _ = kb_check.check_paths([handbook])
    orphans = [p for p in problems if p.message.startswith("verwaist")]
    assert [p.path for p in orphans] == ["notes/allein.md"]


def test_self_link_does_not_prevent_orphan(handbook):
    text = VALID.replace("Beispiel", "Allein").replace("[[andere]]", "[[allein]]")
    (handbook / "allein.md").write_text(text, encoding="utf-8")
    problems, _ = kb_check.check_paths([handbook])
    assert any(p.path == "notes/allein.md" and p.message.startswith("verwaist") for p in problems)


def test_single_file_skips_orphan_check(handbook):
    (handbook / "allein.md").write_text(VALID.replace("Beispiel", "Allein"), encoding="utf-8")
    problems, count = kb_check.check_paths([handbook / "allein.md"])
    assert problems == [] and count == 1


def test_main_exit_codes(handbook, capsys):
    assert kb_check.main(["notes"]) == 0
    assert "OK" in capsys.readouterr().out
    (handbook / "beispiel.md").write_text(VALID + "\n# H1\n", encoding="utf-8")
    assert kb_check.main(["notes"]) == 1
    assert "notes/beispiel.md:10: H1" in capsys.readouterr().out
