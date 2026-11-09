"""Black-box tests for tools/kb_check.py: one folder per case under tests/faelle/.

A case is a tiny handbook: an index.md plus a notes/ folder. The folder name
says what kb_check must do with it:

    ok-...       must pass   (exit code 0)
    fehler-...   must fail   (exit code 1, without crashing)

The test only looks at the exit code, not at the messages, so it works however
kb_check.py is built inside. To add a case, copy ok-minimal, change exactly one
thing and name the folder after the expected result.
"""

import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
KB_CHECK = ROOT / "tools" / "kb_check.py"
CASES = sorted(p for p in (Path(__file__).parent / "faelle").iterdir() if p.is_dir())


@pytest.mark.skipif(not KB_CHECK.exists(), reason="tools/kb_check.py gibt es noch nicht (Übung 2)")
@pytest.mark.parametrize("case", CASES, ids=lambda p: p.name)
def test_fall(case: Path) -> None:
    result = subprocess.run(
        ["uv", "run", str(KB_CHECK), "notes/"],
        cwd=case,
        capture_output=True,
        text=True,
    )
    output = result.stdout + result.stderr
    # A Python crash also exits with 1, so it must not count as "found the error".
    assert "Traceback" not in output, f"kb_check ist bei {case.name} abgestürzt:\n{output}"
    if case.name.startswith("ok-"):
        assert result.returncode == 0, f"{case.name} sollte durchgehen:\n{output}"
    elif case.name.startswith("fehler-"):
        assert result.returncode == 1, f"{case.name} sollte scheitern:\n{output}"
    else:
        pytest.fail(f"Ordnername muss mit ok- oder fehler- beginnen: {case.name}")
