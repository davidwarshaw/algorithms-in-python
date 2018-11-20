#!/usr/bin/env python

from Graph import Graph


class CC(object):

    def __init__(self, g):
        self.marked = [False] * g.num_vertices()
        self.id = [0] * g.num_vertices()
        self.count = 0
        for s in range(g.num_vertices()):
            if not self.marked[s]:
                self._dfs(g, s)
                self.count += 1

    def __str__(self):
        return str(self.id)

    def _print(self):
        for v in range(len(self.id)):
            print(f"{v}: {self.id[v]}")

    def _dfs(self, g, v):
        self.marked[v] = True
        self.id[v] = self.count
        for w in g.adjacent_vertices(v):
            if not self.marked[w]:
                self._dfs(g, w)

    def connected(self, v, w):
        return self.id[v] == self.id[w]

    def id(self, v):
        return self.id[v]

    def count(self):
        return self.count


if __name__ == '__main__':
    a = Graph(13)
    a.add_edge(0, 5)
    a.add_edge(4, 3)
    a.add_edge(0, 1)
    a.add_edge(9, 12)
    a.add_edge(6, 4)
    a.add_edge(5, 4)
    a.add_edge(0, 2)
    a.add_edge(11, 12)
    a.add_edge(9, 10)
    a.add_edge(0, 6)
    a.add_edge(7, 8)
    a.add_edge(9, 11)
    a.add_edge(5, 3)
    a._print()

    cc = CC(a)
    cc._print()
    b = cc.connected(0, 4)
    print(f"cc.connected(0, 4): {b}")
    b = cc.connected(0, 7)
    print(f"cc.connected(0, 7): {b}")
    b = cc.connected(8, 7)
    print(f"cc.connected(8, 7): {b}")
    b = cc.connected(8, 9)
    print(f"cc.connected(8, 9): {b}")
    b = cc.connected(11, 9)
    print(f"cc.connected(11, 9): {b}")
