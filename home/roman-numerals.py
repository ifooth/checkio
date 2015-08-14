# -*- coding: utf-8 -*-
# Copyright 2015 IFOOTH
# Author: Joe Lei <thezero12@hotmail.com>


def checkio(data):
    roman = (('M', 1000),
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
             ('I', 1))
    result = ''
    for n, i in roman:
        while data >= i:
            result += n
            data -= i
    return result

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
