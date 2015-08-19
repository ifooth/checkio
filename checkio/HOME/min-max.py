# -*- coding: utf-8 -*-
# Copyright 2015 IFOOTH
# Author: Joe Lei <thezero12@hotmail.com>


def min(*args, **kwargs):
    key = kwargs.get("key", None)
    if len(args) == 1:
        args = args[0]
    _min = None
    if key:
        for i in args:
            if _min is None:
                _min = i
            elif key(i) < key(_min):
                _min = i
    else:
        for i in args:
            if _min is None:
                _min = i
            if i < _min:
                _min = i
    return _min


def max(*args, **kwargs):
    key = kwargs.get("key", None)
    if len(args) == 1:
        args = args[0]
    _min = None
    if key:
        for i in args:
            if _min is None:
                _min = i
            elif key(i) > key(_min):
                _min = i
    else:
        for i in args:
            if _min is None:
                _min = i
            if i > _min:
                _min = i
    return _min


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
