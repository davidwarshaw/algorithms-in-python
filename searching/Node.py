#!/usr/bin/env python


class Node(object):
    def __init__(self, key, value, n):
        self.key = key
        self.value = value
        self.n = n
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.key) + ': ' + str(self.value) + ' ' + str(self.n)
