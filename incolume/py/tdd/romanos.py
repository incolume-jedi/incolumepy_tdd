#!/usr/bin/env python
"""Exercício com doctest
Habilidade com classes python.

dica: solução ideal 3 linhas
"""

# TODO: Atividade  13: implementar Romanos para que passe nos testes


class Romanos:
    """Class Romanos."""

    romans = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    arabics = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I',
    }

    def calc_roman(self, num: int) -> str:
        if not num:
            raise ValueError('O argumento deve ser inteiro maior que zero.')
        if not isinstance(num, type(1)):
            raise TypeError('Esperado inteiro, obtido {}'.format(type(num)))
        result = []
        for arabic, roman in self.arabics.items():
            count = num // arabic
            result.append(roman * count)
            num -= arabic * count
        return ''.join(result)

    def calc_arabic(self, num: str) -> int:
        lst = []
        for i in num.upper():
            atual = self.romans.get(i)
            if not lst or lst[-1] >= atual:
                lst.append(atual)
            else:
                lst[-1] = -lst[-1]
                lst.append(atual)
        result = sum(lst)
        return result

    def __getattr__(self, item):
        if item.upper() in self.romans:
            return self.romans.get(item.upper())
        elif isinstance(item, str) and len(item) >= 2:
            return self.calc_arabic(item)
        else:
            raise ValueError('Não pertencem aos numerais romanos')


if __name__ == '__main__':
    import doctest

    doctest.testfile('13-romanos.txt')
