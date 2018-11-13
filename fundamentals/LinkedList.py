#!/usr/bin/env python


class Node(object):

    def __init__(self, item):
        self.next = None
        self.item = item

    def __str__(self):
        return str(self.item)


class LinkedList(object):

    def __init__(self):
        self.head = None

    def __str__(self):
        node = self.head
        concatenated = ''
        while node:
            concatenated += str(node) + ' -> '
            node = node.next
        return concatenated

    def size(self):
        node = self.head
        count = 0
        while node:
            count += 1
            node = node.next
        return count

    def tail(self):
        node = self.head
        while node and node.next:
            node = node.next
        return node

    def insertAtBegining(self, item):
        new = Node(item)
        new.next = self.head
        self.head = new

    def insertAtEnd(self, item):
        if self.size() > 0:
            new = Node(item)
            tail = self.tail()
            tail.next = new
        else:
            self.insertAtBegining(item)

    def removeFromBegining(self):
        if self.size() > 0:
            self.head = self.head.next

    def removeFromEnd(self):
        if self.size() == 1:
            self.head = None
        elif self.size() > 1:
            node = self.head
            prevNode = node
            while node.next:
                prevNode = node
                node = node.next
            prevNode.next = None

    def clear(self):
        self.head = None


if __name__ == '__main__':
    a = LinkedList()
    a.insertAtEnd(1)
    a.insertAtEnd(2)
    a.insertAtEnd(3)
    print(a)
    a.clear()
    a.insertAtBegining(1)
    a.insertAtBegining(2)
    a.insertAtBegining(3)
    print(a)
    a.clear()
    a.insertAtBegining(1)
    a.insertAtBegining(2)
    a.insertAtEnd(3)
    a.insertAtEnd(4)
    print(a)
    a.clear()
    a.insertAtEnd(1)
    a.insertAtEnd(2)
    a.insertAtEnd(3)
    print(a)
    a.removeFromEnd()
    print(a)
    a.removeFromEnd()
    print(a)
    a.removeFromEnd()
    print(a)
    a.clear()
    a.insertAtEnd(1)
    a.insertAtEnd(2)
    a.insertAtEnd(3)
    print(a)
    a.removeFromBegining()
    print(a)
    a.removeFromBegining()
    print(a)
    a.removeFromBegining()
    print(a)
    a.clear()
    a.insertAtEnd(1)
    a.insertAtEnd(2)
    a.insertAtEnd(3)
    a.removeFromBegining()
    a.removeFromBegining()
    a.removeFromBegining()
    print(a)
