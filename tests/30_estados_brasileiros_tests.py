"""
# TODO: Atividade 30:  Com dados extraídos do sítio https://www.todamateria.com.br/estados-do-brasil/
construa um arquivo .json, com registros de orientação "records" contendo [estado, sigla, capital].
"""
import unittest
from pathlib import Path
from incolumepy.tdd import __root__
import json
import base64

__author__ = '@britodfbr'
path = Path(__root__) / 'src'/'incolumepy' / 'tdd' / 'json_files'


def test_exite_path():
    assert path.exists(), f'Ops: {path} não existe.'


def test_exite_dir():
    assert path.is_dir(), f'Ops: {path} não é um diretório'


def test_json_file():
    file = path.joinpath('estados.json')
    assert file.exists(), f'Ops: {file}'


def test_content_json():
    s = 'W3siZXN0YWRvIjogIkFjcmUiLCAic2lnbGEiOiAiQUMiLCAiY2FwaXRhbCI6ICJSaW8gQnJhbmNvIn0sIHsiZ' \
        'XN0YWRvIjogIkFsYWdvYXMiLCAic2lnbGEiOiAiQUwiLCAiY2FwaXRhbCI6ICJNYWNlaVx1MDBmMyJ9LCB7Im' \
        'VzdGFkbyI6ICJBbWFwXHUwMGUxIiwgInNpZ2xhIjogIkFQIiwgImNhcGl0YWwiOiAiTWFjYXBcdTAwZTEifSw' \
        'geyJlc3RhZG8iOiAiQW1hem9uYXMiLCAic2lnbGEiOiAiQU0iLCAiY2FwaXRhbCI6ICJNYW5hdXMifSwgeyJl' \
        'c3RhZG8iOiAiQmFoaWEiLCAic2lnbGEiOiAiQkEiLCAiY2FwaXRhbCI6ICJTYWx2YWRvciJ9LCB7ImVzdGFkb' \
        'yI6ICJDZWFyXHUwMGUxIiwgInNpZ2xhIjogIkNFIiwgImNhcGl0YWwiOiAiRm9ydGFsZXphIn0sIHsiZXN0YW' \
        'RvIjogIkVzcFx1MDBlZHJpdG8gU2FudG8iLCAic2lnbGEiOiAiRVMiLCAiY2FwaXRhbCI6ICJWaXRcdTAwZjN' \
        'yaWEifSwgeyJlc3RhZG8iOiAiR29pXHUwMGUxcyIsICJzaWdsYSI6ICJHTyIsICJjYXBpdGFsIjogIkdvaVx1' \
        'MDBlMm5pYSJ9LCB7ImVzdGFkbyI6ICJNYXJhbmhcdTAwZTNvIiwgInNpZ2xhIjogIk1BIiwgImNhcGl0YWwiO' \
        'iAiU1x1MDBlM28gTHVcdTAwZWRzIn0sIHsiZXN0YWRvIjogIk1hdG8gR3Jvc3NvIiwgInNpZ2xhIjogIk1UIi' \
        'wgImNhcGl0YWwiOiAiQ3VpYWJcdTAwZTEifSwgeyJlc3RhZG8iOiAiTWF0byBHcm9zc28gZG8gU3VsIiwgInN' \
        'pZ2xhIjogIk1TIiwgImNhcGl0YWwiOiAiQ2FtcG8gR3JhbmRlIn0sIHsiZXN0YWRvIjogIk1pbmFzIEdlcmFp' \
        'cyIsICJzaWdsYSI6ICJNRyIsICJjYXBpdGFsIjogIkJlbG8gSG9yaXpvbnRlIn0sIHsiZXN0YWRvIjogIlBhc' \
        'lx1MDBlMSIsICJzaWdsYSI6ICJQQSIsICJjYXBpdGFsIjogIkJlbFx1MDBlOW0ifSwgeyJlc3RhZG8iOiAiUG' \
        'FyYVx1MDBlZGJhIiwgInNpZ2xhIjogIlBCIiwgImNhcGl0YWwiOiAiSm9cdTAwZTNvIFBlc3NvYSJ9LCB7ImV' \
        'zdGFkbyI6ICJQYXJhblx1MDBlMSIsICJzaWdsYSI6ICJQUiIsICJjYXBpdGFsIjogIkN1cml0aWJhIn0sIHsi' \
        'ZXN0YWRvIjogIlBlcm5hbWJ1Y28iLCAic2lnbGEiOiAiUEUiLCAiY2FwaXRhbCI6ICJSZWNpZmUifSwgeyJlc' \
        '3RhZG8iOiAiUGlhdVx1MDBlZCIsICJzaWdsYSI6ICJQSSIsICJjYXBpdGFsIjogIlRlcmVzaW5hIn0sIHsiZX' \
        'N0YWRvIjogIlJpbyBkZSBKYW5laXJvIiwgInNpZ2xhIjogIlJKIiwgImNhcGl0YWwiOiAiUmlvIGRlIEphbmV' \
        'pcm8ifSwgeyJlc3RhZG8iOiAiUmlvIEdyYW5kZSBkbyBOb3J0ZSIsICJzaWdsYSI6ICJSTiIsICJjYXBpdGFs' \
        'IjogIk5hdGFsIn0sIHsiZXN0YWRvIjogIlJpbyBHcmFuZGUgZG8gU3VsIiwgInNpZ2xhIjogIlJTIiwgImNhc' \
        'Gl0YWwiOiAiUG9ydG8gQWxlZ3JlIn0sIHsiZXN0YWRvIjogIlJvbmRcdTAwZjRuaWEiLCAic2lnbGEiOiAiUk' \
        '8iLCAiY2FwaXRhbCI6ICJQb3J0byBWZWxobyJ9LCB7ImVzdGFkbyI6ICJSb3JhaW1hIiwgInNpZ2xhIjogIlJ' \
        'SIiwgImNhcGl0YWwiOiAiQm9hIFZpc3RhIn0sIHsiZXN0YWRvIjogIlNhbnRhIENhdGFyaW5hIiwgInNpZ2xh' \
        'IjogIlNDIiwgImNhcGl0YWwiOiAiRmxvcmlhblx1MDBmM3BvbGlzIn0sIHsiZXN0YWRvIjogIlNcdTAwZTNvI' \
        'FBhdWxvIiwgInNpZ2xhIjogIlNQIiwgImNhcGl0YWwiOiAiU1x1MDBlM28gUGF1bG8ifSwgeyJlc3RhZG8iOi' \
        'AiU2VyZ2lwZSIsICJzaWdsYSI6ICJTRSIsICJjYXBpdGFsIjogIkFyYWNhanUifSwgeyJlc3RhZG8iOiAiVG9' \
        'jYW50aW5zIiwgInNpZ2xhIjogIlRPIiwgImNhcGl0YWwiOiAiUGFsbWFzIn1d'
    c = base64.b64decode(s.encode('ascii', 'strict')).decode('ascii')
    d = json.loads(c)

    file = path.joinpath('estados.json')
    e = json.load(file.open())
    assert d == e
