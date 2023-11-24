import requests
import os
from functools import partial
from bs4 import BeautifulSoup, Comment, Doctype
import re
import pathlib

outputdir = pathlib.Path(__file__).parents[0].joinpath('artefacts', 'atos')
outputdir.mkdir(exist_ok=True, parents=True)
output = outputdir / 'L8666.html'


def gravar(code: (str, bytes), filename: str, mode: str = 'wb') -> bool:
    if isinstance(code, str):
        mode = 'w'
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, mode) as f:
        f.write(code)
    return True


def req_lei8666(url: str) -> True:
    return requests.get(url)


def get_content(url: str):
    return requests.get(url).content


save_content = partial(gravar, filename=outputdir / 'l8666-txtSF.html')


def identify_recover(pathfile: str) -> str:
    with open(pathfile) as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    principal = soup.html.html
    principal.attrs = {}
    [x.unwrap() for x in principal.find_all(re.compile(r'span|div'))]
    [tag.decompose() for tag in principal.find_all(re.compile(r'meta|style'))]
    [
        tag.decompose()
        for tag in principal()
        if tag(text=lambda it: isinstance(it, Comment))
    ]
    for tag in principal():
        for attribute in [
            'class',
            'style',
        ]:  # You can also add id,style,etc in the list
            del tag[attribute]
    result = principal.prettify(formatter='html', encoding='iso8859-1')
    gravar(result, output)
    return result


def formating(pathfile: str) -> str:
    pathfile = pathlib.Path(pathfile)
    soup = BeautifulSoup(pathfile.read_bytes(), 'html.parser')
    soup.insert(0, Doctype('html'))
    soup.html['lang'] = 'pt-br'
    soup.html.insert(0, soup.new_tag('head'))
    soup.head.append(soup.new_tag('meta', **{'charset': 'UTF-8'}))
    soup.head.append(
        soup.new_tag(
            'link',
            **{
                'rel': 'stylesheet',
                'type': 'text/css',
                'href': '../css/legis_3.css',
            }
        )
    )
    soup.body.insert(0, soup.new_tag('header'))
    soup.body.header.append(soup.new_tag('h1'))
    soup.body.header.append(soup.new_tag('h2'))
    soup.body.header.append(soup.new_tag('h3'))
    soup.body.header.h1.append('Presidência da Republica')
    soup.body.header.h2.append('Secretaria Geral')
    soup.body.header.h3.append('Subchefia para Assuntos Jurídicos')
    soup.select('p:nth-of-type(1)')[0]['class'] = 'epigrafe'
    soup.select('p:nth-of-type(2)')[0]['class'] = 'ementa'
    soup.find(string=re.compile('ITAMAR FRANCO', re.I)).parent[
        'class'
    ] = 'presidente'
    soup.find(string=re.compile('Fernando Henrique Cardoso', re.I)).parent[
        'class'
    ] = 'ministro'
    soup.find(string=re.compile('Romildo Canhim', re.I)).parent[
        'class'
    ] = 'ministro'
    soup.find(
        string=re.compile(
            'Brasília, 21 de junho de 1993, 172º da Independência e 105º da República.'
        )
    ).parent['class'] = 'dou'
    print()
    result = soup.prettify(formatter='html', encoding='iso8859-1')
    gravar(result, output)
    return result
