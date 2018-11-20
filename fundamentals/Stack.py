#!/usr/bin/env python

from fundamentals.LinkedList import LinkedList


class Stack(object):

    def __init__(self):
        self.items = LinkedList()

    def __str__(self):
        return str(self.items)

    def push(self, item):
        self.items.insertAtEnd(item)

    def pop(self):
        popped = self.items.tail()
        self.items.removeFromEnd()
        return popped

    def is_empty(self):
        return self.items.size() == 0

    def size(self):
        return self.items.size()


if __name__ == '__main__':
    a = Stack()
    a.push(1)
    a.push(2)
    a.push(3)
    print(a)
    print(a.pop())
    print(a.pop())
    print(a.pop())
    print(a.pop())
    print(a)
