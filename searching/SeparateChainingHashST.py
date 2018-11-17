#!/usr/bin/env python

from SymbolTable import SymbolTable
from math import floor


class SeparateChainingHashST(object):
    def __init__(self):
        self.symbolTables = []
        self.m = 4
        for i in range(self.m):
            self.symbolTables.append(SymbolTable())

    def __str__(self):
        return ', '.join([f"{i}: {self.symbolTables[i]}" for i in range(self.m)])

    def _print(self):
        for i in range(self.m):
            print(f"{i}: {self.symbolTables[i]}")

    def _hash(self, key):
        bytes_key = str.encode(str(key))
        numeric_key = int.from_bytes(bytes_key, byteorder='little')
        return numeric_key % self.m

    def put(self, key, value):
        self.symbolTables[self._hash(key)].put(key, value)

    def get(self, key):
        return self.symbolTables[self._hash(key)].get(key)

    def delete(self, key):
        self.symbolTables[self._hash(key)].delete(key)

    def contains(self, key):
        return self.symbolTables[self._hash(key)].contains(key)

    def keys(self):
        keys = []
        for i in range(self.m):
            keys.append(self.symbolTables[i].keys())
        return keys

    def is_empty(self):
        return self.size() == 0

    def size(self):
        n = 0
        for i in range(self.m):
            n += self.symbolTables[i].size()
        return n


if __name__ == '__main__':
    st = SeparateChainingHashST()
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
