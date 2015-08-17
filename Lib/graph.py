# -*- coding: utf-8 -*-
# Copyright 2015 IFOOTH
# Author: Joe Lei <thezero12@hotmail.com>
"""图算法
图很容易使用字段+列表实现
一， 有向图
1, 'A': {}, 代表A指向集合中的值
2, 集合元素唯一
graphA = {
    'A': {'A', 'B', 'C'},
    'B': {'F', 'O', K'},
    'C': {'D'},
    'D': {'C'},
    'E': {'F'},
    'F': {'C'}
    ...
}
graphB = [(A, A), (A, B), (A, C), ...]
G = {'V': {'A', 'B', 'C'}, 'E': {('A', 'B'), ('A', 'C')}}
二， 无向图
graphA = {
    'A': {'A', 'B', 'C'},
    'B': {'F', 'O', K', 'A'},
    'C': {'D'},
    'D': {'C'},
    'E': {'F'},
    'F': {'C'}
    ...
}
graphB = [{A, A}, {A, B}, {A, C}]
G = {'V': ['A', 'B', 'C'), 'E': {'A', 'B'}}
三, 加权图
G = {'V': {'A', 'B', 'C'}, 'E': {'A', 'B'},
     'V_P': {'A': 3}, 'E_P': {'A', 'B'}: 34}
"""


def walk(network):
    # 转换成无向图
    G = {}  # noqa
    for i in network:
        a, b = i.split('-')
        if a not in G:
            G[a] = {b}
        else:
            G[a].add(b)
        if b not in G:
            G[b] = {a}
        else:
            G[b].add(a)

    P, Q = dict(), set()
    # 第一个元素入栈，记录
    start = G.iterkeys().next()
    Q.add(start)
    P[start] = None
    print G
    while Q:
        u = Q.pop()
        for v in G[u].difference(P):
            Q.add(v)
            P[u] = v
    return P


if __name__ == '__main__':
    print walk(("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
     "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"))
