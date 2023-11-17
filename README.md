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
$ nosetests
...........................................................
----------------------------------------------------------------------
Ran 59 tests in 8.072s

OK
```
Se o resultado for similar ao apresentado, Meus parabéns!! Você concluiu o curso com sucesso!!

## Ambiente necessário
* python 3.7 (>= 3.6)
* virtualenv
* pipenv

```bash
pipenv install -d
```

Para melhor aproveitamento do ambiente de desenvolvimento
sugiro a utilização do Pyenv e Pipenv. Detalhes em
http://brito.blog.incolume.com.br/2019/11/python-ambientes-virtuais-com-pyenv.html

Outra ferramenta útil será o git, detalhes em
http://brito.blog.incolume.com.br/2013/03/guia-rapido-de-comandos-git-lado-usuario.html
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
### Testes modulares
Para testar cada etapa individualmente utilize o comando abaixo:
```bash
nosetests tests/3_employers_tests.py
...........
----------------------------------------------------------------------
Ran 11 tests in 0.006s

OK

```
