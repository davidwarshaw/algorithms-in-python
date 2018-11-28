#!/usr/bin/env python

from Graph import Graph


class TwoColor(object):

    def __init__(self, g):
        self.marked = [False] * g.num_vertices()
        self.color = [False] * g.num_vertices()
        self.bipartite = True
        for s in range(g.num_vertices()):
            if not self.marked[s]:
                self._dfs(g, s)

    def __str__(self):
        return str(self.id)

    def _print(self):
        for v in range(len(self.color)):
            print(f"{v}: {self.color[v]}")

    def _dfs(self, g, v):
        self.marked[v] = True
        for w in g.adjacent_vertices(v):
            if not self.marked[w]:
                self.color[w] = not self.color[v]
                self._dfs(g, w)
            elif self.color[w] == self.color[v]:
                self.bipartite = False

    def is_bipartite(self):
        return self.bipartite


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

    tc = TwoColor(a)
    tc._print()
    b = tc.is_bipartite()
    print(f"tc.is_bipartite(): {b}")

    a = Graph(4)
    a.add_edge(0, 1)
    a.add_edge(1, 2)
    a.add_edge(2, 3)
    a.add_edge(3, 0)
    a._print()

    tc = TwoColor(a)
    tc._print()
    b = tc.is_bipartite()
    print(f"tc.is_bipartite(): {b}")

    a = Graph(4)
    a.add_edge(0, 1)
    a.add_edge(1, 2)
    a.add_edge(2, 3)
    a._print()

    tc = TwoColor(a)
    tc._print()
    b = tc.is_bipartite()
    print(f"tc.is_bipartite(): {b}")
