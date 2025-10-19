from pathlib import Path

__all__ = ['version']

VERSION_FILE = Path(__file__).resolve().parent.parent / 'VERSION'
try:
    version = VERSION_FILE.read_text().strip()
except Exception:
    version = '0.0.0'
# qro_project package
from pathlib import Path

# Read semantic version from the top-level VERSION file so code and releases stay in sync.
try:
    __version__ = Path(__file__).resolve().parent.parent.joinpath("VERSION").read_text().strip()
except Exception:
    __version__ = "0.0.0"