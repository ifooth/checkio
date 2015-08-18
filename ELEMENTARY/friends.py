# -*- coding: utf-8 -*-
# Copyright 2015 IFOOTH
# Author: Joe Lei <thezero12@hotmail.com>


class Friends:
    def __init__(self, connections):
        self.graph = {}
        for i in connections:
            a, b = i
            if a in self.graph:
                self.graph[a].add(b)
            else:
                self.graph[a] = {b}
            if b in self.graph:
                self.graph[b].add(a)
            else:
                self.graph[b] = {a}

    def add(self, connection):
        a, b = connection
        if (a in self.graph and b in self.graph[a]) and \
           (b in self.graph and a in self.graph[b]):
            return False

        if a in self.graph:
            self.graph[a].add(b)
        else:
            self.graph[a] = {b}
        if b in self.graph:
            self.graph[b].add(a)
        else:
            self.graph[b] = {a}
        return True

    def remove(self, connection):
        a, b = connection
        if (a not in self.graph or b not in self.graph[a]) or \
           (b not in self.graph and a not in self.graph[b]):
            return False
        self.graph[a].remove(b)
        if not self.graph[a]:
            self.graph.pop(a)
        self.graph[b].remove(a)
        if not self.graph[b]:
            self.graph.pop(b)
        return True

    def names(self):
        return set(self.graph.keys())

    def connected(self, name):
        return self.graph.get(name, set())


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"
