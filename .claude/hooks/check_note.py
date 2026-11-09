# /// script
# requires-python = ">=3.12"
# dependencies = ["pyyaml>=6"]
# ///
"""PostToolUse hook: run kb-check on a note right after Claude wrote or edited it.

Claude Code passes the tool call as JSON on stdin. Problems go to stderr with
exit code 2, which hands them back to Claude so it fixes them right away.
"""

import json
import os
import sys
from pathlib import Path

PROJECT = Path(os.environ.get("CLAUDE_PROJECT_DIR") or Path(__file__).resolve().parents[2])
sys.path.insert(0, str(PROJECT / "tools"))

from kb_check import check_paths  # noqa: E402


def main() -> int:
    event = json.loads(sys.stdin.buffer.read() or b"{}")
    file_path = event.get("tool_input", {}).get("file_path")
    if not file_path:
        return 0
    path = Path(file_path).resolve()
    notes = (PROJECT / "notes").resolve()
    if path.suffix != ".md" or path.parent != notes or not path.exists():
        return 0
    os.chdir(PROJECT)
    problems, _ = check_paths([path])
    if not problems:
        return 0
    print(f"kb-check meldet Probleme in {path.name} — bitte beheben:", file=sys.stderr)
    for problem in problems:
        print(f"  {problem}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
