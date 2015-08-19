# -*- coding: utf-8 -*-
# Copyright 2015 IFOOTH
# Author: Joe Lei <thezero12@hotmail.com>


def check_connection(network, first, second):
    # 转换成图
    graph = {}
    for i in network:
        a, b = i.split('-')
        if a in graph:
            graph[a].add(b)
        else:
            graph[a] = {b}
        if b in graph:
            graph[b].add(a)
        else:
            graph[b] = {a}
    # 第一个元素压栈，记录前驱
    P, Q = dict(), set() # noqa
    P[first] = None
    Q.add(first)
    while Q:
        u = Q.pop()
        if u == second:
            return True
        for i in graph[u].difference(P):
            Q.add(i)
            P[i] = u
    return False


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."
