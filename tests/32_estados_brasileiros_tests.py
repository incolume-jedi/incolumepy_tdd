"""
# TODO: Atividade 32: Extração de dados Web.
Com dados extraídos do sítio https://www.todamateria.com.br/estados-do-brasil/
construa um arquivo estados.json, com registros de orientação "records"
contendo [estado, sigla, capital].
"""
from pathlib import Path
import json
import base64
from incolume.py.tdd.json_files.estados import url, path

__author__ = '@britodfbr'


def test_url():
    """Test url."""
    assert 'https://www.todamateria.com.br/estados-do-brasil/' in url


def test_exite_path():
    assert path.exists(), f'Ops: {path} não existe.'


def test_path():
    """"""
    expected = (
        Path(__file__)
        .parents[1]
        .joinpath('incolume', 'py', 'tdd', 'json_files')
    )
    assert path == expected


def test_exite_dir():
    assert path.is_dir(), f'Ops: {path} não é um diretório'


def test_json_file():
    file = path / 'estados.json'
    assert file.is_file(), f'Not Found: {file}'


def test_content_json():
    s = (
        'W3siZXN0YWRvIjogIkFjcmUiLCAic2lnbGEiOiAiQUMiLCAiY2FwaXRhbCI6'
        'ICJSaW8gQnJhbmNvIn0sIHsiZXN0YWRvIjogIkFsYWdvYXMiLCAic2lnbGEi'
        'OiAiQUwiLCAiY2FwaXRhbCI6ICJNYWNlaVx1MDBmMyJ9LCB7ImVzdGFkbyI6'
        'ICJBbWFwXHUwMGUxIiwgInNpZ2xhIjogIkFQIiwgImNhcGl0YWwiOiAiTWFj'
        'YXBcdTAwZTEifSwgeyJlc3RhZG8iOiAiQW1hem9uYXMiLCAic2lnbGEiOiAi'
        'QU0iLCAiY2FwaXRhbCI6ICJNYW5hdXMifSwgeyJlc3RhZG8iOiAiQmFoaWEi'
        'LCAic2lnbGEiOiAiQkEiLCAiY2FwaXRhbCI6ICJTYWx2YWRvciJ9LCB7ImVz'
        'dGFkbyI6ICJDZWFyXHUwMGUxIiwgInNpZ2xhIjogIkNFIiwgImNhcGl0YWwi'
        'OiAiRm9ydGFsZXphIn0sIHsiZXN0YWRvIjogIkVzcFx1MDBlZHJpdG8gU2Fu'
        'dG8iLCAic2lnbGEiOiAiRVMiLCAiY2FwaXRhbCI6ICJWaXRcdTAwZjNyaWEi'
        'fSwgeyJlc3RhZG8iOiAiR29pXHUwMGUxcyIsICJzaWdsYSI6ICJHTyIsICJj'
        'YXBpdGFsIjogIkdvaVx1MDBlMm5pYSJ9LCB7ImVzdGFkbyI6ICJNYXJhbmhc'
        'dTAwZTNvIiwgInNpZ2xhIjogIk1BIiwgImNhcGl0YWwiOiAiU1x1MDBlM28g'
        'THVcdTAwZWRzIn0sIHsiZXN0YWRvIjogIk1hdG8gR3Jvc3NvIiwgInNpZ2xh'
        'IjogIk1UIiwgImNhcGl0YWwiOiAiQ3VpYWJcdTAwZTEifSwgeyJlc3RhZG8i'
        'OiAiTWF0byBHcm9zc28gZG8gU3VsIiwgInNpZ2xhIjogIk1TIiwgImNhcGl0'
        'YWwiOiAiQ2FtcG8gR3JhbmRlIn0sIHsiZXN0YWRvIjogIk1pbmFzIEdlcmFp'
        'cyIsICJzaWdsYSI6ICJNRyIsICJjYXBpdGFsIjogIkJlbG8gSG9yaXpvbnRl'
        'In0sIHsiZXN0YWRvIjogIlBhclx1MDBlMSIsICJzaWdsYSI6ICJQQSIsICJj'
        'YXBpdGFsIjogIkJlbFx1MDBlOW0ifSwgeyJlc3RhZG8iOiAiUGFyYVx1MDBl'
        'ZGJhIiwgInNpZ2xhIjogIlBCIiwgImNhcGl0YWwiOiAiSm9cdTAwZTNvIFBl'
        'c3NvYSJ9LCB7ImVzdGFkbyI6ICJQYXJhblx1MDBlMSIsICJzaWdsYSI6ICJQ'
        'UiIsICJjYXBpdGFsIjogIkN1cml0aWJhIn0sIHsiZXN0YWRvIjogIlBlcm5h'
        'bWJ1Y28iLCAic2lnbGEiOiAiUEUiLCAiY2FwaXRhbCI6ICJSZWNpZmUifSwg'
        'eyJlc3RhZG8iOiAiUGlhdVx1MDBlZCIsICJzaWdsYSI6ICJQSSIsICJjYXBp'
        'dGFsIjogIlRlcmVzaW5hIn0sIHsiZXN0YWRvIjogIlJpbyBkZSBKYW5laXJv'
        'IiwgInNpZ2xhIjogIlJKIiwgImNhcGl0YWwiOiAiUmlvIGRlIEphbmVpcm8i'
        'fSwgeyJlc3RhZG8iOiAiUmlvIEdyYW5kZSBkbyBOb3J0ZSIsICJzaWdsYSI6'
        'ICJSTiIsICJjYXBpdGFsIjogIk5hdGFsIn0sIHsiZXN0YWRvIjogIlJpbyBH'
        'cmFuZGUgZG8gU3VsIiwgInNpZ2xhIjogIlJTIiwgImNhcGl0YWwiOiAiUG9y'
        'dG8gQWxlZ3JlIn0sIHsiZXN0YWRvIjogIlJvbmRcdTAwZjRuaWEiLCAic2ln'
        'bGEiOiAiUk8iLCAiY2FwaXRhbCI6ICJQb3J0byBWZWxobyJ9LCB7ImVzdGFk'
        'byI6ICJSb3JhaW1hIiwgInNpZ2xhIjogIlJSIiwgImNhcGl0YWwiOiAiQm9h'
        'IFZpc3RhIn0sIHsiZXN0YWRvIjogIlNhbnRhIENhdGFyaW5hIiwgInNpZ2xh'
        'IjogIlNDIiwgImNhcGl0YWwiOiAiRmxvcmlhblx1MDBmM3BvbGlzIn0sIHsi'
        'ZXN0YWRvIjogIlNcdTAwZTNvIFBhdWxvIiwgInNpZ2xhIjogIlNQIiwgImNh'
        'cGl0YWwiOiAiU1x1MDBlM28gUGF1bG8ifSwgeyJlc3RhZG8iOiAiU2VyZ2lw'
        'ZSIsICJzaWdsYSI6ICJTRSIsICJjYXBpdGFsIjogIkFyYWNhanUifSwgeyJl'
        'c3RhZG8iOiAiVG9jYW50aW5zIiwgInNpZ2xhIjogIlRPIiwgImNhcGl0YWwi'
        'OiAiUGFsbWFzIn1d'
    )
    c = base64.b64decode(s.encode('ascii', 'strict')).decode('ascii')
    d = json.loads(c)

    file = path.joinpath('estados.json')
    e = json.load(file.open())
    assert d == e
