#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'
import os
from time import sleep
from incolumepy.tdd.menu import entrance, header, line, itemmenu
from incolumepy.tdd.romanos import Romanos
from functools import partial


def menu(options: list):
    os.system('clear')
    functs = {i: f for i, _, f in options}
    while True:
        header('MENU PRINCIPAL')
        for i, msg, _ in options:
            print('{} - {}'.format(i, msg))
        op = entrance('Escolha sua opção: ')
        functs.get(
            op,
            lambda: print(
                '\nOpção inválida!\nEscolha apenas as presentadas no Menu.\n\n'
            ),
        )()
        sleep(1)
    print(line(), '\n')


def to_roman():
    print(Romanos().calc_roman(int(input('Informe o número arabico: '))))


def to_arabic():
    print(Romanos().calc_arabic(input('Informe o número romano: ')))


def run():
    options = [
        itemmenu(0, 'Sair', exit),
        itemmenu(1, 'Arabicos > Romanos', to_roman),
        itemmenu(2, 'Romanos > Arabicos', to_arabic),
    ]
    menu(options)


if __name__ == '__main__':
    run()
