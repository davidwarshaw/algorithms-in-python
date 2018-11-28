#!/usr/bin/env python

from Graph import Graph


class Cycle(object):

    def __init__(self, g):
        self.marked = [False] * g.num_vertices()
        self.cycle = False
        for s in range(g.num_vertices()):
            if not self.marked[s]:
                self._dfs(g, s, s)

    def __str__(self):
        return str(self.id)

    def _print(self):
        for v in range(len(self.marked)):
            print(f"{v}: {self.marked[v]}")

    def _dfs(self, g, v, u):
        self.marked[v] = True
        for w in g.adjacent_vertices(v):
            if not self.marked[w]:
                self._dfs(g, w, v)
            elif w != u:
                self.cycle = True

    def has_cycle(self):
        return self.cycle


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

    c = Cycle(a)
    c._print()
    b = c.has_cycle()
    print(f"c.has_cycle(): {b}")

    a = Graph(4)
    a.add_edge(0, 1)
    a.add_edge(1, 2)
    a.add_edge(2, 3)
    a.add_edge(3, 0)
    a._print()

    c = Cycle(a)
    c._print()
    b = c.has_cycle()
    print(f"c.has_cycle(): {b}")

    a = Graph(4)
    a.add_edge(0, 1)
    a.add_edge(1, 2)
    a.add_edge(2, 3)
    a._print()

    c = Cycle(a)
    c._print()
    b = c.has_cycle()
    print(f"c.has_cycle(): {b}")
