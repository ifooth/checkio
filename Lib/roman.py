# -*- coding: utf-8 -*-
# Copyright 2015 IFOOTH
# Author: Joe Lei <thezero12@hotmail.com>
"""罗马数字转换"""
import re


_Roman = (
    ('M', 1000),
    ('CM', 900),
    ('D', 500),
    ('CD', 400),
    ('C', 100),
    ('XC', 90),
    ('L', 50),
    ('XL', 40),
    ('X', 10),
    ('IX', 9),
    ('V', 5),
    ('IV', 4),
    ('I', 1)
)
_RomanPattern = re.compile("""
    ^                   # beginning of string
    M{0,4}              # thousands - 0 to 4 M's
    (CM|CD|D?C{0,3})    # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 C's),
                        #            or 500-800 (D, followed by 0 to 3 C's)
    (XC|XL|L?X{0,3})    # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 X's),
                        #        or 50-80 (L, followed by 0 to 3 X's)
    (IX|IV|V?I{0,3})    # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 I's),
                        #        or 5-8 (V, followed by 0 to 3 I's)
    $                   # end of string
    """, re.VERBOSE)


def int2roman(num):
    assert 0 < num < 5000, 'num must be 1 - 4999'
    assert int(num) == num, 'num must be int'

    result = ''
    for n, i in _Roman:
        while num >= i:
            result += n
            num -= i
    return result


def roman2int(roman):
    assert roman, 'roman cannt be null'
    assert _RomanPattern.match(roman), 'invalid roman'

    result = 0
    index = 0
    for n, i in _Roman:
        while roman[index: index + len(n)] == n:
            result += i
            index += len(n)
    return result
