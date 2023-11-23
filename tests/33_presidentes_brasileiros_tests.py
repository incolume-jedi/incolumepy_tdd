"""
# TODO:: Atividade 33: Do endereço https://pt.m.wikipedia.org/wiki/Lista_de_presidentes_do_Brasil, extraia as
informações dos presidentes brasileiros e grave em um arquivo chamado presidentes_com_fotos.json, contendo Presidente,
 Vice-presidente, início e fim de mandato, partido político, url da fotografia e suas respectivas fotos em formato
  binário.
"""
from pathlib import Path
from incolumepy.tdd import __root__
import json
import base64
import pytest
import pandas as pd


__author__ = '@britodfbr'
path = Path(__root__) / 'src' / 'incolumepy' / 'tdd' / 'json_files'
file = path.joinpath('presidentes_com_fotos.json')


@pytest.fixture
def content_json():
    with Path(__file__).parent.joinpath('presidentes_com_fotos.b64').open() as f:
        s = f.read()
    c = base64.b64decode(s.encode('ascii', 'strict')).decode('ascii')
    return json.loads(c)


@pytest.fixture
def content_file():
    with file.open() as f:
        return json.load(f)


def test_exite_path():
    assert path.exists(), f'Ops: {path} não existe.'


def test_exite_dir():
    assert path.is_dir(), f'Ops: {path} não é um diretório'


def test_json_file():
    assert file.exists(), f'Arquivo inexistente: {file}'
    assert file.is_file(), f'Arquivo inválido: {file}'


# @pytest.mark.skip(reason="no way of currently testing this")
def test_content_json(content_json, content_file):
    e = json.load(file.open())
    df = pd.DataFrame(content_file)
    assert df.columns.all() in ['PRESIDENTE', 'PARTIDO', 'VICE-PRESIDENTE', 'INICIO_MANDATO',
                                'FIM_MANDATO', 'URL_FOTOGRAFIA', 'FOTOGRAFIA'], "Campos insuficientes ou inválidos"
    assert content_json == e, "Arquivo incorreto ou inconsistente"
