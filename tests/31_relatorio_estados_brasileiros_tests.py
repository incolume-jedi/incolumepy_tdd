"""
# TODO: Atividade 31:  Com dados extraídos do sítio https://www.todamateria.com.br/estados-do-brasil/
construa um arquivo .json, com registros em orientação "records" contendo: estado, sigla, capital e as informações do
IBGE, exceto datas. Os campos/colunas devem ser em formato ASCII com "_" no lugar de espaços.
"""
from pathlib import Path
from incolumepy.tdd import __root__
import base64
import json
import pytest

__author__ = '@britodfbr'
path = Path(__root__) / 'src'/'incolumepy' / 'tdd' / 'json_files'
file = path.joinpath('ibge.json')


def test_exite_path():
    assert path.exists(), f'Ops: {path} não existe.'


def test_exite_dir():
    assert path.is_dir(), f'Ops: {path} não é um diretório'


def test_json_file():
    assert file.exists(), f'Ops: {file}'


def test_content_json():
    s = "W3siRVNUQURPIjogIkFjcmUiLCAiU0lHTEEiOiAiQUMiLCAiQ0FQSVRBTCI6ICJSaW8gQnJhbmNvIiwgIkdFTlRJTElDTyI6ICJ" \
        "xdWVtIG5hc2NlIG5vIEVzdGFkbyBkbyBBY3JlIFx1MDBlOSBhY3JlYW5vIG91IGFjcmlhbm8iLCAiUE9QVUxBQ0FPIjogIjgyOS" \
        "42MTkgaGFiaXRhbnRlcyAoZXN0aW1hdGl2YSBJQkdFLCAyMDE3KSIsICJOVU1FUk9fREVfTVVOSUNJUElPUyI6ICIyMiIsICJFQ" \
        "09OT01JQSI6ICJleHRyYVx1MDBlN1x1MDBlM28gZGEgY2FzdGFuaGEgZG8gQnJhc2lsIiwgIkNMSU1BIjogImVxdWF0b3JpYWwi" \
        "LCAiUFJJTkNJUEFJU19SSU9TIjogIlRhcmF1YWNcdTAwZTEsIFB1cnVzLCBHcmVnXHUwMGYzcmlvLCBFbnZpcmEsIEFjcmUgZSB" \
        "KdXJ1XHUwMGUxIn0sIHsiRVNUQURPIjogIkFtYXBcdTAwZTEiLCAiU0lHTEEiOiAiQVAiLCAiQ0FQSVRBTCI6ICJNYWNhcFx1MD" \
        "BlMSIsICJHRU5USUxJQ08iOiAicXVlbSBuYXNjZSBubyBFc3RhZG8gZG8gQW1hcFx1MDBlMSBcdTAwZTkgYW1hcGFlbnNlIiwgI" \
        "lBPUFVMQUNBTyI6ICI3OTcuNzIyIGhhYml0YW50ZXMgKGVzdGltYXRpdmEgSUJHRSwgMjAxNykiLCAiTlVNRVJPX0RFX01VTklD" \
        "SVBJT1MiOiAiMTYiLCAiRUNPTk9NSUEiOiAiZXh0cmF0aXZpc21vIG1pbmVyYWwgZSB2ZWdldGFsIiwgIkNMSU1BIjogImVxdWF" \
        "0b3JpYWwiLCAiUFJJTkNJUEFJU19SSU9TIjogIkFyYWd1YXJpLCBPaWFwb3F1ZSwgQW1hcGFyaSBlIEFtYXBcdTAwZTEgR3Jhbm" \
        "RlIn0sIHsiRVNUQURPIjogIkFtYXpvbmFzIiwgIlNJR0xBIjogIkFNIiwgIkNBUElUQUwiOiAiTWFuYXVzIiwgIkdFTlRJTElDT" \
        "yI6ICJxdWVtIG5hc2NlIG5vIEVzdGFkbyBkbyBBbWF6b25hcyBcdTAwZTkgYW1hem9uZW5zZSIsICJQT1BVTEFDQU8iOiAiNC4w" \
        "NjMuNjE0IGhhYml0YW50ZXMgKGVzdGltYXRpdmEgSUJHRSwgMjAxNykiLCAiTlVNRVJPX0RFX01VTklDSVBJT1MiOiAiNjIiLCA" \
        "iRUNPTk9NSUEiOiAiYWdyaWN1bHR1cmEsIHBlY3VcdTAwZTFyaWEsIGV4dHJhdGl2aXNtbyB2ZWdldGFsIiwgIkNMSU1BIjogIm" \
        "VxdWF0b3JpYWwiLCAiUFJJTkNJUEFJU19SSU9TIjogIkFtYXpvbmFzLCBQdXJ1cywgVGFwYWpcdTAwZjNzLCBYaW5ndSwgTmVnc" \
        "m8gZSBUcm9tYmV0YXMifSwgeyJFU1RBRE8iOiAiUGFyXHUwMGUxIiwgIlNJR0xBIjogIlBBIiwgIkNBUElUQUwiOiAiQmVsXHUw" \
        "MGU5bSIsICJHRU5USUxJQ08iOiAicXVlbSBuYXNjZSBubyBFc3RhZG8gZG8gUGFyXHUwMGUxIFx1MDBlOSBwYXJhZW5zZSIsICJ" \
        "QT1BVTEFDQU8iOiAiOC4zNjYuNjI4IGhhYml0YW50ZXMgKGVzdGltYXRpdmEgSUJHRSwgMjAxNykiLCAiTlVNRVJPX0RFX01VTk" \
        "lDSVBJT1MiOiAiMTQ0IiwgIkVDT05PTUlBIjogImFncmljdWx0dXJhLCBwZWN1XHUwMGUxcmlhLCBleHRyYXRpdmlzbW8gbWluZ" \
        "XJhbCBlIHZlZ2V0YWwsIGluZFx1MDBmYXN0cmlhIGUgdHVyaXNtbyIsICJDTElNQSI6ICJlcXVhdG9yaWFsIiwgIlBSSU5DSVBB" \
        "SVNfUklPUyI6ICJBbWF6b25hcywgVGFwYWpcdTAwZjNzLCBUb2NhbnRpbnMsIFhpbmd1LCBKYXJpIGUgUGFyXHUwMGUxIn0sIHs" \
        "iRVNUQURPIjogIlJvbmRcdTAwZjRuaWEiLCAiU0lHTEEiOiAiUk8iLCAiQ0FQSVRBTCI6ICJQb3J0byBWZWxobyIsICJHRU5USU" \
        "xJQ08iOiAicXVlbSBuYXNjZSBubyBFc3RhZG8gZGUgUm9uZFx1MDBmNG5pYSBcdTAwZTkgcm9uZG9uaWVuc2Ugb3Ugcm9uZG9ua" \
        "WFubyIsICJQT1BVTEFDQU8iOiAiMS44MDUuNzg4IGhhYml0YW50ZXMgKGVzdGltYXRpdmEgSUJHRSwgMjAxNykiLCAiTlVNRVJP" \
        "X0RFX01VTklDSVBJT1MiOiAiNTIiLCAiRUNPTk9NSUEiOiAicGVjdVx1MDBlMXJpYSBkZSBjb3J0ZSwgYWdyaWN1bHR1cmEsIGV" \
        "4dHJhdGl2aXNtbyBtaW5lcmFsIGUgdmVnZXRhbCIsICJDTElNQSI6ICJlcXVhdG9yaWFsIiwgIlBSSU5DSVBBSVNfUklPUyI6IC" \
        "JNYWRlaXJhLCBKaS1QYXJhblx1MDBlMSwgR3VhcG9yXHUwMGU5IGUgTWFtb3JcdTAwZTkifSwgeyJFU1RBRE8iOiAiUm9yYWltY" \
        "SIsICJTSUdMQSI6ICJSUiIsICJDQVBJVEFMIjogIkJvYSBWaXN0YSIsICJHRU5USUxJQ08iOiAicXVlbSBuYXNjZSBubyBFc3Rh" \
        "ZG8gZGUgUm9yYWltYSBcdTAwZTkgcm9yYWltZW5zZSIsICJQT1BVTEFDQU8iOiAiNTIyLjYzNiBoYWJpdGFudGVzIChlc3RpbWF" \
        "0aXZhIElCR0UsIDIwMTcpIiwgIk5VTUVST19ERV9NVU5JQ0lQSU9TIjogIjE1IiwgIkVDT05PTUlBIjogImFncmljdWx0dXJhIC" \
        "hwcm9kdVx1MDBlN1x1MDBlM28gZGUgYXJyb3opLCBleHRyYXRpdmlzbW8gbWluZXJhbCIsICJDTElNQSI6ICJ0cm9waWNhbCBlI" \
        "GVxdWF0b3JpYWwgXHUwMGZhbWlkbyIsICJQUklOQ0lQQUlTX1JJT1MiOiAiQnJhbmNvLCBDYXRyaW1hbmksIE11Y2FqYVx1MDBl" \
        "ZCwgVGFjdXR1IGUgQW5hdVx1MDBlMSJ9LCB7IkVTVEFETyI6ICJUb2NhbnRpbnMiLCAiU0lHTEEiOiAiVE8iLCAiQ0FQSVRBTCI" \
        "6ICJQYWxtYXMiLCAiR0VOVElMSUNPIjogInF1ZW0gbmFzY2Ugbm8gRXN0YWRvIGRvIFRvY2FudGlucyBcdTAwZTkgdG9jYW50aW" \
        "5lbnNlIiwgIlBPUFVMQUNBTyI6ICIxLjU1MC4xOTQgaGFiaXRhbnRlcyAoZXN0aW1hdGl2YSBJQkdFLCAyMDE3KSIsICJOVU1FU" \
        "k9fREVfTVVOSUNJUElPUyI6ICIxMzkiLCAiRUNPTk9NSUEiOiAiYWdyaWN1bHR1cmEsIHBlY3VcdTAwZTFyaWEgZSBjb21cdTAw" \
        "ZTlyY2lvIiwgIkNMSU1BIjogInRyb3BpY2FsIiwgIlBSSU5DSVBBSVNfUklPUyI6ICJUb2NhbnRpbnMsIEFyYWd1YWlhLCBQYXJ" \
        "hblx1MDBlMSwgU29ubyBlIEJhbHNhcyJ9LCB7IkVTVEFETyI6ICJNYXJhbmhcdTAwZTNvIiwgIlNJR0xBIjogIk1BIiwgIkNBUE" \
        "lUQUwiOiAiU1x1MDBlM28gTHVcdTAwZWRzIiwgIkdFTlRJTElDTyI6ICJxdWVtIG5hc2NlIG5vIEVzdGFkbyBkbyBNYXJhbmhcd" \
        "TAwZTNvIFx1MDBlOSBtYXJhbmhlbnNlIiwgIlBPUFVMQUNBTyI6ICI3LjAwMC4yMjkgaGFiaXRhbnRlcyAoZXN0aW1hdGl2YSBJ" \
        "QkdFLCAyMDE3KSIsICJOVU1FUk9fREVfTVVOSUNJUElPUyI6ICIyMTciLCAiRUNPTk9NSUEiOiAiYWdyaWN1bHR1cmEsIHBlY3V" \
        "cdTAwZTFyaWEsIGluZFx1MDBmYXN0cmlhLCBleHRyYXRpdmlzbW8gdmVnZXRhbCBlIHNlcnZpXHUwMGU3b3MiLCAiQ0xJTUEiOi" \
        "AidHJvcGljYWwiLCAiUFJJTkNJUEFJU19SSU9TIjogIlRvY2FudGlucywgR3VydXBpLCBQaW5kYXJcdTAwZTksIFBhcm5hXHUwM" \
        "GVkYmEgZSBJdGFwZWN1cnUifSwgeyJFU1RBRE8iOiAiUGlhdVx1MDBlZCIsICJTSUdMQSI6ICJQSSIsICJDQVBJVEFMIjogIlRl" \
        "cmVzaW5hIiwgIkdFTlRJTElDTyI6ICJxdWVtIG5hc2NlIG5vIEVzdGFkbyBkbyBQaWF1XHUwMGVkIFx1MDBlOSBwaWF1aWVuc2U" \
        "iLCAiUE9QVUxBQ0FPIjogIjMuMjE5LjI1NyBoYWJpdGFudGVzIChlc3RpbWF0aXZhIElCR0UsIDIwMTcpIiwgIk5VTUVST19ERV" \
        "9NVU5JQ0lQSU9TIjogIjIyNCIsICJFQ09OT01JQSI6ICJhZ3JpY3VsdHVyYSwgcGVjdVx1MDBlMXJpYSwgc2VydmlcdTAwZTdvc" \
        "yBlIGluZFx1MDBmYXN0cmlhIiwgIkNMSU1BIjogInRyb3BpY2FsIGUgc2VtaVx1MDBlMXJpZG8iLCAiUFJJTkNJUEFJU19SSU9T" \
        "IjogIlBhcm5hXHUwMGVkYmEsIFBvdGksIENhbmluZFx1MDBlOSwgUGlhdVx1MDBlZCBlIFNcdTAwZTNvIE5pY29sYXUifSwgeyJ" \
        "FU1RBRE8iOiAiQ2Vhclx1MDBlMSIsICJTSUdMQSI6ICJDRSIsICJDQVBJVEFMIjogIkZvcnRhbGV6YSIsICJHRU5USUxJQ08iOi" \
        "AicXVlbSBuYXNjZSBubyBFc3RhZG8gZG8gQ2Vhclx1MDBlMSBcdTAwZTkgY2VhcmVuc2UiLCAiUE9QVUxBQ0FPIjogIjkuMDIwL" \
        "jQ2MCBoYWJpdGFudGVzIChlc3RpbWF0aXZhIElCR0UsIDIwMTcpIiwgIk5VTUVST19ERV9NVU5JQ0lQSU9TIjogIjE4NCIsICJF" \
        "Q09OT01JQSI6ICJhZ3JvcGVjdVx1MDBlMXJpYSwgY29tXHUwMGU5cmNpbywgc2VydmlcdTAwZTdvcywgZXh0cmF0aXZpc21vIG1" \
        "pbmVyYWwsIHR1cmlzbW8iLCAiQ0xJTUEiOiAidHJvcGljYWwiLCAiUFJJTkNJUEFJU19SSU9TIjogIkFjYXJhXHUwMGZhLCBDb2" \
        "5jZWlcdTAwZTdcdTAwZTNvLCBKYWd1YXJpYmUsIFBhY290aSwgUGlyYW5qaSBlIFNhbGdhZG8ifSwgeyJFU1RBRE8iOiAiUmlvI" \
        "EdyYW5kZSBkbyBOb3J0ZSIsICJTSUdMQSI6ICJSTiIsICJDQVBJVEFMIjogIk5hdGFsIiwgIkdFTlRJTElDTyI6ICJxdWVtIG5h" \
        "c2NlIG5vIFJpbyBHcmFuZGUgZG8gTm9ydGUgXHUwMGU5IHBvdGlndWFyLCBub3J0ZS1yaW8tZ3JhbmRlbnNlIG91IHJpby1ncmF" \
        "uZGVuc2UtZG8tbm9ydGUiLCAiUE9QVUxBQ0FPIjogIjMuNTA3LjAwMyBoYWJpdGFudGVzIChlc3RpbWF0aXZhIElCR0UsIDIwMT" \
        "cpIiwgIk5VTUVST19ERV9NVU5JQ0lQSU9TIjogIjE2NyIsICJFQ09OT01JQSI6ICJ0dXJpc21vLCBhZ3JvcGVjdVx1MDBlMXJpY" \
        "SwgZnJ1dGljdWx0dXJhLCBleHRyYVx1MDBlN1x1MDBlM28gZGUgc2FsLCBpbmRcdTAwZmFzdHJpYSBlIGNvbVx1MDBlOXJjaW8i" \
        "LCAiQ0xJTUEiOiAic2VtaVx1MDBlMXJpZG8iLCAiUFJJTkNJUEFJU19SSU9TIjogIk1vc3Nvclx1MDBmMywgUGlyYW5oYXMsIFB" \
        "vdGVuZ3VpLCBKYWN1LCBTZXJpZFx1MDBmMyBlIEN1cmltYXRhXHUwMGZhIn0sIHsiRVNUQURPIjogIlBhcmFcdTAwZWRiYSIsIC" \
        "JTSUdMQSI6ICJQQiIsICJDQVBJVEFMIjogIkpvXHUwMGUzbyBQZXNzb2EiLCAiR0VOVElMSUNPIjogInF1ZW0gbmFzY2Ugbm8gR" \
        "XN0YWRvIGRhIFBhcmFcdTAwZWRiYSBcdTAwZTkgcGFyYWliYW5vIiwgIlBPUFVMQUNBTyI6ICI0LjAyNS41NTggaGFiaXRhbnRl" \
        "cyAoZXN0aW1hdGl2YSBJQkdFLCAyMDE3KSIsICJOVU1FUk9fREVfTVVOSUNJUElPUyI6ICIyMjMiLCAiRUNPTk9NSUEiOiAiYWd" \
        "yb3BlY3VcdTAwZTFyaWEsIGluZFx1MDBmYXN0cmlhICh0ZWNpZG9zLCBjYWxcdTAwZTdhZG9zLCBhbGltZW50b3MsIGJlYmlkYX" \
        "MpLCBjb21cdTAwZTlyY2lvLCB0dXJpc21vIiwgIkNMSU1BIjogInRyb3BpY2FsIGUgc2VtaVx1MDBlMXJpZG8iLCAiUFJJTkNJU" \
        "EFJU19SSU9TIjogIlBhcmFcdTAwZWRiYSwgVGFwZXJvXHUwMGUxLCBDdXJpbWF0YVx1MDBmYSwgUGlyYW5oYXMgZSBNYW1hbmd1" \
        "YXBlIn0sIHsiRVNUQURPIjogIlBlcm5hbWJ1Y28iLCAiU0lHTEEiOiAiUEUiLCAiQ0FQSVRBTCI6ICJSZWNpZmUiLCAiR0VOVEl" \
        "MSUNPIjogInF1ZW0gbmFzY2Ugbm8gRXN0YWRvIGRvIFBlcm5hbWJ1Y28gXHUwMGU5IHBlcm5hbWJ1Y2FubyIsICJQT1BVTEFDQU" \
        "8iOiAiOS40NzMuMjY2IGhhYml0YW50ZXMgKGVzdGltYXRpdmEgSUJHRSwgMjAxNykiLCAiTlVNRVJPX0RFX01VTklDSVBJT1MiO" \
        "iAiMTg1IiwgIkVDT05PTUlBIjogImFncmljdWx0dXJhLCBwZWN1XHUwMGUxcmlhLCB0dXJpc21vLCBpbmRcdTAwZmFzdHJpYSAo" \
        "YWxpbWVudFx1MDBlZGNpYSwgbWV0YWxcdTAwZmFyZ2ljYSwgbmF2YWwsIGF1dG9tb2JpbFx1MDBlZHN0aWNhLCBlbGV0cm9lbGV" \
        "0clx1MDBmNG5pY2EsIHF1XHUwMGVkbWljYSwgdFx1MDBlYXh0aWwpIiwgIkNMSU1BIjogInRyb3BpY2FsIGUgdHJvcGljYWwgXH" \
        "UwMGZhbWlkbyIsICJQUklOQ0lQQUlTX1JJT1MiOiAiU1x1MDBlM28gRnJhbmNpc2NvLCBQYWplXHUwMGZhLCBNb3hvdFx1MDBmM" \
        "ywgQ2FwaWJhcmliZSBlIElwb2p1Y2EifSwgeyJFU1RBRE8iOiAiQWxhZ29hcyIsICJTSUdMQSI6ICJBTCIsICJDQVBJVEFMIjog" \
        "Ik1hY2VpXHUwMGYzIiwgIkdFTlRJTElDTyI6ICJxdWVtIG5hc2NlIG5vIEVzdGFkbyBkbyBBbGFnb2FzIFx1MDBlOSBhbGFnb2F" \
        "ubyIsICJQT1BVTEFDQU8iOiAiMy4zNzUuODIzIGhhYml0YW50ZXMgKGVzdGltYXRpdmEgSUJHRSwgMjAxNykiLCAiTlVNRVJPX0" \
        "RFX01VTklDSVBJT1MiOiAiMTAyIiwgIkVDT05PTUlBIjogImFncm9wZWN1XHUwMGUxcmlhLCB0dXJpc21vIGUgaW5kXHUwMGZhc" \
        "3RyaWEgZGUgcGV0cm9xdVx1MDBlZG1pY29zIiwgIkNMSU1BIjogInRyb3BpY2FsIiwgIlBSSU5DSVBBSVNfUklPUyI6ICJTXHUw" \
        "MGUzbyBGcmFuY2lzY28sIE11bmRhXHUwMGZhIGUgUGFyYVx1MDBlZGJhIGRvIE1laW8ifSwgeyJFU1RBRE8iOiAiU2VyZ2lwZSI" \
        "sICJTSUdMQSI6ICJTRSIsICJDQVBJVEFMIjogIkFyYWNhanUiLCAiR0VOVElMSUNPIjogInF1ZW0gbmFzY2Ugbm8gRXN0YWRvIG" \
        "RvIFNlcmdpcGUgXHUwMGU5IHNlcmdpcGFubyBvdSBzZXJnaXBlbnNlIiwgIlBPUFVMQUNBTyI6ICIyLjI4OC4xMTYgaGFiaXRhb" \
        "nRlcyAoZXN0aW1hdGl2YSBJQkdFLCAyMDE3KSIsICJOVU1FUk9fREVfTVVOSUNJUElPUyI6ICI3NSIsICJFQ09OT01JQSI6ICJh" \
        "Z3JvcGVjdVx1MDBlMXJpYSwgaW5kXHUwMGZhc3RyaWEsIGV4dHJhdGl2aXNtbyBtaW5lcmFsIGUgc2VydmlcdTAwZTdvcyIsICJ" \
        "DTElNQSI6ICJ0cm9waWNhbCBhdGxcdTAwZTJudGljbyBlIHNlbWlcdTAwZTFyaWRvIiwgIlBSSU5DSVBBSVNfUklPUyI6ICJTXH" \
        "UwMGUzbyBGcmFuY2lzY28sIFZhemEtQmFycmlzLCBSZWFsLCBQaWF1XHUwMGVkIGUgSmFwYXR1YmEifSwgeyJFU1RBRE8iOiAiQ" \
        "mFoaWEiLCAiU0lHTEEiOiAiQkEiLCAiQ0FQSVRBTCI6ICJTYWx2YWRvciIsICJHRU5USUxJQ08iOiAicXVlbSBuYXNjZSBubyBF" \
        "c3RhZG8gZGEgQmFoaWEgXHUwMGU5IGJhaWFubyIsICJQT1BVTEFDQU8iOiAiMTUuMzQ0LjQ0NyBoYWJpdGFudGVzIChlc3RpbWF" \
        "0aXZhIElCR0UsIDIwMTcpIiwgIk5VTUVST19ERV9NVU5JQ0lQSU9TIjogIjQxNyIsICJFQ09OT01JQSI6ICJhZ3JvcGVjdVx1MD" \
        "BlMXJpYSwgZXh0cmF0aXZpc21vIG1pbmVyYWwsIGluZFx1MDBmYXN0cmlhLCB0dXJpc21vIGUgc2VydmlcdTAwZTdvcyIsICJDT" \
        "ElNQSI6ICJ0cm9waWNhbCIsICJQUklOQ0lQQUlTX1JJT1MiOiAiU1x1MDBlM28gRnJhbmNpc2NvLCBQYXJhZ3VhXHUwMGU3dSwg" \
        "SmVxdWl0aW5ob25oYSBlIEl0YXBlY3VydSJ9LCB7IkVTVEFETyI6ICJHb2lcdTAwZTFzIiwgIlNJR0xBIjogIkdPIiwgIkNBUEl" \
        "UQUwiOiAiR29pXHUwMGUybmlhIiwgIkdFTlRJTElDTyI6ICJxdWVtIG5hc2NlIG5vIEVzdGFkbyBkZSBHb2lcdTAwZTFzIFx1MD" \
        "BlOSBnb2lhbm8iLCAiUE9QVUxBQ0FPIjogIjYuNzc4Ljc3MiBoYWJpdGFudGVzIChlc3RpbWF0aXZhLCBJQkdFIDIwMTcpIiwgI" \
        "k5VTUVST19ERV9NVU5JQ0lQSU9TIjogIjI0NiIsICJFQ09OT01JQSI6ICJhZ3JvcGVjdVx1MDBlMXJpYSwgY29tXHUwMGU5cmNp" \
        "bywgaW5kXHUwMGZhc3RyaWEgKG1ldGFsXHUwMGZhcmdpY2EsIG1pbmVyYVx1MDBlN1x1MDBlM28sIGFsaW1lbnRvcywgY29uZmV" \
        "jXHUwMGU3XHUwMGY1ZXMpLCB0dXJpc21vIiwgIkNMSU1BIjogInRyb3BpY2FsIiwgIlBSSU5DSVBBSVNfUklPUyI6ICJBcG9yXH" \
        "UwMGU5LCBBcmFndWFpYSwgUGFyYW5cdTAwZTEsIFBhcmFuYVx1MDBlZGJhIGUgTWFyYW5oXHUwMGUzbyJ9LCB7IkVTVEFETyI6I" \
        "CJNYXRvIEdyb3NzbyIsICJTSUdMQSI6ICJNVCIsICJDQVBJVEFMIjogIkN1aWFiXHUwMGUxIiwgIkdFTlRJTElDTyI6ICJxdWVt" \
        "IG5hc2NlIG5vIEVzdGFkbyBkbyBNYXRvIEdyb3NzbyBcdTAwZTkgbWF0by1ncm9zc2Vuc2UiLCAiUE9QVUxBQ0FPIjogIjMuMzQ" \
        "0LjU0NCBoYWJpdGFudGVzIChlc3RpbWF0aXZhIElCR0UsIDIwMTcpIiwgIk5VTUVST19ERV9NVU5JQ0lQSU9TIjogIjE0MSIsIC" \
        "JFQ09OT01JQSI6ICJhZ3JvcGVjdVx1MDBlMXJpYSwgYWdyb25lZ1x1MDBmM2NpbywgZXh0cmF0aXZpc21vIG1pbmVyYWwsIHZlZ" \
        "2V0YWwgZSB0dXJpc21vIiwgIkNMSU1BIjogInRyb3BpY2FsIiwgIlBSSU5DSVBBSVNfUklPUyI6ICJKdXJ1ZW5hLCBBcmFndWFp" \
        "YSwgWGluZ3UsIFBhcmFndWFpLCBDdWlhYlx1MDBlMSBlIFBpcXVlcmkifSwgeyJFU1RBRE8iOiAiTWF0byBHcm9zc28gZG8gU3V" \
        "sIiwgIlNJR0xBIjogIk1TIiwgIkNBUElUQUwiOiAiQ2FtcG8gR3JhbmRlIiwgIkdFTlRJTElDTyI6ICJxdWVtIG5hc2NlIG5vIE" \
        "VzdGFkbyBcdTAwZTkgc3VsLW1hdG8tZ3Jvc3NlbnNlIG91IG1hdG8tZ3Jvc3NlbnNlLWRvLXN1bCIsICJQT1BVTEFDQU8iOiAiM" \
        "i43MTMuMTQ3IGhhYml0YW50ZXMgKGVzdGltYXRpdmEgSUJHRSwgMjAxNykiLCAiTlVNRVJPX0RFX01VTklDSVBJT1MiOiAiNzci" \
        "LCAiRUNPTk9NSUEiOiAiYWdyaWN1bHR1cmEsIHBlY3VcdTAwZTFyaWEsIGV4dHJhdGl2aXNtbyBtaW5lcmFsLCB2ZWdldGFsLCB" \
        "pbmRcdTAwZmFzdHJpYSBlIHR1cmlzbW8iLCAiQ0xJTUEiOiAidHJvcGljYWwiLCAiUFJJTkNJUEFJU19SSU9TIjogIkFxdWlkYX" \
        "VhbmEsIFBhcmFndWFpLCBQYXJhbmFcdTAwZWRiYSwgUGFyYW5cdTAwZTEgZSBOZWdybyJ9LCB7IkVTVEFETyI6ICJEaXN0cml0b" \
        "yBGZWRlcmFsIiwgIlNJR0xBIjogIkRGIiwgIkNBUElUQUwiOiAiQnJhc1x1MDBlZGxpYSIsICJHRU5USUxJQ08iOiAicXVlbSBu" \
        "YXNjZSBubyBEaXN0cml0byBGZWRlcmFsIFx1MDBlOSBicmFzaWxpZW5zZSIsICJQT1BVTEFDQU8iOiAiMy4wMzkuNDQ0IGhhYml" \
        "0YW50ZXMgKGVzdGltYXRpdmEgSUJHRSwgMjAxNykiLCAiTlVNRVJPX0RFX01VTklDSVBJT1MiOiAiMSIsICJFQ09OT01JQSI6IC" \
        "JhZ3JpY3VsdHVyYSwgcGVjdVx1MDBlMXJpYSwgY29tXHUwMGU5cmNpbywgc2VydmlcdTAwZTdvcyBlIGluZFx1MDBmYXN0cmlhI" \
        "ChleHRyYXRpdmlzdGEsIHRyYW5zZm9ybWFcdTAwZTdcdTAwZTNvLCB0cmFuc3BvcnRlLCBwZXNxdWVpcmEgZSBhbGltZW50XHUw" \
        "MGVkY2lhKSIsICJDTElNQSI6ICJ0cm9waWNhbCIsICJQUklOQ0lQQUlTX1JJT1MiOiAiUHJldG8sIFBhcmFub1x1MDBlMSBlIFN" \
        "cdTAwZTNvIEJhcnRvbG9tZXUifSwgeyJFU1RBRE8iOiAiU1x1MDBlM28gUGF1bG8iLCAiU0lHTEEiOiAiU1AiLCAiQ0FQSVRBTC" \
        "I6ICJTXHUwMGUzbyBQYXVsbyIsICJHRU5USUxJQ08iOiAicXVlbSBuYXNjZSBubyBFc3RhZG8gZGUgU1x1MDBlM28gUGF1bG8gX" \
        "HUwMGU5IHBhdWxpc3RhIiwgIlBPUFVMQUNBTyI6ICI0NS4wOTQuODY2IGhhYml0YW50ZXMgKGVzdGltYXRpdmEgSUJHRSwgMjAx" \
        "NykiLCAiTlVNRVJPX0RFX01VTklDSVBJT1MiOiAiNjQ1IiwgIkVDT05PTUlBIjogImFncmljdWx0dXJhLCBwZWN1XHUwMGUxcml" \
        "hLCBpbmRcdTAwZmFzdHJpYXMgKG1lY1x1MDBlMm5pY2EsIHRcdTAwZWF4dGlsLCBhXHUwMGU3XHUwMGZhY2FyLCBcdTAwZTFsY2" \
        "9vbCwgYXV0b21vYmlsXHUwMGVkc3RpY2EsIGF2aWFcdTAwZTdcdTAwZTNvKSwgc2VydmlcdTAwZTdvcyBlIHR1cmlzbW8iLCAiQ" \
        "0xJTUEiOiAidHJvcGljYWwgYXRsXHUwMGUybnRpY28gZSB0cm9waWNhbCBkZSBhbHRpdHVkZSIsICJQUklOQ0lQQUlTX1JJT1Mi" \
        "OiAiUGFyYW5hcGFuZW1hLCBUaWV0XHUwMGVhLCBQYXJhXHUwMGVkYmEgZG8gU3VsIGUgUGlyYWNpY2FiYSJ9LCB7IkVTVEFETyI" \
        "6ICJSaW8gZGUgSmFuZWlybyIsICJTSUdMQSI6ICJSSiIsICJDQVBJVEFMIjogIlJpbyBkZSBKYW5laXJvIiwgIkdFTlRJTElDTy" \
        "I6ICJxdWVtIG5hc2NlIG5vIFJpbyBkZSBKYW5laXJvIFx1MDBlOSBmbHVtaW5lbnNlIiwgIlBPUFVMQUNBTyI6ICIxNi43MTguO" \
        "TU2IGhhYml0YW50ZXMgKGVzdGltYXRpdmEgSUJHRSwgMjAxNykiLCAiTlVNRVJPX0RFX01VTklDSVBJT1MiOiAiOTIiLCAiRUNP" \
        "Tk9NSUEiOiAiaW5kXHUwMGZhc3RyaWEgKGFsaW1lbnRcdTAwZWRjaWEsIHBldHJvcXVcdTAwZWRtaWNhLCBzaWRlclx1MDBmYXJ" \
        "naWNhLCBtZXRhbFx1MDBmYXJnaWNhLCBmYXJtYWNcdTAwZWF1dGljYSwgbmF2YWwsIGF1dG9tb2JpbFx1MDBlZHN0aWNhLCBtZW" \
        "NcdTAwZTJuaWNhLCBhdWRpb3Zpc3VhbCwgdFx1MDBlYXh0aWwpLCBleHRyYVx1MDBlN1x1MDBlM28gbWluZXJhbCwgY29tXHUwM" \
        "GU5cmNpbywgc2VydmlcdTAwZTdvcyBlIHR1cmlzbW8iLCAiQ0xJTUEiOiAidHJvcGljYWwgYXRsXHUwMGUybnRpY28iLCAiUFJJ" \
        "TkNJUEFJU19SSU9TIjogIkdyYW5kZSwgTXVyaWFcdTAwZTksIFBhcmFcdTAwZWRiYSBkbyBTdWwsIE1hY2FcdTAwZTksIFBpcmF" \
        "cdTAwZWQifSwgeyJFU1RBRE8iOiAiTWluYXMgR2VyYWlzIiwgIlNJR0xBIjogIk1HIiwgIkNBUElUQUwiOiAiQmVsbyBIb3Jpem" \
        "9udGUiLCAiR0VOVElMSUNPIjogInF1ZW0gbmFzY2Ugbm8gRXN0YWRvIGRlIE1pbmFzIEdlcmFpcyBcdTAwZTkgbWluZWlybyIsI" \
        "CJQT1BVTEFDQU8iOiAiMjEuMTE5LjUzNiBoYWJpdGFudGVzIChlc3RpbWF0aXZhIElCR0UsIDIwMTcpIiwgIk5VTUVST19ERV9N" \
        "VU5JQ0lQSU9TIjogIjg1MyIsICJFQ09OT01JQSI6ICJhZ3JvcGVjdVx1MDBlMXJpYSwgaW5kXHUwMGZhc3RyaWEgKG1ldGFsdXJ" \
        "naWEsIHNpZGVydXJnaWEsIG1pbmVyYWlzIG1ldFx1MDBlMWxpY29zLCBhbGltZW50b3MgZSBhdXRvbW90aXZhKSwgc2VydmlcdT" \
        "AwZTdvcyBlIHR1cmlzbW8iLCAiQ0xJTUEiOiAidHJvcGljYWwiLCAiUFJJTkNJUEFJU19SSU9TIjogIkRvY2UsIEdyYW5kZSwgU" \
        "GFyYW5hXHUwMGVkYmEsIEplcXVpdGluaG9uaGEgZSBTXHUwMGUzbyBGcmFuY2lzY28ifSwgeyJFU1RBRE8iOiAiRXNwXHUwMGVk" \
        "cml0byBTYW50byIsICJTSUdMQSI6ICJFUyIsICJDQVBJVEFMIjogIlZpdFx1MDBmM3JpYSIsICJHRU5USUxJQ08iOiAicXVlbSB" \
        "uYXNjZSBubyBFc3RhZG8gZG8gRXNwXHUwMGVkcml0byBTYW50byBcdTAwZTkgY2FwaXhhYmEgb3UgZXNwXHUwMGVkcml0by1zYW" \
        "50ZW5zZSIsICJQT1BVTEFDQU8iOiAiNC4wMTYuMzU2IGhhYml0YW50ZXMgKGVzdGltYXRpdmEgSUJHRSwgMjAxNykiLCAiTlVNR" \
        "VJPX0RFX01VTklDSVBJT1MiOiAiNzgiLCAiRUNPTk9NSUEiOiAiYWdyaWN1bHR1cmEsIHBlY3VcdTAwZTFyaWEsIG1pbmVyYVx1" \
        "MDBlN1x1MDBlM28sIGluZFx1MDBmYXN0cmlhIChzaWRlcnVyZ2lhLCB0XHUwMGVheHRpbCwgbWFkZWlyYSwgY2VsdWxvc2UsIGF" \
        "saW1lbnRvcykgZSB0dXJpc21vIiwgIkNMSU1BIjogInRyb3BpY2FsIiwgIlBSSU5DSVBBSVNfUklPUyI6ICJEb2NlLCBJdGFcdT" \
        "AwZmFuYXMsIEl0YXBlbWlyaW0sIFNcdTAwZTNvIE1hdGhldXMifSwgeyJFU1RBRE8iOiAiUGFyYW5cdTAwZTEiLCAiU0lHTEEiO" \
        "iAiUFIiLCAiQ0FQSVRBTCI6ICJDdXJpdGliYSIsICJHRU5USUxJQ08iOiAicXVlbSBuYXNjZSBubyBFc3RhZG8gZG8gUGFyYW5c" \
        "dTAwZTEgXHUwMGU5IHBhcmFuYWVuc2UiLCAiUE9QVUxBQ0FPIjogIjExLjMyMC44OTIgaGFiaXRhbnRlcyAoZXN0aW1hdGl2YSB" \
        "JQkdFLCAyMDE3KSIsICJOVU1FUk9fREVfTVVOSUNJUElPUyI6ICIzOTkiLCAiRUNPTk9NSUEiOiAiYWdyaWN1bHR1cmEsIHBlY3" \
        "VcdTAwZTFyaWEsIGV4dHJhdGl2aXNtbyB2ZWdldGFsLCBpbmRcdTAwZmFzdHJpYSAoYWdyb2luZFx1MDBmYXN0cmlhLCBhdXRvb" \
        "Vx1MDBmM3ZlaXMsIGFsaW1lbnRvcywgYmViaWRhcywgY2VsdWxvc2UpLCBzZXJ2aVx1MDBlN29zIGUgdHVyaXNtbyIsICJDTElN" \
        "QSI6ICJTdWJ0cm9waWNhbCIsICJQUklOQ0lQQUlTX1JJT1MiOiAiUGFyYW5cdTAwZTEsIEl2YVx1MDBlZCwgSXRhcmFyXHUwMGU" \
        "5LCBQYXJhbmFwYW5lbWEsIFRpYmFnaSBlIElndWFcdTAwZTd1In0sIHsiRVNUQURPIjogIlNhbnRhIENhdGFyaW5hIiwgIlNJR0" \
        "xBIjogIlNDIiwgIkNBUElUQUwiOiAiRmxvcmlhblx1MDBmM3BvbGlzIiwgIkdFTlRJTElDTyI6ICJxdWVtIG5hc2NlIG5vIEVzd" \
        "GFkbyBkZSBTYW50YSBDYXRhcmluYSBcdTAwZTkgY2F0YXJpbmVuc2Ugb3UgYmFycmlnYS12ZXJkZSIsICJQT1BVTEFDQU8iOiAi" \
        "Ny4wMDEuMTYxIGhhYml0YW50ZXMgKGVzdGltYXRpdmEgSUJHRSwgMjAxNykiLCAiTlVNRVJPX0RFX01VTklDSVBJT1MiOiAiMjk" \
        "1IiwgIkVDT05PTUlBIjogImFncmljdWx0dXJhLCBwZWN1XHUwMGUxcmlhLCBwZXNjYSwgZXh0cmF0aXZpc21vIG1pbmVyYWwsIG" \
        "luZFx1MDBmYXN0cmlhIChhZ3JvaW5kXHUwMGZhc3RyaWEsIHRcdTAwZWF4dGlsLCBhbGltZW50b3MsIGNlclx1MDBlMm1pY2EsI" \
        "GF1dG9tXHUwMGYzdmVpcywgZWxldHJvZG9tXHUwMGU5c3RpY29zKSBlIHR1cmlzbW8iLCAiQ0xJTUEiOiAic3VidHJvcGljYWwi" \
        "LCAiUFJJTkNJUEFJU19SSU9TIjogIkNhbm9hcywgUGVsb3RhcywgTmVncm8gZSBVcnVndWFpIn0sIHsiRVNUQURPIjogIlJpbyB" \
        "HcmFuZGUgZG8gU3VsIiwgIlNJR0xBIjogIlJTIiwgIkNBUElUQUwiOiAiUG9ydG8gQWxlZ3JlIiwgIkdFTlRJTElDTyI6ICJxdW" \
        "VtIG5hc2NlIG5vIEVzdGFkbyBkbyBSaW8gR3JhbmRlIGRvIFN1bCBcdTAwZTkgZ2FcdTAwZmFjaG8gb3Ugc3VsLXJpby1ncmFuZ" \
        "GVuc2UiLCAiUE9QVUxBQ0FPIjogIjExLjMyMi44OTUgaGFiaXRhbnRlcyAoZXN0aW1hdGl2YSBJQkdFLCAyMDE3KSIsICJOVU1F" \
        "Uk9fREVfTVVOSUNJUElPUyI6ICI0OTciLCAiRUNPTk9NSUEiOiAiYWdyaWN1bHR1cmEsIHBlY3VcdTAwZTFyaWEsIGluZFx1MDB" \
        "mYXN0cmlhIChxdVx1MDBlZG1pY2EsIG1ldGFsXHUwMGZhcmdpY2EsIGF1dG9tXHUwMGYzdmVpcywgbmF2YWwsIHRcdTAwZWF4dG" \
        "lsLCBhbGltZW50b3MsIGNvdXJvLCB0YWJhY28sIGNhbFx1MDBlN2Fkb3MsIG1hZGVpcmEpIGUgdHVyaXNtbyIsICJDTElNQSI6I" \
        "CJzdWJ0cm9waWNhbCIsICJQUklOQ0lQQUlTX1JJT1MiOiAiVGFxdWFyaSwgSWp1XHUwMGVkLCBJYmljdVx1MDBlZCwgVXJ1Z3Vh" \
        "aSwgUGVsb3RhcyBlIENhbWFxdVx1MDBlMyJ9XQ =="
    c = base64.b64decode(s.encode('ascii', 'strict')).decode('ascii')
    d = json.loads(c)

    e = json.load(file.open())
    assert d == e
