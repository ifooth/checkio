# -*- coding: utf-8 -*-
# Copyright 2015 IFOOTH
# Author: Joe Lei <thezero12@hotmail.com>
from copy import deepcopy
from itertools import combinations


def check_connection(network, first, second):
    _cache = []
    network = dict(enumerate([set(i.split('-')) for i in network]))
    finish = False
    while not finish:
        finish = True
        _cache = deepcopy(network)
        for _a, _b in combinations(network.items(), 2):
            if _a[1] & _b[1]:
                _cache['union'] = _a[1] | _b[1]
                _cache.pop(_a[0])
                _cache.pop(_b[0])
                network = dict(enumerate(_cache.values()))
                finish = False
                break
        if finish:
            break

    for j in _cache.values():
        if first in j:
            return second in j
        if second in j:
            return first in j


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    # assert check_connection(
    #     ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
    #      "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
    #     "super", "scout2") == True, "Super Scout"
    # assert check_connection(
    #     ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
    #      "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
    #     "dr101", "sscout") == False, "I don't know any scouts."
    # assert check_connection(("nikola-robin","batman-nwing","mr99-batman","mr99-robin","dr101-out00","out00-nwing",),"dr101","mr99") == True
