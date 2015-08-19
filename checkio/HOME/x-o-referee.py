# -*- coding: utf-8 -*-
# Copyright 2015 IFOOTH
# Author: Joe Lei <thezero12@hotmail.com>


def checkio(game_result):
    _cache = {'XXX': 'X', 'OOO': 'O'}
    for k, v in _cache.iteritems():
        # 横着三排
        for i in game_result:
            if i == k:
                return v
        # 竖着三排
        for i in range(3):
            if game_result[0][i] == v and game_result[1][i] == v and game_result[2][i] == v:
                return v
        # 左边斜着
        if game_result[0][0] == v and game_result[1][1] == v and game_result[2][2] == v:
            return v
        # 右边斜着
        if game_result[0][2] == v and game_result[1][1] == v and game_result[2][0] == v:
            return v
    return 'D'


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        u"X.O",
        u"XX.",
        u"XOO"]) == "X", "Xs wins"
    assert checkio([
        u"OO.",
        u"XOX",
        u"XOX"]) == "O", "Os wins"
    assert checkio([
        u"OOX",
        u"XXO",
        u"OXX"]) == "D", "Draw"
    assert checkio([
        u"O.X",
        u"XX.",
        u"XOO"]) == "X", "Xs wins again"
