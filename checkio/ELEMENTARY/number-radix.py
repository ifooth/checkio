# -*- coding: utf-8 -*-
# Copyright 2015 IFOOTH
# Author: Joe Lei <thezero12@hotmail.com>
import string


def checkio(str_number, radix):
    n = string.digits + string.ascii_uppercase
    n = dict((i, idx) for idx, i in enumerate(n))
    if n[sorted(str_number)[-1]] >= radix + 1:
        return -1
    return sum(radix ** idx * n[i] for idx, i in enumerate(
        reversed(str_number)))


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"AF", 16) == 175, "Hex"
    assert checkio(u"101", 2) == 5, "Bin"
    assert checkio(u"101", 5) == 26, "5 base"
    assert checkio(u"Z", 36) == 35, "Z base"
    assert checkio(u"AB", 10) == -1, "B > A > 10"
