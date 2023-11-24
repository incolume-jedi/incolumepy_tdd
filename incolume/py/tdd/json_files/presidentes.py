#!/usr/bin/env python
# -*- coding: utf-8 -*-
import base64
import json

import requests
import pandas as pd
from bs4 import BeautifulSoup
from unidecode import unidecode
from pathlib import Path
from incolumepy.tdd import __root__
from fuzzywuzzy.process import extractOne, extractBests
from inspect import stack


__author__ = '@britodfbr'
path = Path(__root__) / 'src' / 'incolumepy' / 'tdd' / 'json_files'
url = 'https://pt.m.wikipedia.org/wiki/Lista_de_presidentes_do_Brasil'
req = requests.get(url)


def truncus0():
    print(req.content)


def truncus1():
    df = pd.read_html(req.content)[0]
    df.columns = [x[0] for x in df.columns]
    df.columns = df.columns.map(unidecode).str.upper().str.replace(' ', '_')
    df[['INICIO_MANDATO', 'FIM_MANDATO']] = (
        df['PERIODO_DO_MANDATO(DURACAO_DO_MANDATO)']
        .str.replace('°|º', '', regex=True)
        .apply(
            lambda x: x.replace(x[x.find('(') : x.find(')') + 1], '').strip()
        )
        .str.split('até', expand=True)
    )
    df['VICE-PRESIDENTE'] = df['VICE-PRESIDENTE(S)'].apply(
        lambda x: x.replace(x[x.find('[') : x.find(']') + 1], '').strip()
    )
    df['PARTIDO'] = df.PARTIDO.astype(str).apply(
        lambda x: x.replace(x[x.find('[') : x.find(']') + 1], '').strip()
    )
    df.loc[df['PARTIDO'] == 'nenhum', 'PARTIDO'] = float('nan')
    df.loc[df['VICE-PRESIDENTE'] == 'nenhum', 'VICE-PRESIDENTE'] = float('nan')
    df.loc[df['FIM_MANDATO'] == None, 'FIM_MANDATO'] = float('nan')
    df.drop(df.loc[df['NDEG'] == '—'].index, inplace=True)
    df.drop_duplicates(subset='PRESIDENTE', keep='last', inplace=True)
    print(df)

    result = df.loc[
        :,
        [
            'PRESIDENTE',
            'PARTIDO',
            'VICE-PRESIDENTE',
            'INICIO_MANDATO',
            'FIM_MANDATO',
        ],
    ]
    result = result[
        ~result['PRESIDENTE'].str.contains('República')
    ].reset_index(drop=True)
    result.to_json(
        path.joinpath('presidentes.json'), indent=4, orient='records'
    )


def truncus2():
    file = path.joinpath('presidentes.json')
    df = pd.DataFrame(json.load(file.open()))
    print(df.columns)


def truncus3():
    file = path.joinpath('presidentes.json')
    df = pd.DataFrame(json.load(file.open()))
    j = json.dumps(df.to_dict(orient='records'))
    print(j)
    k = base64.b64encode(j.encode('ascii')).decode('ascii')
    print(k)
    for i, j in enumerate(k, start=1):
        if i % 80 == 0:
            print(j)
        else:
            print(j, end='')


