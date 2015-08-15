# -*- coding: utf-8 -*-
# Copyright 2015 IFOOTH
# Author: Joe Lei <thezero12@hotmail.com>
import copy


def break_rings(rings):
    vertex = {}
    rings = list(rings)
    for i in rings:
        for j in i:
            vertex[j] = vertex.get(j, 0) + 1
    _break = 0
    while True:
        if sum(vertex.values()) == 0:
            break
        _min = min(filter(lambda x: vertex[x] >= 1, vertex), key=lambda x: vertex[x])
        _need_delete = set()
        for i in rings:
            if _min in i:
                _need_delete |= i
        _need_delete -= {_min}
        for other in _need_delete:
            for j in copy.deepcopy(rings):
                if _min not in j and other in j:
                    o = j - {other}
                    o = o.pop()
                    vertex[o] -= 1
                    rings.remove(j)
            vertex[_min] -= 1
            vertex.pop(other)
            _break += 1
    return _break


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert break_rings(({1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {4, 6})) == 3, "example"
    assert break_rings(({1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4})) == 3, "All to all"
    assert break_rings(({5, 6}, {4, 5}, {3, 4}, {3, 2}, {2, 1}, {1, 6})) == 3, "Chain"
    assert break_rings(({8, 9}, {1, 9}, {1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {8, 7})) == 5, "Long chain"
