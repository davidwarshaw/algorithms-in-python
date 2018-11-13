#!/usr/bin/env python

from Heap import Heap


class MaxPQ(object):

    def __init__(self):
        self.items = Heap()

    def __str__(self):
        return str(self.items)

    def _print(self):
        self.items._print()

    def insert(self, item):
        self.items.insert(item)

    def max(self, item):
        self.items.items[1]

    def remove_max(self):
        self.items.remove_max()

    def is_empty(self):
        return self.items.size() == 0

    def size(self):
        return self.items.size()


if __name__ == '__main__':
    a = MaxPQ()
    a.insert(5)
    a.insert(6)
    a.insert(1)
    a.insert(4)
    a.insert(2)
    a.insert(3)
    print(a)
    a._print()
    print(a.remove_max())
    print(a.remove_max())
    print(a)
    a._print()
