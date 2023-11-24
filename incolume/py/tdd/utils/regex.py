# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@britodfbr'

import re
import datetime as dt


def is_ccredito_amex(data: str):
    if not isinstance(data, str):
        raise TypeError('required string')
    bandeira, cliente, num, cvv = data.strip('\n').splitlines()
    pattern = r'.*(3[47]\d{13}) (\d{1,2})/(\d{2,4})'
    regex = re.compile(pattern)
    result = re.match(regex, num)
    return bool(result)


def is_ccredito_diners(data: str):
    if not isinstance(data, str):
        raise TypeError('required string')
    bandeira, cliente, num, cvv = data.strip('\n').splitlines()
    pattern = r'(30[013-5]\d{11,13}|3[68]\d{12,17}) \d{1,2}/\d{2,4}'
    regex = re.compile(pattern)
    result = re.match(regex, num)
    return bool(result)


def is_ccredito_master(data: str):
    if not isinstance(data, str):
        raise TypeError('required string')
    bandeira, cliente, num, cvv = data.strip('\n').splitlines()
    # pattern = r"(5[1-5]\d{14}|(222[1-9]|2720)\d{12}) \d{1,2}/\d{2,4}"
    pattern = (r'(5[1-5]\d{14}|(222[1-9]|22[3-9][0-9]|2[3-6][0-9][0-9]|'
               r'27[0-1][0-9]|2720)\d{12}) \d{1,2}/\d{2,4}')
    regex = re.compile(pattern)
    result = re.match(regex, num)
    return bool(result)


def is_ccredito_visa(data: str):
    if not isinstance(data, str):
        raise TypeError('required string')
    bandeira, cliente, num, cvv = data.strip('\n').splitlines()
    pattern = r'4\d{15} \d{1,2}/\d{2,4}'
    regex = re.compile(pattern)
    result = re.match(regex, num)
    return bool(result)


def is_date(date: str):
    # print(date)
    d = None
    try:
        if bool(re.match(r'\d{1,2}/\d{1,2}/\d{4}', date)):
            d = dt.datetime.strptime(date, '%d/%m/%Y')
        elif bool(re.match(r'\d{1,2}\.\d{1,2}\.\d{4}', date)):
            d = dt.datetime.strptime(date, '%d.%m.%Y')
        elif bool(re.match(r'\d{1,2}-\d{1,2}-\d{4}', date)):
            d = dt.datetime.strptime(date, '%d-%m-%Y')
        elif bool(re.match(r'\d{4}-\d{1,2}-\d{1,2}', date)):
            d = dt.datetime.strptime(date, '%Y-%m-%d')
        elif bool(re.match(r'\d{4}\.\d{1,2}\.\d{1,2}', date)):
            d = dt.datetime.strptime(date, '%Y.%m.%d')
        elif bool(re.match(r'\d{1,2} de \w{4,9} de \d{4}', date)):
            d = dt.datetime.strptime(date, '%d de %B de %Y')
        elif bool(re.match(r'\w{4,9} \d{1,2}, \d{4}', date)):
            d = dt.datetime.strptime(date, '%B %d, %Y')
        elif bool(re.match(r'\w+, \d{1,2} de \w{4,9} de \d{4}.', date)):
            d = dt.datetime.strptime(date, '%A, %d de %B de %Y.')
        return bool(d) or False
    except ValueError:
        return False


def isemail(email: str):
    pattern = r'[-\w]+@\w+(\.\w{2,})+'
    result = re.match(pattern, email)
    return bool(result)


def isfone(num: str):
    pattern = (
        r'(?:\+\d{2} )?\(?([14689][1-9]|2[12478]|3[1234578]|'
        r'5[1345]|7[134579])\)? \d?\d{4}[ -]?\d{4}'
    )
    result = re.match(pattern, num)
    return bool(result)


def is_ipv4(num: str):
    pattern = r'\b((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.|$)){4}\b'
    result = re.match(pattern, num)
    return bool(result)


def is_ipv6(num: str):
    pattern = r''
    result = re.match(pattern, num)
    return bool(result)


def is_url(url: str):
    print(url)
    # p1 = r'(ht|f)tps?://(localhost|\w+[\.\w+]+(\.\w{2,3}){1,2})(:\d{2,})?'
    # # p2 = r'(ht|f)tps?://(\d{1,3}(\.|$)){3}\d{1,3}(:\d{2,})'                 # OK parcial
    # # p2 = r'(ht|f)tps?://((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.|$)){4}'    # Fail
    # p2 = r'(ht|f)tps?://((25[0-5]|2[0-4][0-9]|1?[0-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1?[0-9]?[0-9])(:\d{2,})?'
    # result = None
    # if bool(re.match(p2, url)):
    #     result = re.match(p2, url)
    # elif bool(re.match(p1, url)):
    #     result = re.match(p1, url)
    # return bool(result)

    regex = re.compile(
        r'^(?:ht|f)tps?://'  # ftp or ftps or http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d{2,})?'  # optional port
        r'(?:/?|[/?]\S+)$',
        re.IGNORECASE,
    )
    result = re.match(regex, url)
    return bool(result)
