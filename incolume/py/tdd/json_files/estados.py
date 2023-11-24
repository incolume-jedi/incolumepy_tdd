#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pprint import pprint
from inspect import stack
from pathlib import Path
from incolumepy.tdd import __root__
from bs4 import BeautifulSoup
from unidecode import unidecode
import json
import pandas as pd
import requests
import base64


__author__ = '@britodfbr'
path = Path(__root__) / 'src' / 'incolumepy' / 'tdd' / 'json_files'
url = 'https://www.todamateria.com.br/estados-do-brasil/'


def truncus1():
    df = pd.read_html(url)[0]
    df.columns = df.columns.str.casefold()
    df.to_json(
        path.joinpath(f'{stack()[0][3]}.json'), orient='records', indent=4
    )
    df.to_json(path.joinpath('estados.json'), orient='records', indent=4)


def truncus12():
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html5lib')
    # print(soup)
    # estados = [x.text for x in soup.find_all('h3')]
    # print(estados)
    # ibge = [x.find_next_sibling('p') for x in soup.find_all('h3')]
    # print(ibge)
    estados = zip(
        [x.text for x in soup.find_all('h3')],
        [x.find_next_sibling('p') for x in soup.find_all('h3')],
    )
    # print(list(estados))
    result = []
    for estado, info in estados:
        print(estado, info)
        [x.decompose() for x in info.find_all('br')]
        key = ['estado']
        value = [estado]
        for i, inf in enumerate(info):
            # print(i, inf)
            if i % 2 == 0:
                key.append(inf.text)
            else:
                value.append(inf.replace(': ', ''))

        result.append(dict(zip(key, value)))
    pprint(result)


def truncus13():
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html5lib')
    estados = zip(
        [x.text for x in soup.find_all('h3')],
        [x.find_next_sibling('p') for x in soup.find_all('h3')],
    )
    result = []
    for estado, info in estados:
        print(estado, info)
        [x.decompose() for x in info.find_all('br')]
        key = ['estado']
        value = [estado]
        for i, inf in enumerate(info):
            if i % 2 == 0:
                key.append(inf.text)
            else:
                value.append(inf.replace(': ', ''))

        result.append(dict(zip(key, value)))
    pprint(result)
    df = pd.DataFrame(result)
    df.columns = (
        df.columns.str.strip().str.replace(' ', '_').str.upper().map(unidecode)
    )
    df.drop('2', axis=1, inplace=True)
    # print(df.columns)
    # print(df)

    df.to_json(
        path.joinpath(f'{stack()[0][3]}.json'), orient='records', indent=4
    )


def truncus14():
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html5lib')
    estados = zip(
        [x.text for x in soup.find_all('h3')],
        [x.find_next_sibling('p') for x in soup.find_all('h3')],
    )
    result = []
    for estado, info in estados:
        print(estado, info)
        [x.decompose() for x in info.find_all('br')]
        key = ['estado']
        value = [estado]
        for i, inf in enumerate(info):
            if i % 2 == 0:
                key.append(inf.text)
            else:
                value.append(inf.replace(': ', ''))

        result.append(dict(zip(key, value)))
    pprint(result)
    df = pd.DataFrame(result)
    df.columns = (
        df.columns.str.strip().str.replace(' ', '_').str.upper().map(unidecode)
    )
    df.drop('2', axis=1, inplace=True)
    # print(df.columns)
    # print(df)
    df.dropna(axis=1, inplace=True)
    df.to_json(
        path.joinpath(f'{stack()[0][3]}.json'), orient='records', indent=4
    )


def truncus15():
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html5lib')
    estados = zip(
        [x.text for x in soup.find_all('h3')],
        [x.find_next_sibling('p') for x in soup.find_all('h3')],
    )
    result = []
    for estado, info in estados:
        print(estado, info)
        [x.decompose() for x in info.find_all('br')]
        key = ['estado']
        value = [estado]
        for i, inf in enumerate(info):
            if i % 2 == 0:
                key.append(inf.text)
            else:
                value.append(inf.replace(': ', ''))

        result.append(dict(zip(key, value)))
    pprint(result)
    df = pd.DataFrame(result)
    df.columns = (
        df.columns.str.strip().str.replace(' ', '_').str.upper().map(unidecode)
    )
    df.drop('2', axis=1, inplace=True)
    # print(df.columns)
    # print(df)
    # df.dropna(axis=1, inplace=True)
    # print(df.columns.str.contains('DATA'))
    print(df[[x for x in df.columns if x.startswith('DATA')]])
    df.to_json(
        path.joinpath(f'{stack()[0][3]}.json'), orient='records', indent=4
    )
    df.to_json(path.joinpath('estados.json'), orient='records', indent=4)


def truncus16():
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html5lib')
    estados = zip(
        [x.text for x in soup.find_all('h3')],
        [x.find_next_sibling('p') for x in soup.find_all('h3')],
    )
    result = []
    for estado, info in estados:
        # print(estado, info)
        [x.decompose() for x in info.find_all('br')]
        key = ['estado']
        value = [estado]
        for i, inf in enumerate(info):
            if i % 2 == 0:
                key.append(inf.text)
            else:
                value.append(inf.replace(': ', ''))

        result.append(dict(zip(key, value)))
    # pprint(result)
    df = pd.DataFrame(result)
    df.columns = (
        df.columns.str.strip().str.replace(' ', '_').str.upper().map(unidecode)
    )
    df.drop('2', axis=1, inplace=True)
    # print(df.columns)
    # print(df)
    df.dropna(axis=1, inplace=True)
    d = json.dumps(df.to_dict(orient='records'))
    print(d)
    b = base64.b64encode(d.encode('ascii')).decode('ascii')
    print(b)
    # with open('x.json', 'w') as f:
    #     f.write(b)
    df.to_json(
        path.joinpath(f'{stack()[0][3]}.json'), orient='records', indent=4
    )


if __name__ == '__main__':
    truncus1()
    truncus16()
