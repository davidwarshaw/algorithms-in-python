#!/usr/bin/env python

from RedBlackNode import RedBlackNode


class RedBlackBST(object):
    def __init__(self):
        self.root = None

    def _print(self):
        self._depth_first(self.root, 0)

    def _ordered_print(self, node):
        if node.left is not None:
            self._ordered_print(node.left)
        print(node)
        if node.right is not None:
            self._ordered_print(node.right)

    def _depth_first(self, node, depth):
        if node is None:
            return
        for i in range(depth):
            print(' ', end='')
        print('└', end='')
        print(node)
        self._depth_first(node.left, depth + 1)
        self._depth_first(node.right, depth + 1)

    def _size(self, node):
        return node.n if node is not None else 0

    def _is_red(self, node):
        return node.red if node else False

    def _rotate_left(self, parent):
        new_parent = parent.right
        parent.right = new_parent.left
        new_parent.left = parent

        new_parent.red = parent.red
        parent.red = True

        new_parent.n = parent.n
        parent.n = self._size(parent.left) + self._size(parent.right) + 1
        return new_parent

    def _rotate_right(self, parent):
        new_parent = parent.left
        parent.left = new_parent.right
        new_parent.right = parent

        new_parent.red = parent.red
        parent.red = True

        new_parent.n = parent.n
        parent.n = self._size(parent.left) + self._size(parent.right) + 1
        return new_parent

    def _flip_colors(self, parent):
        parent.red = True
        parent.left.red = False
        parent.right.red = False

    def _put(self, parent, key, value):
        if parent is None:
            return RedBlackNode(key, value, 1, True)
        if key < parent.key:
            parent.left = self._put(parent.left, key, value)
        elif key > parent.key:
            parent.right = self._put(parent.right, key, value)
        else:
            parent.value = value

        if self._is_red(parent.right) and not self._is_red(parent.left):
            parent = self._rotate_left(parent)
        if self._is_red(parent.left) and self._is_red(parent.left.left):
            parent = self._rotate_right(parent)
        if self._is_red(parent.left) and self._is_red(parent.right):
            self._flip_colors(parent)

        parent.n = self._size(parent.left) + self._size(parent.right) + 1
        return parent

    def _get(self, parent, key):
        if parent is None:
            return None
        if key < parent.key:
            return self._get(parent.left, key)
        elif key > parent.key:
            return self._get(parent.right, key)
        return parent.value

    def _min(self, parent):
        if parent.left is None:
            return parent
        return self._min(parent.left)

    def _max(self, parent):
        if parent.right is None:
            return parent
        return self._max(parent.right)

    def _floor(self, parent, key):
        if parent is None:
            return None
        if key < parent.key:
            return self._floor(parent.left, key)
        potential = self._floor(parent.right, key)
        if potential is not None:
            return potential
        else:
            return parent.value

    def _ceil(self, parent, key):
        if parent is None:
            return None
        if key > parent.key:
            return self._ceil(parent.right, key)
        potential = self._ceil(parent.left, key)
        if potential is not None:
            return potential
        else:
            return parent.value

    def _select(self, parent, rank):
        if parent is None:
            return None
        if parent.left is not None:
            left_size = self._size(parent.left)
        else:
            left_size = 0
        if rank < left_size:
            return self._select(parent.left, rank)
        if rank > left_size:
            return self._select(parent.right, rank - left_size - 1)
        else:
            return parent.key

    def _rank(self, parent, key):
        if parent is None:
            return 0
        if parent.left is not None:
            left_size = self._size(parent.left)
        else:
            left_size = 0
        if key < parent.key:
            return self._rank(parent.left, key)
        if key > parent.key:
            return self._rank(parent.right, key) + left_size + 1
        else:
            return left_size

    def _delete_min(self, parent):
        if parent.left is None:
            return parent.right
        parent.left = self._delete_min(parent.left)
        parent.n = self._size(parent.left) + self._size(parent.right) + 1
        return parent

    def _delete_max(self, parent):
        if parent.right is None:
            return parent.left
        parent.right = self._delete_max(parent.right)
        parent.n = self._size(parent.left) + self._size(parent.right) + 1
        return parent

    def _delete(self, parent, key):
        if parent is None:
            return None
        if key < parent.key:
            parent.left = self._delete(parent.left, key)
        elif key > parent.key:
            parent.right = self._delete(parent.right, key)
        else:
            if parent.right is None:
                return parent.left
            if parent.left is None:
                return parent.right

            successor = self._min(parent.right)
            successor.right = self._delete_min(parent.right)
            successor.left = parent.left
            parent = successor

        parent.n = self._size(parent.left) + self._size(parent.right) + 1
        return parent

    def _range(self, node, min_key, max_key, keys_in_range):
        if node is None:
            return None
        if node.key > min_key:
            self._range(node.left, min_key, max_key, keys_in_range)
        if node.key >= min_key and node.key <= max_key:
            keys_in_range.append(node)
        if node.key < max_key:
            self._range(node.right, min_key, max_key, keys_in_range)

    def ordered_print(self):
        self._ordered_print(self.root)

    def size(self):
        return self._size(self.root)

    def put(self, key, value):
        self.root = self._put(self.root, key, value)
        self.root.red = False

    def get(self, key):
        return self._get(self.root, key)

    def min(self):
        return self._min(self.root).value

    def max(self):
        return self._max(self.root).value

    def floor(self, key):
        return self._floor(self.root, key)

    def ceil(self, key):
        return self._ceil(self.root, key)

    def select(self, rank):
        return self._select(self.root, rank)

    def rank(self, key):
        return self._rank(self.root, key)

    def delete_min(self):
        self.root = self._delete_min(self.root)

    def delete_max(self):
        self.root = self._delete_max(self.root)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def range(self, min_key, max_key):
        keys_in_range = []
        self._range(self.root, min_key, max_key, keys_in_range)
        return keys_in_range


