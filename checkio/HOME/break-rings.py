# -*- coding: utf-8 -*-
# Copyright 2015 IFOOTH
# Author: Joe Lei <thezero12@hotmail.com>


def break_rings(rings):
    # 转换成图
    graph = {}
    for i in rings:
        a, b = i
        if a not in graph:
            graph[a] = {b}
        else:
            graph[a].add(b)
        if b not in graph:
            graph[b] = {a}
        else:
            graph[b].add(a)

    # 找出最少编点做起点，记录，压栈
    start = min(graph, key=lambda x: len(graph[x]))
    P, Q = {}, set()
    P[start] = None
    Q.add(start)
    while Q:
        u = Q.pop()
        for v in graph[u].difference(P):
            P[v] = u
        _graph = filter(lambda x: x not in P, graph)
        if not _graph:
            break
        start = min(_graph, key=lambda x: len(graph[x].difference(P)))
        P[start] = None
        Q.add(start)
    return len(filter(lambda x: P[x] is not None, P))


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert break_rings(({1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {4, 6})) == 3, "example"
    assert break_rings(({1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4})) == 3, "All to all"
    assert break_rings(({5, 6}, {4, 5}, {3, 4}, {3, 2}, {2, 1}, {1, 6})) == 3, "Chain"
    assert break_rings(({8, 9}, {1, 9}, {1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {8, 7})) == 5, "Long chain"
