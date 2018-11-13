#!/usr/bin/env python

from LinkedList import LinkedList


class Bag(object):

    def __init__(self):
        self.items = LinkedList()

    def __str__(self):
        return str(self.items)

    def add(self, item):
        self.items.insertAtEnd(item)

    def is_empty(self):
        return self.items.size() == 0

    def size(self):
        return self.items.size()


if __name__ == '__main__':
    a = Bag()
    a.add(1)
    a.add(2)
    a.add(3)
    print(a)
