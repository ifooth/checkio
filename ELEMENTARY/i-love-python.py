# -*- coding: utf-8 -*-
# Copyright 2015 IFOOTH
# Author: Joe Lei <thezero12@hotmail.com>


def i_love_python():
    """
        Let's explain why do we love Python.
    """
    return "I love Python!"


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert i_love_python() == "I love Python!"
