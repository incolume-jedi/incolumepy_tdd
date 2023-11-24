#!/usr/bin/env python
# -*- coding: utf-8 -*-
from abc import ABC, ABCMeta, abstractmethod


class Transporte(ABC):
    __metaclass__ = ABCMeta
    _tipo_transporte = ['CARGA', 'PASSAGEIRO']

    @abstractmethod
    def method(self):
        ...
