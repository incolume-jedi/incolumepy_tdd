# Treinamento em Python
## Sobre o Curso
### Nome
Treinamento em Python

### Instrutor
Ricardo Brito do Nascimento (http://brito.blog.incolume.com.br)

### Objetivo
Apresentar e aprimorar as habilidades de desenvolvimento
 e técnicas da linguagem Python.

### Pré−Requisitos
Vontade de aprender, desejo de pesquisar,
noções básicas de informática e
operação do sistema operacional por linha de comando.

### Público Alvo
Desenvolvedores, administradores de sistemas, programadores e interessados em geral.

### Duração
40 horas

## Introdução
Este treinamento se divide em etapas sequênciais,
 de conhecimento cumulativo para aperfeiçoar e
 aprimorar as habilidades de desenvolvimento e
 técnicas da linguagem.


O treinamento consite na metodologia
TDD - Test Driven Development, ou em português
Desenvolvimento Orientado por Testes.

Os testes deste treinamento foram implementados em
__doctest__ e **unittest**.
E os resutados dos testes indicarão se o objetivo foi
atendido, ou não.

Ao terminar o desenvolvimento dos testes, o
resultado deverá ser similar ao apresentado abaixo:
```bash
$ nosetests tests/*
...........................................................
----------------------------------------------------------------------
Ran 59 tests in 8.072s

OK
```
Se o resultado for similar ao apresentado, Meus parabéns!! Você concluiu o curso com sucesso!!

## Ambiente necessário
* python 3.7+ (3.7, 3.8, 3.9 ou superior)
* virtualenv
* git client


Para melhor aproveitamento do ambiente de desenvolvimento
sugiro a utilização do Pyenv e Pipenv/poetry. Detalhes em:

Usuários Linux: http://brito.blog.incolume.com.br/2019/11/python-ambientes-virtuais-com-pyenv.html

Usuários Windows: https://brito.blog.incolume.com.br/2020/11/python-ambientes-virtuais-com-pyenv-win.html

Outra ferramenta útil será o git, detalhes em
http://brito.blog.incolume.com.br/2013/03/guia-rapido-de-comandos-git-lado-usuario.html

## Como começar?
### Baixe o projeto para diretório local
```bash
git clone --depth 1 https://gitlab.com/development-incolume/treinamentos/incolumepy_tdd.git -b 2.2.1; ou
git clone --depth 1 git@gitlab.com:development-incolume/treinamentos/incolumepy_tdd.git -b 2.2.1
```
Observação: em -b será a tag mais rescente ou a indicada pelo professor.
### Crie o ambiente virtual para o projeto

* pipenv
```bash
cd incolumepy_tdd
pipenv --python 3.7
pipenv install -d
```
ou
* poetry
```bash
cd incolumepy_tdd
poetry env use 3.7
poetry install
```


## Qual o conteúdo em cada etapa?
1. Criação de modulo;
Tratamento de Exceções;
Personalização de mensagem de exceções;

1. Criação de módulos em classe; classes em python;
Tratamento de Exceções;
Personalização de mensagens de exceções;

1. Classes; atributos estáticos;
manipulação de datas;
estruturas de dados (listas), slice em lista e string;
Calculos em floats; manipulação de atributos privados;
property/setter

1. Interface em python; metodos NotImplementedError;
property/setter

1. Herança
1. Herança
1. Herança
1. Herança
1. Metodos abstratos e Classe abstrata
1. Personalização de exceções por tipo
1. Clousures
1. Decoradores
1. Meta programação em Classe Python
1. Fatoração de código agregando funcionalidades
1. Fatoração de código com mudança de
código sem perder funcionalidades
1. Recursividade
1. Fatoração para recursividade
1. Properties com bloqueio de escrita; raspagem HTML com BeautifulSoup;
1. Iteração com servidor python http.server; e utilização do selenium;
1. Utilização request; tratamento de HTML via python;
1. Validação de dados com expressões regulares;
1. Fatoração Employer
1. Manibpulação com CSV e Fatoração de classe com herança;
1. Calculos de Hashes
1. Conversão de cores rgb para hexadecimal;
1. Decodificador Morse
1. Gerador de senhas
1. Manipulação de arquivos
1. Permissões no Sistemas de Arquivos Nativo (Linux, Unix, MacOS, Windows, e outros)
1. Menu em terminal

### Testes modulares
Para testar cada etapa individualmente utilize o comando abaixo, para cada arquivo de teste unitário:
```bash
nosetests tests/03_employers_tests.py
...........
----------------------------------------------------------------------
Ran 11 tests in 0.006s

OK

```
