#!/usr/bin/env python

# Path hack to import from sibling dir
import sys
import os
sys.path.insert(0, os.path.abspath('..'))

from fundamentals.Bag import Bag
from searching.SymbolTable import SymbolTable


class SymbolGraph(object):

    def __init__(self, v):
        self.v = v
        self.e = 0
        self.st = SymbolTable()
        self.keys = []
        self.vertices = []
        for v in range(v):
            self.vertices.append(Bag())

    def __str__(self):
        return str(self.vertices)

    def _print(self):
        print(f"V: {self.num_vertices()} E: {self.num_edges()}")
        for v in range(self.num_vertices()):
            print(f"{v}: {self.keys[v]}: {self.vertices[v]}")

    def num_vertices(self):
        return self.v

    def num_edges(self):
        return self.e

    def add_edge(self, v_key, w_key):
        if self.st.contains(v_key):
            v_index = self.st.get(v_key)
        else:
            v_index = len(self.keys)
            self.keys.append(v_key)
            self.st.put(v_key, v_index)

        if self.st.contains(w_key):
            w_index = self.st.get(w_key)
        else:
            w_index = len(self.keys)
            self.keys.append(w_key)
            self.st.put(w_key, w_index)

        self.vertices[v_index].add(w_index)
        self.vertices[w_index].add(v_index)
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

    def contains(self, key):
        return self.st.contains(key)

    def index(self, key):
        return self.st.get(key)

    def name(self, v):
        return self.keys[v]


if __name__ == '__main__':
    a = SymbolGraph(10)
    a.add_edge('JFK', 'MCO')
    a.add_edge('ORD', 'DEN')
    a.add_edge('ORD', 'HOU')
    a.add_edge('DFW', 'PHX')
    a.add_edge('JFK', 'ATL')
    a.add_edge('ORD', 'DFW')
    a.add_edge('ORD', 'PHX')
    a.add_edge('ATL', 'HOU')
    a.add_edge('DEN', 'PHX')
    a.add_edge('PHX', 'LAX')
    a.add_edge('JFK', 'ORD')
    a.add_edge('DEN', 'LAS')
    a.add_edge('DFW', 'HOU')
    a.add_edge('ORD', 'ATL')
    a.add_edge('LAS', 'LAX')
    a.add_edge('ATL', 'MCO')
    a.add_edge('HOU', 'MCO')
    a.add_edge('LAS', 'PHX')
    print(a)
    a._print()

    b = a.contains('LAX')
    print('a.contains(\'LAX\')')
    print(b)

    b = a.index('JFK')
    print('a.index(\'JFK\')')
    print(b)

    b = a.name(1)
    print('a.name(1)')
    print(b)
