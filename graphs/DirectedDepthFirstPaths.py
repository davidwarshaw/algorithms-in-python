#!/usr/bin/env python

# Path hack to import from sibling dir
import sys
import os
sys.path.insert(0, os.path.abspath('..'))

from fundamentals.Stack import Stack

from DiGraph import DiGraph


class DepthFirstPaths(object):

    def __init__(self, g, s):
        self.s = s
        self.marked = [False] * g.num_vertices()
        self.edge_to = [None] * g.num_vertices()
        self._dfs(g, s)

    def __str__(self):
        return str(self.edge_to)

    def _print(self):
        print(f"s: {self.s}")
        for edge_from in range(len(self.edge_to)):
            print(f"{edge_from} -> {self.edge_to[edge_from]}: {self.marked[edge_from]}")

    def _dfs(self, g, v):
        self.marked[v] = True
        for w in g.adjacent_vertices(v):
            if not self.marked[w]:
                self.edge_to[w] = v
                self._dfs(g, w)

    def has_path_to(self, v):
        return self.marked[v]

    def path_to(self, v):
        if not has_path_to(v):
            return None
        stack = Stack()
        x = v
        while x != s:
            stack.push(x)
            x = self.edge_to[x]
        return stack.items


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

    dfp = DepthFirstPaths(a, 0)
    dfp._print()
