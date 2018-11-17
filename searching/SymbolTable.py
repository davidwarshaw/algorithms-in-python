#!/usr/bin/env python

# Path hack to import from sibling dir
import sys
import os
sys.path.insert(0, os.path.abspath('..'))

from math import floor
from fundamentals.LinkedList import LinkedList


class SymbolTable(object):
    def __init__(self):
        self.items = LinkedList()

    def __str__(self):
        return str(self.items)

    def _print(self):
        node = self.items.head
        while node:
            print(node)
            node = node.next

    def _move_key_to_head(self, key):
        if not self.items.head:
            return None
        first_item = self.items.head.item
        item = first_item
        while True:
            self.items.removeFromBegining()
            self.items.insertAtEnd(item)
            item = self.items.head.item
            if item[0] == key:
                return True
            if item == first_item:
                return False

    def put(self, key, value):
        node = self._get(key)
        if node:
            node.item = (key, value)
        else:
            self.items.insertAtEnd((key, value))

    def _get(self, key):
        node = self.items.head
        while node and node.item[0] != key:
            node = node.next
        return node

    def get(self, key):
        return self._get(key).item[1]

    def delete(self, key):
        if self._move_key_to_head(key):
            self.items.removeFromBegining()

    def contains(self, key):
        return self.get(key) is not None

    def entries(self):
        entries = []
        node = self.items.head
        while node:
            entries.append(node.item)
            node = node.next
        return entries

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return self.items.size()

    def min(self):
        node = self.items.head
        if not node:
            return None
        min_key = node.item[0]
        while node:
            min_key = min(node.item[0], min_key)
            node = node.next
        return min_key

    def max(self):
        node = self.items.head
        if not node:
            return None
        min_key = node.item[0]
        while node:
            min_key = max(node.item[0], min_key)
            node = node.next
        return min_key

    def floor(self, key):
        node = self.items.head
        if not node:
            return None
        floor_key = None
        while node:
            node_key = node.item[0]
            if node_key <= key:
                floor_key = max(node_key, floor_key) if floor_key else node_key
            node = node.next
        return floor_key

    def ceil(self, key):
        node = self.items.head
        if not node:
            return None
        ceil_key = None
        while node:
            node_key = node.item[0]
            if node_key >= key:
                ceil_key = min(node_key, ceil_key) if ceil_key else node_key
            node = node.next
        return ceil_key

    def select(self, rank):
        node = self.items.head
        if not node:
            return None
        # This is _bad_
        while node:
            node_key = node.item[0]
            node_rank = self.rank(node_key)
            if node_rank == rank:
                return node_key
            node = node.next
        return None

    def rank(self, key):
        node = self.items.head
        if not node:
            return None
        num_smaller = 0
        while node:
            node_key = node.item[0]
            if node_key < key:
                num_smaller += 1
            node = node.next
        return num_smaller


if __name__ == '__main__':
    st = SymbolTable()
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
