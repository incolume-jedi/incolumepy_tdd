"""Principal Module."""

from toml import load
from pathlib import Path

__author__ = '@britodfbr'

configfile = Path(__file__).parents[2].joinpath('pyproject.toml')
versionfile = Path(__file__).parent.joinpath('version.txt')

versionfile.write_text(
    f"{load(configfile)['tool']['poetry']['version']}\n",
)

__version__ = versionfile.read_text().split()
