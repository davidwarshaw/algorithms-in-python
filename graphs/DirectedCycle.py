#!/usr/bin/env python

# Path hack to import from sibling dir
import sys
import os
sys.path.insert(0, os.path.abspath('..'))

from fundamentals.Stack import Stack
from DiGraph import DiGraph


class DirectedCycle(object):

    def __init__(self, g):
        self.marked = [False] * g.num_vertices()
        self.edge_to = [None] * g.num_vertices()
        self.cycle = None
        self.on_stack = [False] * g.num_vertices()
        for s in range(g.num_vertices()):
            if not self.marked[s]:
                self._dfs(g, s)

    def __str__(self):
        return str(self.id)

    def _print(self):
        for v in range(len(self.marked)):
            print(f"{v}: {self.marked[v]}")

    def _dfs(self, g, v):
        print(f"v : {v}")
        self.marked[v] = True
        self.on_stack[v] = True
        for w in g.adjacent_vertices(v):
            print(f"w: {w}")
            if self.has_cycle():
                return
            if not self.marked[w]:
                self.edge_to[w] = v
                self._dfs(g, w)
            elif self.on_stack[w]:
                self.cycle = Stack()
                x = v
                while x != w:
                    print(f"x: {x}")
                    self.cycle.push(x)
                    x = self.edge_to[x]
                self.cycle.push(w)
                self.cycle.push(v)
        self.on_stack[v] = True

    def has_cycle(self):
        return self.cycle is not None

    def get_cycle(self):
        return self.cycle


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

    c = DirectedCycle(a)
    c._print()
    b = c.has_cycle()
    print(f"c.has_cycle(): {b}")

    a = DiGraph(4)
    a.add_edge(0, 1)
    a.add_edge(1, 2)
    a.add_edge(2, 3)
    a.add_edge(3, 0)
    a._print()

    c = DirectedCycle(a)
    c._print()
    b = c.has_cycle()
    print(f"c.has_cycle(): {b}")

    a = DiGraph(4)
    a.add_edge(0, 1)
    a.add_edge(1, 2)
    a.add_edge(2, 3)
    a._print()

    c = DirectedCycle(a)
    c._print()
    b = c.has_cycle()
    print(f"c.has_cycle(): {b}")
