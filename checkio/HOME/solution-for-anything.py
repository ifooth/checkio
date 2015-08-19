# -*- coding: utf-8 -*-
# Copyright 2015 IFOOTH
# Author: Joe Lei <thezero12@hotmail.com>


class Compare(object):
    def __lt__(self, item):
        return True

    def __le__(self, item):
        return True

    def __eq__(self, item):
        return True

    def __ne__(self, item):
        return True

    def __ge__(self, item):
        return True

    def __gt__(self, item):
        return True


def checkio(anything):
    """
        try to return anything else :)
    """
    return Compare()


if __name__ == '__main__':
    import re, math

    assert checkio({}) != [],         'You'
    assert checkio('Hello') < 'World', 'will'
    assert checkio(80) > 81,           'never'
    assert checkio(re) >= re,          'make'
    assert checkio(re) <= math,        'this'
    assert checkio(5) == ord,          ':)'

    print('NO WAY :(')
