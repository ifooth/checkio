# -*- coding: utf-8 -*-
# Copyright 2015 IFOOTH
# Author: Joe Lei <thezero12@hotmail.com>
import string


def checkio(data):
    is_lower, is_upper, is_digit = False, False, False
    if len(data) < 10:
        return False
    for i in data:
        if not is_lower and i in string.ascii_lowercase:
            is_lower = True
        if not is_upper and i in string.ascii_uppercase:
            is_upper = True
        if not is_digit and i in string.digits:
            is_digit = True
    return all((is_lower, is_upper, is_digit))


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(u'A1213pokl') == False, "1st example"
    assert checkio(u'bAse730onE4') == True, "2nd example"
    assert checkio(u'asasasasasasasaas') == False, "3rd example"
    assert checkio(u'QWERTYqwerty') == False, "4th example"
    assert checkio(u'123456123456') == False, "5th example"
    assert checkio(u'QwErTy911poqqqq') == True, "6th example"
