import subprocess

import jsonl5


def test_version():
    version_from_pyproject = subprocess.check_output(
        ["uv", "version", "--short"]
    ).decode().strip()
    
    assert jsonl5.__version__ == version_from_pyproject
