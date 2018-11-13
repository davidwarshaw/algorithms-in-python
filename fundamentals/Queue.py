#!/usr/bin/env python

from LinkedList import LinkedList


class Queue(object):

    def __init__(self):
        self.items = LinkedList()

    def __str__(self):
        return str(self.items)

    def enqueue(self, item):
        self.items.insertAtEnd(item)

    def dequeue(self):
        dequeued = self.items.head
        self.items.removeFromBegining()
        return dequeued

    def is_empty(self):
        return self.items.size() == 0

    def size(self):
        return self.items.size()


if __name__ == '__main__':
    a = Queue()
    a.enqueue(1)
    a.enqueue(2)
    a.enqueue(3)
    print(a)
    print(a.dequeue())
    print(a.dequeue())
    print(a.dequeue())
    print(a.dequeue())
    print(a)
