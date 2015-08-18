# -*- coding: utf-8 -*-
# Copyright 2015 IFOOTH
# Author: Joe Lei <thezero12@hotmail.com>
import string

def checkio(text):

    #replace this for solution
    text = text.lower()
    _cache = {}
    _max = 0
    for i in text:
        if i in string.ascii_lowercase:
            _length = _cache.get(i, 0) + 1
            if _length > _max:
                _max = _length
            _cache[i] = _length
    _cache = filter(lambda x: x[1] == _max, _cache.items())
    _cache = sorted(_cache, key=lambda x: x[0])
    result = _cache[0][0]
    return result


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(u"Hello World!") == "l", "Hello test"
    assert checkio(u"How do you do?") == "o", "O is most wanted"
    assert checkio(u"One") == "e", "All letter only once."
    assert checkio(u"Oops!") == "o", "Don't forget about lower case."
    assert checkio(u"AAaooo!!!!") == "a", "Only letters."
    assert checkio(u"abe") == "a", "The First."
    print("Start the long test")
    assert checkio(u"a" * 9000 + u"b" * 1000) == "a", "Long."
    print("The local tests are done.")
