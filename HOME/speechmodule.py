# -*- coding: utf-8 -*-
# Copyright 2015 IFOOTH
# Author: Joe Lei <thezero12@hotmail.com>

FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    letters = ''
    h = number // 100
    if h > 0:
        letters += FIRST_TEN[h - 1] + ' hundred'
    number %= 100
    if number < 1:
        return letters
    if h > 0:
        letters += ' '
    if number < 10:
        letters += FIRST_TEN[number - 1]
    elif number < 20:
        letters += SECOND_TEN[number - 10]
    elif number % 10 == 0:
        letters += OTHER_TENS[number // 10 - 2]
    else:
        letters += OTHER_TENS[number // 10 - 2]
        letters += ' ' + FIRST_TEN[number % 10 - 1]
    return letters


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
