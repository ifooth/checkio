# -*- coding: utf-8 -*-
# Copyright 2015 IFOOTH
# Author: Joe Lei <thezero12@hotmail.com>


def safe_pawns(pawns):
    _sum = 0
    for i in pawns:
        if '%s%s' % (chr(ord(i[0]) - 1), int(i[1]) - 1) in pawns:
            _sum += 1
        elif '%s%s' % (chr(ord(i[0]) + 1), int(i[1]) - 1) in pawns:
            _sum += 1
    return _sum


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
