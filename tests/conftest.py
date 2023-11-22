"""Configure switch test."""
from pathlib import Path
from sys import version_info

import pytest

from incolumepy.tdd import genfile


collect_ignore = [
    'incolumepy/static_html',
]


if version_info < (3, 10, 0):  # noqa: UP036
    collect_ignore.extend(
        (
            'incolume/py/dojo20220720',
            'incolume/py/dojo20220808',
            'incolume/py/dojo20220910',
        ),
    )


@pytest.fixture(scope='session')
def semver_regex() -> str:
    """Fixture para regex de validação do Versionamento Semântico."""
    return r'^\d+(\.\d+){2}((-\w+\.\d+)|(\w+\d+))?$'


@pytest.fixture()
def fakefile() -> Path:
    """Return fiction file for tests."""
    return genfile(prefix='File-testing-')
