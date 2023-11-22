"""Principal Module."""
from tempfile import NamedTemporaryFile

from tomli import load
from pathlib import Path

__author__ = '@britodfbr'

configfile = Path(__file__).parents[2].joinpath('pyproject.toml')
versionfile = Path(__file__).parent.joinpath('version.txt')

with configfile.open('rb') as stream:
    versionfile.write_text(f"{load(stream)['tool']['poetry']['version']}\n")

__version__ = versionfile.read_text().strip()


def genfile(prefix: str = '', suffix: str = '') -> Path:
    """Return empty file."""
    return Path(NamedTemporaryFile(prefix=prefix, suffix=suffix).name)
