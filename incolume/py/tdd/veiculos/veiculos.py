#!/usr/bin/env python
# -*- coding: utf-8 -*-
import abc
from datetime import datetime


class Veiculo(abc.ABC):
    __metaclass__ = abc.ABCMeta
    modelo = ''
    fabricante = ''
    velocidade = ''
    categoria = [
        'TERRESTRE',
        'AÉREO',
        'AQUÁTICO',
        'ESPACIAL',
    ]

    def acelerar(self, valor):
        raise NotImplementedError

    def frenar(self, valor):
        raise NotImplementedError

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, valor):
        if valor.upper() in self.categoria:
            self.__tipo = valor.lower().title()
        else:
            raise AssertionError('Categoria não disponível')

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, valor: (int, str)) -> None:
        try:
            int(valor)
            if len(str(valor)) != 4:
                raise ValueError
        except ValueError:
            raise ValueError('Informe o Ano com 4 algarismos')

        self.__ano = datetime.strptime(str(valor), '%Y')

    def getAno(self):
        return self.ano.strftime('%Y')
