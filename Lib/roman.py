# -*- coding: utf-8 -*-
# Copyright 2015 IFOOTH
# Author: Joe Lei <thezero12@hotmail.com>
"""罗马数字转换"""
_ROMAN = (
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


def int2roman(num):
    # todo 类型，边界检查
    result = ''
    for n, i in _ROMAN:
        while num >= i:
            result += n
            num -= i
    return result


def roman2int(roman):
    result = 0
    index = 0
    for n, i in _ROMAN:
        while roman[index: index + len(n)] == n:
            result += i
            index += len(n)
    return result
