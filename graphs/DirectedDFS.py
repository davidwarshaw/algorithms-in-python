#!/usr/bin/env python

from DiGraph import DiGraph


class DirectedDFS(object):

    def __init__(self, g, s):
        self.s = s
        self.marked = [False] * g.num_vertices()
        self.count = 0
        self._dfs(g, s)

    def __str__(self):
        return str(self.count)

    def _print(self):
        print(f"s: {self.s}")
        for v in range(len(self.marked)):
            print(f"{v}: {self.marked[v]}")

    def _dfs(self, g, v):
        self.marked[v] = True
        self.count += 1
        for w in g.adjacent_vertices(v):
            if not self.marked[w]:
                self._dfs(g, w)

    def marked(self, v):
        return self.marked[v]

    def count(self):
        return self.count


if __name__ == '__main__':
    a = DiGraph(13)
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

    dfs = DirectedDFS(a, 0)
    dfs._print()
