#!/usr/bin/env python

from SymbolGraph import SymbolGraph
from BreadthFirstPaths import BreadthFirstPaths


class DegreesOfSeparation(object):

    def __init__(self, g):
        self.g = g

    def degrees_of_separation(self, s, t):
        s_index = self.g.index(s)
        t_index = self.g.index(t)
        if s_index is None or t_index is None:
            return None
        self.bfs = BreadthFirstPaths(self.g, s_index)
        path = self.bfs.path_to(t_index)
        return path.size() if path else None


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

    ds = DegreesOfSeparation(a)
    b = ds.degrees_of_separation('JFK', 'LAX')
    print('ds.degrees_of_separation(\'JFK\', \'LAX\')')
    print(b)

    ds = DegreesOfSeparation(a)
    b = ds.degrees_of_separation('DFW', 'LAX')
    print('ds.degrees_of_separation(\'DFW\', \'LAX\')')
    print(b)

    ds = DegreesOfSeparation(a)
    b = ds.degrees_of_separation('DFW', 'PHX')
    print('ds.degrees_of_separation(\'DFW\', \'PHX\')')
    print(b)
