#!/usr/bin/env python

from math import floor


class Heap(object):

    # Parent: floor(k / 2)
    # Children: (2k, 2k + 1)

    def __init__(self):
        self.items = []
        # Heap starts at k = 1
        self.items.append(None)

    def __str__(self):
        return str(self.items)

    def _print(self):
        self._depth_first(1, 0)
        print('')

    def _depth_first(self, k, depth):
        for i in range(depth):
            print(' ', end='')
        print('└', end='')
        print(self.items[k])
        left = 2 * k
        right = (2 * k) + 1
        if left < len(self.items):
            self._depth_first(left, depth + 1)
        if right < len(self.items):
            self._depth_first(right, depth + 1)

    def _sink(self, k):
        while 2 * k < len(self.items):
            left = 2 * k
            bigger_child = left

            right = (2 * k) + 1
            if right < len(self.items):
                bigger_child = right if self.items[right] > self.items[left] else left

            if self.items[k] < self.items[bigger_child]:
                # Swap parent with bigger child
                temp = self.items[k]
                self.items[k] = self.items[bigger_child]
                self.items[bigger_child] = temp
                k = bigger_child
            else:
                break

    def _swim(self, k):
        while k > 1 and self.items[k] > self.items[floor(k / 2)]:
            # Swap child with parent
            temp = self.items[k]
            self.items[k] = self.items[floor(k / 2)]
            self.items[floor(k / 2)] = temp

            # Go up to parent
            k = floor(k / 2)

    def insert(self, item):
        self.items.append(item)
        self._swim(len(self.items) - 1)

    def remove_max(self):
        max = self.items[1]
        self.items[1] = self.items[len(self.items) - 1]
        del self.items[-1:]
        self._sink(1)
        return max


if __name__ == '__main__':
    a = Heap()
    a.insert(5)
    a.insert(6)
    a.insert(1)
    a.insert(4)
    a.insert(2)
    a.insert(3)
    print(a)
    a._print()
    print(a.remove_max())
    print(a)
    a._print()
