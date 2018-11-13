#!/usr/bin/env python


class RedBlackNode(object):
    def __init__(self, key, value, n, color):
        self.key = key
        self.value = value
        self.n = n
        self.left = None
        self.right = None
        self.red = color

    def __str__(self):
        color = 'red' if self.red else 'black'
        return str(self.key) + ': ' + str(self.value) + ' ' + str(self.n) + ' ' + color
