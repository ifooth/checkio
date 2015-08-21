# -*- coding: utf-8 -*-
# Copyright 2015 IFOOTH
# Author: Joe Lei <thezero12@hotmail.com>
import string


_VOWELS = "AEIOUY"
_VOWELS = set(_VOWELS)
_CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"
_CONSONANTS = set(_CONSONANTS)


def check_striped(s):
    a = set(i.upper() for i in s[::2])
    b = set(i.upper() for i in s[1::2])
    if a and b and (a.issubset(_VOWELS) and b.issubset(_CONSONANTS) or
                    a.issubset(_CONSONANTS) and b.issubset(_VOWELS)):
        return 1
    return 0


def checkio(text):
    _VOWELS = "AEIOUY"
    _VOWELS = set(_VOWELS)
    _CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"
    _CONSONANTS = set(_CONSONANTS)
    s = ''
    c = 0
    for i in text:
        if i == ' ' or i in string.punctuation:
            c += check_striped(s)
            s = ''

        else:
            s += i
    c += check_striped(s)
    return c


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"My name is ...") == 3, "All words are striped"
    assert checkio(u"Hello world") == 0, "No one"
    assert checkio(u"A quantity of striped words.") == 1, "Only of"
    assert checkio(u"Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