def truncus4():
    file = path.joinpath('presidentes_com_fotos.json')
    soup = BeautifulSoup(req.content, 'html.parser')
    df = pd.read_html(req.content)[0]
    df.columns = [x[0] for x in df.columns]
    df.columns = df.columns.map(unidecode).str.upper().str.replace(' ', '_')
    df[['INICIO_MANDATO', 'FIM_MANDATO']] = (
        df['PERIODO_DO_MANDATO(DURACAO_DO_MANDATO)']
        .str.replace('°|º', '', regex=True)
        .apply(
            lambda x: x.replace(x[x.find('(') : x.find(')') + 1], '').strip()
        )
        .str.split('até', expand=True)
    )
    df['VICE-PRESIDENTE'] = df['VICE-PRESIDENTE(S)'].apply(
        lambda x: x.replace(x[x.find('[') : x.find(']') + 1], '').strip()
    )
    df['PARTIDO'] = df.PARTIDO.astype(str).apply(
        lambda x: x.replace(x[x.find('[') : x.find(']') + 1], '').strip()
    )
    df.loc[df['PARTIDO'] == 'nenhum', 'PARTIDO'] = float('nan')
    df.loc[df['VICE-PRESIDENTE'] == 'nenhum', 'VICE-PRESIDENTE'] = float('nan')
    df.loc[df['FIM_MANDATO'] == None, 'FIM_MANDATO'] = float('nan')

    fotografias = [f'http:{x.get("src")}' for x in soup.select('td img')]

    for i, presidente in df.iterrows():
        p = presidente.PRESIDENTE.casefold()
        fotos = fotografias  # [x.casefold() for x in fotografias]
        print(p)
        q = extractOne(p, fotos)
        r = extractBests(p, fotos)
        print(q)
        print(r)

    # df.to_json(file, orient='records', indent=4)


def truncus5():
    from time import sleep

    soup = BeautifulSoup(req.content, 'html.parser')
    df0 = pd.read_html(req.content)[0]

    # iter1
    df = df0.copy()
    df.columns = [x[0] for x in df.columns]
    df.columns = df.columns.map(unidecode).str.upper().str.replace(' ', '_')
    df[['INICIO_MANDATO', 'FIM_MANDATO']] = (
        df['PERIODO_DO_MANDATO(DURACAO_DO_MANDATO)']
        .str.replace('°|º', '', regex=True)
        .apply(
            lambda x: x.replace(x[x.find('(') : x.find(')') + 1], '').strip()
        )
        .str.split('até', expand=True)
    )
    df['VICE-PRESIDENTE'] = df['VICE-PRESIDENTE(S)'].apply(
        lambda x: x.replace(x[x.find('[') : x.find(']') + 1], '').strip()
    )
    df['PARTIDO'] = df.PARTIDO.astype(str).apply(
        lambda x: x.replace(x[x.find('[') : x.find(']') + 1], '').strip()
    )
    df.drop(df.loc[df['NDEG'] == '—'].index, inplace=True)

    # iter2 - seleção do dados
    result = df.loc[
        :,
        [
            'PRESIDENTE',
            'PARTIDO',
            'VICE-PRESIDENTE',
            'INICIO_MANDATO',
            'FIM_MANDATO',
        ],
    ]
    result = result[
        ~result['PRESIDENTE'].str.contains('República')
    ].reset_index(drop=True)
    result.drop_duplicates(subset='PRESIDENTE', keep='last', inplace=True)

    # iter3 - Tratamento de datas
    result1 = result.copy()

    meses = [
        'janeiro',
        'fevereiro',
        'março',
        'abril',
        'maio',
        'junho',
        'julho',
        'agosto',
        'setembro',
        'outubro',
        'novembro',
        'dezembro',
    ]

    d = {x: y for y, x in enumerate(meses, start=1)}
    d1 = result1.INICIO_MANDATO.str.split(' de ', expand=True)
    d1.loc[:, 3] = d1[1].map(lambda x: d.get(x))
    result1.INICIO_MANDATO = pd.to_datetime(
        d1[d1.columns[[2, 3, 0]]].apply(
            lambda x: '/'.join(x.astype(str)), axis=1
        )
    )

    d2 = result1.FIM_MANDATO.str.split(' de ', expand=True).dropna()
    d2.loc[:, 3] = d2[1].map(lambda x: d.get(x))
    result1.FIM_MANDATO = pd.to_datetime(
        d2[d2.columns[[2, 3, 0]]].apply(
            lambda x: '/'.join(x.astype(str)), axis=1
        )
    )

    # result1.to_json('presidentes_com_fotos.json', indent=4, orient='records')

    # iter4 - Seleção das fotos
    result2 = result1.copy()
    # soup.select('td img')
    images = [
        (x.get('alt'), f'http:{x.get("src")}') for x in soup.select('td img')
    ]

    for i, presidente in result2.iterrows():
        p = presidente.PRESIDENTE.strip()
        q = extractOne(p, [x[1] for x in images])
        print(p, q)
        # quote = quote_plus(q[0].strip())
        quote = q[0].strip().encode('ascii')
        print(quote)

        result2.loc[i, 'URL_FOTOGRAFIA'] = quote

        foto = requests.get(q[0].strip(), stream=True, allow_redirects=True)
        sleep(7)
        print(foto.status_code)
        result2.loc[i, 'FOTOGRAFIA'] = (
            foto.content if foto.status_code == 200 else None
        )

    print('repescagem..')
    nomes = ['Costa', 'Sarney', 'Lula']
    for nome in nomes:
        q = extractOne(nome, [i[1] for i in images])
        print(q)
        quote = q[0].strip().encode('ascii')
        result2.loc[
            result2.PRESIDENTE.str.contains(nome), 'URL_FOTOGRAFIA'
        ] = quote
        foto = requests.get(q[0].strip(), stream=True, allow_redirects=True)
        result2.loc[result2.PRESIDENTE.str.contains(nome), 'FOTOGRAFIA'] = (
            foto.content if foto.status_code == 200 else None
        )

    # result2.loc[:, 'URL_FOTOGRAFIA'] = result2.loc[:, 'URL_FOTOGRAFIA'].astype('str')
    result2.INICIO_MANDATO = result2.INICIO_MANDATO.astype('str')
    result2.FIM_MANDATO = result2.FIM_MANDATO.astype('str')
    result2.loc[:, 'FOTOGRAFIA'] = result2.loc[:, 'FOTOGRAFIA'].astype('str')
    # result2.to_json('presidentes_com_fotos.json', indent=4, orient='records')
    result2.to_json(path / f'{stack()[0][3]}.json', indent=4, orient='records')
    print(result2)


