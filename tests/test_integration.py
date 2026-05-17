import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_main_smoke_all_sections():
    result = subprocess.run(
        [sys.executable, "main.py", "--section", "all"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr


def test_pandas_intro_script_registered():
    result = subprocess.run(
        ["uv", "run", "pandas-intro", "--section", "basics"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr
