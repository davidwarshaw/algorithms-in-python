#!/usr/bin/env python


class QuickFind(object):

    def __init__(self, n):
        self.ids = range(n)
        self.n = n

    def __str__(self):
        return str(self.ids)

    def union(self, p, q):
        pId = self.find(p)
        qId = self.find(q)
        if pId == qId:
            return
        for i in range(len(self.ids)):
            if self.ids[i] == qId:
                self.ids[i] = pId
        self.n -= 1

    def find(self, p):
        return self.ids[p]

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def count(self):
        return self.n


class QuickUnion(object):

    def __init__(self, n):
        self.ids = range(n)
        self.n = n

    def __str__(self):
        return str(self.ids)

    def union(self, p, q):
        pId = self.find(p)
        qId = self.find(q)
        if pId == qId:
            return
        self.ids[qId] = pId
        self.n -= 1

    def find(self, p):
        node = p
        while self.ids[node] != node:
            node = self.ids[node]
        return node

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def count(self):
        return self.n


class WeightedQuickUnion(object):

    def __init__(self, n):
        self.ids = range(n)
        self.sizes = [1] * n
        self.n = n

    def __str__(self):
        return str(zip(self.ids, self.sizes))

    def union(self, p, q):
        pId = self.find(p)
        qId = self.find(q)
        if pId == qId:
            return
        if self.sizes[p] <= self.sizes[q]:
            self.ids[qId] = pId
            self.sizes[q] += self.sizes[p]
        else:
            self.ids[pId] = qId
            self.sizes[p] += self.sizes[q]
        self.n -= 1

    def find(self, p):
        node = p
        while self.ids[node] != node:
            node = self.ids[node]
        return node

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def count(self):
        return self.n


class WeightedQuickUnionPathCompression(object):

    def __init__(self, n):
        self.ids = range(n)
        self.sizes = [1] * n
        self.n = n

    def __str__(self):
        return str(zip(self.ids, self.sizes))

    def union(self, p, q):
        pId = self.find(p)
        qId = self.find(q)
        if pId == qId:
            return
        if self.sizes[p] <= self.sizes[q]:
            self.ids[qId] = pId
            self.sizes[q] += self.sizes[p]
        else:
            self.ids[pId] = qId
            self.sizes[p] += self.sizes[q]
        self.n -= 1

    def find(self, p):
        node = p
        while self.ids[node] != node:
            node = self.ids[node]
        self.ids[p] = node
        return node

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def count(self):
        return self.n


if __name__ == '__main__':
    a = QuickFind(10)
    a.union(4, 3)
    a.union(3, 8)
    a.union(6, 5)
    a.union(9, 4)
    a.union(2, 1)
    a.union(5, 0)
    a.union(7, 2)
    a.union(6, 1)
    print(a)
    print(a.count())
    print(a.find(0) == a.find(6))
    print(a.find(8) == a.find(9))
    print(a.find(0) != a.find(9))

    a = QuickUnion(10)
    a.union(4, 3)
    a.union(3, 8)
    a.union(6, 5)
    a.union(9, 4)
    a.union(2, 1)
    a.union(5, 0)
    a.union(7, 2)
    a.union(6, 1)
    print(a)
    print(a.count())
    print(a.find(0) == a.find(6))
    print(a.find(8) == a.find(9))
    print(a.find(0) != a.find(9))

    a = WeightedQuickUnion(10)
    a.union(4, 3)
    a.union(3, 8)
    a.union(6, 5)
    a.union(9, 4)
    a.union(2, 1)
    a.union(5, 0)
    a.union(7, 2)
    a.union(6, 1)
    print(a)
    print(a.count())
    print(a.find(0) == a.find(6))
    print(a.find(8) == a.find(9))
    print(a.find(0) != a.find(9))

    a = WeightedQuickUnionPathCompression(10)
    a.union(4, 3)
    a.union(3, 8)
    a.union(6, 5)
    a.union(9, 4)
    a.union(2, 1)
    a.union(5, 0)
    a.union(7, 2)
    a.union(6, 1)
    print(a)
    print(a.count())
    print(a.find(0) == a.find(6))
    print(a.find(8) == a.find(9))
    print(a.find(0) != a.find(9))
