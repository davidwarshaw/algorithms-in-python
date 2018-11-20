#!/usr/bin/env python

# Path hack to import from sibling dir
import sys
import os
sys.path.insert(0, os.path.abspath('..'))

from fundamentals.Bag import Bag


class Graph(object):

    def __init__(self, v):
        self.v = v
        self.e = 0
        self.vertices = []
        for v in range(v):
            self.vertices.append(Bag())

    def __str__(self):
        return str(self.vertices)

    def _print(self):
        print(f"V: {self.num_vertices()} E: {self.num_edges()}")
        for v in range(self.num_vertices()):
            print(f"{v}: {self.vertices[v]}")

    def num_vertices(self):
        return self.v

    def num_edges(self):
        return self.e

    def add_edge(self, v, w):
        self.vertices[v].add(w)
        self.vertices[w].add(v)
        self.e += 1

    def adjacent_vertices(self, v):
        return [item.item for item in self.vertices[v].items]

    def degree(self, v):
        degree = 0
        for w in self.adjacent_vertices(v):
            degree += 1
        return degree

    def max_degrees(self):
        max_degrees = 0
        for v in range(self.num_vertices()):
            max_degrees = max(self.degree(v))
        return max_degrees

    def avg_degrees(self):
        return 2 * self.num_edges() / self.num_vertices()

    def num_self_loops(self):
        count = 0
        for v in range(self.num_vertices()):
            for w in self.adjacent_vertices(v):
                if v == w:
                    count += 1
        return count / 2


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
    print(a)
    a._print()