def truncus6():
    from time import sleep

    soup = BeautifulSoup(req.content, 'html.parser')
    df0 = pd.read_html(req.content)[0]

    # iter1
    df = df0.copy()
    df.columns = [x[0] for x in df.columns]
    df.columns = df.columns.map(unidecode).str.upper().str.replace(' ', '_')
    df[['INICIO_MANDATO', 'FIM_MANDATO']] = (
        df['PERIODO_DO_MANDATO(DURACAO_DO_MANDATO)']
        .str.replace('°|º', '', regex=True)
        .apply(
            lambda x: x.replace(x[x.find('(') : x.find(')') + 1], '').strip()
        )
        .str.split('até', expand=True)
    )
    df['VICE-PRESIDENTE'] = df['VICE-PRESIDENTE(S)'].apply(
        lambda x: x.replace(x[x.find('[') : x.find(']') + 1], '').strip()
    )
    df['PARTIDO'] = df.PARTIDO.astype(str).apply(
        lambda x: x.replace(x[x.find('[') : x.find(']') + 1], '').strip()
    )
    df.drop(df.loc[df['NDEG'] == '—'].index, inplace=True)

    # iter2 - seleção do dados
    result = df.loc[
        :,
        [
            'PRESIDENTE',
            'PARTIDO',
            'VICE-PRESIDENTE',
            'INICIO_MANDATO',
            'FIM_MANDATO',
        ],
    ]
    result = result[
        ~result['PRESIDENTE'].str.contains('República')
    ].reset_index(drop=True)
    result.drop_duplicates(subset='PRESIDENTE', keep='last', inplace=True)

    # iter3 - Tratamento de datas
    result1 = result.copy()

    meses = [
        'janeiro',
        'fevereiro',
        'março',
        'abril',
        'maio',
        'junho',
        'julho',
        'agosto',
        'setembro',
        'outubro',
        'novembro',
        'dezembro',
    ]

    d = {x: y for y, x in enumerate(meses, start=1)}
    d1 = result1.INICIO_MANDATO.str.split(' de ', expand=True)
    d1.loc[:, 3] = d1[1].map(lambda x: d.get(x))
    result1.INICIO_MANDATO = pd.to_datetime(
        d1[d1.columns[[2, 3, 0]]].apply(
            lambda x: '/'.join(x.astype(str)), axis=1
        )
    )

    d2 = result1.FIM_MANDATO.str.split(' de ', expand=True).dropna()
    d2.loc[:, 3] = d2[1].map(lambda x: d.get(x))
    result1.FIM_MANDATO = pd.to_datetime(
        d2[d2.columns[[2, 3, 0]]].apply(
            lambda x: '/'.join(x.astype(str)), axis=1
        )
    )

    # result1.to_json('presidentes_com_fotos.json', indent=4, orient='records')

    # iter4 - Seleção das fotos
    result2 = result1.copy()
    # soup.select('td img')
    images = [
        (x.get('alt'), f'http:{x.get("src")}') for x in soup.select('td img')
    ]

    for i, presidente in result2.iterrows():
        p = presidente.PRESIDENTE.strip()
        q = extractOne(p, [x[1] for x in images])
        print(p)
        # print(p, q)
        # quote = quote_plus(q[0].strip())
        quote = q[0].strip().encode('ascii')
        # print(quote)

        result2.loc[i, 'URL_FOTOGRAFIA'] = quote

        foto = requests.get(q[0].strip(), stream=True, allow_redirects=True)
        sleep(5)
        # print(foto.status_code)
        result2.loc[i, 'FOTOGRAFIA'] = (
            foto.content if foto.status_code == 200 else None
        )

    # print('repescagem..')
    nomes = ['Costa', 'Sarney', 'Lula']
    for nome in nomes:
        q = extractOne(nome, [i[1] for i in images])
        # print(q)
        quote = q[0].strip().encode('ascii')
        result2.loc[
            result2.PRESIDENTE.str.contains(nome), 'URL_FOTOGRAFIA'
        ] = quote
        foto = requests.get(q[0].strip(), stream=True, allow_redirects=True)
        result2.loc[result2.PRESIDENTE.str.contains(nome), 'FOTOGRAFIA'] = (
            foto.content if foto.status_code == 200 else None
        )

    # result2.loc[:, 'URL_FOTOGRAFIA'] = result2.loc[:, 'URL_FOTOGRAFIA'].astype('str')
    result2.INICIO_MANDATO = result2.INICIO_MANDATO.astype('str')
    result2.FIM_MANDATO = result2.FIM_MANDATO.astype('str')
    result2.loc[:, 'FOTOGRAFIA'] = result2.loc[:, 'FOTOGRAFIA'].astype('str')
    print(
        '>>>',
        result2.loc[
            result2['VICE-PRESIDENTE'].str.contains('nenhum'),
            'VICE-PRESIDENTE',
        ],
        sep='\n',
    )
    result2.loc[
        result2['VICE-PRESIDENTE'].str.contains('nenhum'), 'VICE-PRESIDENTE'
    ] = float('Nan')
    result2.to_json('presidentes_com_fotos.json', indent=4, orient='records')
    result2.to_json(path / f'{stack()[0][3]}.json', indent=4, orient='records')
    # print(result2)


def truncus7():
    df = pd.read_json(path / 'truncus6.json')
    print(df)


def truncus8():
    jsonf = path / 'presidentes_com_fotos.json'
    with jsonf.open() as f:
        content = json.load(f)
    print(len(content), type(content))
    print(content[34]['PRESIDENTE'])
    print(content[34]['VICE-PRESIDENTE'])


def truncus9():
    df = pd.read_json(path / 'presidentes_com_fotos.json')
    print(df.shape)
    d = json.dumps(df.to_dict(orient='records'))
    print(d)
    b = base64.b64encode(d.encode('ascii')).decode('ascii')
    print(b)
    path.joinpath('presidentes_com_fotos_hash.txt').write_text(b)


if __name__ == '__main__':
    truncus9()
