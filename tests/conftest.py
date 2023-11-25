"""Configure switch test."""
import unittest
import tempfile
from typing import final

from faker import Faker
from collections import namedtuple
from pathlib import Path
from sys import version_info

import pytest
from incolume.py.tdd import genfile

collect_ignore = [
    'incolume/py/static_html',
]

if version_info < (3, 10, 0):  # noqa: UP036
    collect_ignore.extend(
        (
            'incolume/py/dojo20220720',
            'incolume/py/dojo20220808',
            'incolume/py/dojo20220910',
        ),
    )

LOREMIPSUM: final = """Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Mauris sit amet lorem fringilla, consectetur nulla non, finibus nibh.
Suspendisse elementum orci nunc, quis tempus ante convallis ut. Fusce rutrum
 velit id commodo cursus. Fusce sagittis rhoncus consequat. Aliquam quis
 volutpat nunc. Duis quis tellus urna. Nunc in semper metus.
Cras ut semper nulla, in mattis eros. Aenean consectetur ex ex, varius
condimentum augue aliquet in. Pellentesque habitant morbi tristique senectus
et netus et malesuada fames ac turpis egestas. Proin purus sapien,
volutpat sed volutpat a, condimentum id ipsum. Maecenas fringilla turpis
et libero commodo, volutpat sollicitudin risus blandit. Phasellus id odio
eu arcu porttitor eleifend id nec nisl. Vestibulum placerat urna sagittis,
ullamcorper tellus at, suscipit leo.

Suspendisse consectetur scelerisque tincidunt. Vestibulum lorem erat,
ullamcorper non tortor vitae, dignissim finibus eros. Curabitur metus nisi,
semper vel fringilla ut, rutrum sed diam. Nam at orci in dui placerat
interdum eget sed augue. Proin ut tempus purus. Duis in est mi. Duis
efficitur justo ac erat rutrum vestibulum eu ac metus. Sed sit amet
sollicitudin arcu. Sed lacinia faucibus porta. Quisque rutrum est ligula,
eget aliquet dui sodales in. Morbi viverra sem at felis vehicula molestie.
Aenean lacinia ipsum tempus, pretium augue ac, scelerisque ex. Morbi sit
amet diam et eros varius pharetra vitae sit amet eros. Suspendisse vitae
enim ac nulla volutpat lobortis quis ac ligula.

Aenean ligula turpis, rutrum sit amet aliquam nec, tristique vel sapien.
Vivamus tincidunt lacus vel eros ornare facilisis. Maecenas feugiat tempus
fermentum. Aliquam erat volutpat. Curabitur pulvinar, nibh quis lacinia
lobortis, libero elit ultrices justo, a molestie magna urna sit amet magna.
Proin et faucibus magna, at scelerisque diam. Phasellus ut tristique purus.

Nunc et venenatis mi, sit amet pretium ligula. Aenean pellentesque, quam ut
porta condimentum, sapien ante pulvinar augue, et pretium elit magna ac magna.
Proin vitae hendrerit est, eleifend posuere lacus. Vestibulum vulputate velit
sed arcu porta, et vulputate diam pretium. Donec eu neque mauris. Integer
venenatis porttitor feugiat. Aenean sed lectus et orci pulvinar dignissim a
et sem. Etiam nec nunc et libero semper suscipit eu a lorem.

Cras sagittis mauris at sem ultrices, vitae imperdiet ex aliquam. Morbi
maximus quam nec nulla viverra rhoncus. Pellentesque non leo ut lorem pretium
mattis. Donec venenatis eros placerat, eleifend erat eu, consectetur ipsum.
Cras sem leo, tincidunt id turpis eu, cursus convallis leo. Aenean at
tincidunt enim. Quisque sodales dui vel massa imperdiet, ut gravida magna
dictum. Aliquam pulvinar suscipit fermentum. Nunc in ligula sem. Ut
sollicitudin fringilla posuere. Proin erat tellus, semper ac ullamcorper in,
mollis sit amet tortor."""


@pytest.fixture(scope='session')
def semver_regex() -> str:
    """Fixture para regex de validação do Versionamento Semântico."""
    return r'^\d+(\.\d+){2}((-\w+\.\d+)|(\w+\d+))?$'


@pytest.fixture()
def fakefile() -> Path:
    """Return fiction file for tests."""
    return genfile(prefix='File-testing-')


@pytest.fixture()
def loremipsum() -> str:
    """Content."""
    return LOREMIPSUM