if __name__ == '__main__':
    rbt = RedBlackBST()
    rbt.put(1, 'one')
    rbt.put(2, 'two')
    rbt.put(3, 'three')
    rbt.put(4, 'four')
    rbt.put(5, 'five')
    rbt.put(6, 'six')
    rbt.put(9, 'nine')
    rbt.put(15, 'fifteen')
    rbt._print()

    rbt = RedBlackBST()
    rbt.put(4, 'four')
    rbt.put(5, 'five')
    rbt.put(6, 'six')
    rbt.put(1, 'one')
    rbt.put(9, 'nine')
    rbt.put(15, 'fifteen')
    rbt.put(2, 'two')
    rbt.put(3, 'three')
    rbt._print()
    print(rbt.get(2))
    print(rbt.min())
    print(rbt.max())
    print(rbt.floor(11))
    print(rbt.floor(5))
    print(rbt.ceil(11))
    print(rbt.ceil(5))

    for input, expected in [(0, 1), (5, 6), (20, None)]:
        actual = rbt.select(input)
        print(f"\n{input} -> {actual} == {expected}: {actual == expected}")

    for input, expected in [(1, 0), (6, 5), (0, 0)]:
        actual = rbt.rank(input)
        print(f"\n{input} -> {actual} == {expected}: {actual == expected}")

    print('\ninitial')
    rbt._print()

    print('\ndelete_min()')
    rbt.delete_min()
    rbt._print()

    print('\ndelete_max()')
    rbt.delete_max()
    rbt._print()

    print('\nrbt.delete(6)')
    rbt.delete(6)
    rbt._print()

    print('\nrbt.put(6, \'six\')')
    rbt.put(6, 'six')
    rbt._print()

    print('\rbt.put(6, \'six again\')')
    rbt.put(6, 'six again')
    rbt._print()

    print('\nrbt.delete(15)')
    rbt.delete(15)
    rbt._print()

    print('\nrbt.put(15, \'fifteen\')')
    rbt.put(15, 'fifteen')
    rbt._print()

    print('\nrbt.delete(4)')
    rbt.delete(4)
    rbt._print()

    print('\nrbt.put(4, \'four\')')
    rbt.put(4, 'four')
    rbt._print()

    print('\nOrdered Print')
    rbt.ordered_print()

    print('\nrbt.range(3, 10)')
    rbt._print()
    nodes = rbt.range(3, 10)
    for node in nodes:
        print(node)
