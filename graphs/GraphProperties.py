#!/usr/bin/env python

import math

from SymbolGraph import SymbolGraph
from BreadthFirstPaths import BreadthFirstPaths


class GraphProperties(object):

    def __init__(self, g):
        self.g = g

    def eccentricity(self, s):
        s_index = self.g.index(s)
        if s_index is None:
            return None
        self.bfs = BreadthFirstPaths(self.g, s_index)
        lengths = []
        for v in range(self.g.num_vertices()):
            path = self.bfs.path_to(v)
            length = path.size() if path else 0
            lengths.append(length)
        return max(lengths)

    def diameter(self):
        es = [0] * self.g.num_vertices()
        for v in range(self.g.num_vertices()):
            e = self.eccentricity(self.g.name(v))
            if e is not None:
                es[v] = e
        return max(es)

    def radius(self):
        es = [0] * self.g.num_vertices()
        for v in range(self.g.num_vertices()):
            e = self.eccentricity(self.g.name(v))
            if e is not None:
                es[v] = e
        return min(es)

    def center(self):
        es = [0] * self.g.num_vertices()
        for v in range(self.g.num_vertices()):
            e = self.eccentricity(self.g.name(v))
            if e is not None:
                es[v] = e
        radius = min(es)
        for v in range(self.g.num_vertices()):
            if es[v] == radius:
                return self.g.name(v)

    def girth(self):
        lengths = []
        for v in range(self.g.num_vertices()):
            self.bfs = BreadthFirstPaths(self.g, v)
            for w in range(self.g.num_vertices()):
                path = self.bfs.path_to(w)
                cycle = v in self.g.adjacent_vertices(w)
                if path and cycle:
                    length = path.size() + 1
                    lengths.append(length)
        return min(lengths) if len(lengths) > 0 else math.inf


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

    gp = GraphProperties(a)
    b = gp.eccentricity('JFK')
    print('gp.eccentricity(\'JFK\')')
    print(b)

    gp = GraphProperties(a)
    b = gp.diameter()
    print('gp.diameter()')
    print(b)

    gp = GraphProperties(a)
    b = gp.radius()
    print('gp.radius()')
    print(b)

    gp = GraphProperties(a)
    b = gp.center()
    print('gp.center()')
    print(b)

    gp = GraphProperties(a)
    b = gp.girth()
    print('gp.girth()')
    print(b)
