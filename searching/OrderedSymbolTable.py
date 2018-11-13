#!/usr/bin/env python

# Path hack to import from sibling dir
import sys
import os
sys.path.insert(0, os.path.abspath('..'))

from fundamentals.LinkedList import LinkedList
from math import floor


class OrderedSymbolTable(object):
    def __init__(self):
        self.keys = []
        self.values = []
        self.n = 0

    def __str__(self):
        return ', '.join([f"({self.keys[i]}, {self.values[i]})" for i in range(self.n)])

    def _print(self):
        for i in range(self.n):
            print(f"({self.keys[i]}, {self.values[i]})")

    def _rank(self, key, low, high):
        if high < low:
            return low
        mid = floor(low + ((high - low) / 2))
        if key > self.keys[mid]:
            return self._rank(key, mid + 1, high)
        if key < self.keys[mid]:
            return self._rank(key, low, mid - 1)
        if key == self.keys[mid]:
            return mid

    def put(self, key, value):
        rank = self.rank(key)
        if rank < self.n and self.keys[rank] == key:
            self.values[rank] = value
            return

        if not self.is_empty():
            last_key = self.keys[self.n - 1]
            last_value = self.values[self.n - 1]
        else:
            last_key = key
            last_value = value
        self.keys.append(last_key)
        self.values.append(last_value)

        for i in range(self.n, rank, -1):
            self.keys[i] = self.keys[i - 1]
            self.values[i] = self.values[i - 1]

        self.keys[rank] = key
        self.values[rank] = value
        self.n += 1
        print(self.keys)

    def get(self, key):
        rank = self.rank(key)
        return self.values[rank] if rank < self.n and self.keys[rank] == key else None

    def delete(self, key):
        rank = self.rank(key)
        if rank >= self.n or self.keys[rank] != key:
            return

        for i in range(rank, self.n - 1):
            self.keys[i] = self.keys[i + 1]
            self.values[i] = self.values[i + 1]

        del self.keys[self.n - 1]
        del self.values[self.n - 1]
        self.n -= 1

    def contains(self, key):
        return self.get(key) is not None

    def keys(self):
        return self.keys

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return self.n

    def min(self):
        return self.keys[0] if not self.is_empty() else None

    def max(self):
        return self.keys[self.n - 1] if not self.is_empty() else None

    def floor(self, key):
        rank = self.rank(key)
        if rank >= self.n:
            return None
        return key if self.keys[rank] == key else self.keys[rank - 1]

    def ceil(self, key):
        rank = self.rank(key)
        return self.keys[rank] if rank < self.n else None

    def select(self, rank):
        return self.keys[rank] if rank < self.n else None

    def rank(self, key):
        return self._rank(key, 0, self.n - 1)


if __name__ == '__main__':
    st = OrderedSymbolTable()
    st.put(4, 'four')
    st.put(5, 'five')
    st.put(6, 'six')
    st.put(1, 'one')
    st.put(9, 'nine')
    st.put(15, 'fifteen')
    st.put(2, 'two')
    st.put(3, 'three')
    st._print()
    print(st.get(2))
    print(st.min())
    print(st.max())
    print(st.floor(11))
    print(st.floor(5))
    print(st.ceil(11))
    print(st.ceil(5))

    for input, expected in [(0, 1), (5, 6), (20, None)]:
        actual = st.select(input)
        print(f"\n{input} -> {actual} == {expected}: {actual == expected}")

    for input, expected in [(1, 0), (6, 5), (0, 0)]:
        actual = st.rank(input)
        print(f"\n{input} -> {actual} == {expected}: {actual == expected}")

    print('\nst.delete(6)')
    st.delete(6)
    st._print()

    print('\nst.put(6, \'six\')')
    st.put(6, 'six')
    st._print()

    print('\nst.put(6, \'six again\')')
    st.put(6, 'six again')
    st._print()

    print('\nst.delete(15)')
    st.delete(15)
    st._print()

    print('\nst.put(15, \'fifteen\')')
    st.put(15, 'fifteen')
    st._print()

    print('\nst.delete(4)')
    st.delete(4)
    st._print()

    print('\nst.put(4, \'four\')')
    st.put(4, 'four')
    st._print()
