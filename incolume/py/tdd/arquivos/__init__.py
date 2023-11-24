# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@britodfbr'
import pathlib
import pandas as pd


def txt_create(a):
    f = pathlib.Path(a)
    c = [f'azul escuro, verde claro\n' for x in range(100)]
    with open(f, 'w') as fp:
        fp.writelines(c)
    return f.exists()


def __csv_create_pandas(fout):
    f = pathlib.Path(fout)
    count = 1501
    df = pd.DataFrame(
        {
            0: ('azul escuro' for x in range(count)),
            1: ('verde claro' for x in range(count)),
        }
    )
    df.to_csv(f)
    return f.exists()


def csv_create(fout):
    return __csv_create_pandas(fout)


def __json_create_pandas(fout):
    f = pathlib.Path(fout)
    df = pd.DataFrame((('azul escuro', 'verde claro') for x in range(1501)))
    df.to_json(f, force_ascii=False)
    return f.exists()


def json_create(fout):
    return __json_create_pandas(fout)


def __xlsx_create_pandas(fout):
    f = pathlib.Path(fout)
    df = pd.DataFrame((('azul escuro', 'verde claro') for x in range(1501)))
    df.to_excel(f)
    return f.exists()


def xlsx_create(fout):
    return __xlsx_create_pandas(fout)


if __name__ == '__main__':
    txt_create('/tmp/a.txt')
    csv_create('/tmp/a.csv')
