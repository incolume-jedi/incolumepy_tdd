#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'
from collections import namedtuple

itemmenu = namedtuple('ItemMenu', 'id msg func')


def entrance(msg: str):
    while True:
        try:
            value = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mDigite uma opção válida.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mOpção não informada. Execução cancelada.\033[m')
            return 1
        else:
            return value


def line(char: str = '-', tamanho: int = 50):
    return char * tamanho


def header(txt: str, tamanho: int = 50):
    print()
    print(line('='))
    print(txt.center(tamanho))
    print(line())


if __name__ == '__main__':
    header('MENU')
    # entrance('opções: ')
