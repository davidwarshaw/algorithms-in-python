#!/usr/bin/env python


class LinearProbingHashST(object):
    def __init__(self, m=4):
        self.n = 0
        self.m = m
        self.keys = [None] * self.m
        self.values = [None] * self.m

    def __str__(self):
        return ', '.join([f"({self.keys[i]}, {self.values[i]})" for i in range(self.m)])

    def _print(self):
        for i in range(self.m):
            print(f"({self.keys[i]}, {self.values[i]})")

    def _hash(self, key):
        bytes_key = str.encode(str(key))
        numeric_key = int.from_bytes(bytes_key, byteorder='little')
        return numeric_key % self.m

    def _resize(self, new_m):
        new_table = LinearProbingHashST(new_m)
        for key, value in self.entries():
            new_table.put(key, value)
        self.n = new_table.n
        self.m = new_table.m
        self.keys = new_table.keys
        self.values = new_table.values

    def put(self, key, value):
        if self.n > self.m / 2:
            self._resize(self.m * 2)

        hash_key = self._hash(key)
        for offset in range(hash_key, hash_key + self.m):
            i = offset % self.m
            if not self.keys[i]:
                self.keys[i] = key
                self.values[i] = value
                self.n += 1
                return
            if self.keys[i] == key:
                self.values[i] = value
                return

    def _get(self, key):
        hash_key = self._hash(key)
        for offset in range(hash_key, hash_key + self.m):
            i = offset % self.m
            if not self.keys[i]:
                return None
            if self.keys[i] == key:
                return i
        return None

    def get(self, key):
        i = self._get(key)
        return self.values[i] if i else None

    def delete(self, key):
        key_index = self._get(key)
        if not key_index:
            return
        self.keys[key_index] = None
        self.values[key_index] = None
        for offset in range(key_index + 1, key_index + self.m - 1):
            if not self.keys[key_index]:
                break
            i = offset % len(self.keys)
            self.put(self.keys[i], self.values[i])
            self.keys[i] = None
            self.values[i] = None
        self.n -= 1
        if self.n > 0 and self.n <= self.m // 8:
            self._resize(m // 2)

    def contains(self, key):
        return self._get(key) is not None

    def entries(self):
        entries = []
        for i in range(self.m):
            if self.keys[i]:
                entries.append((self.keys[i], self.values[i]))
        return entries

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return self.n


if __name__ == '__main__':
    st = LinearProbingHashST()
    st.put(4, 'four')
    st.put(5, 'five')
    st.put(6, 'six')
    st.put(1, 'one')
    st.put(9, 'nine')
    st.put(15, 'fifteen')
    st.put(2, 'two')
    st.put(3, 'three')
    st._print()
    print(st.get(2))

    print('\nst.delete(6)')
    st.delete(6)
    st._print()

    print('\nst.put(6, \'six\')')
    st.put(6, 'six')
    st._print()

    print('\nst.put(6, \'six again\')')
    st.put(6, 'six again')
    st._print()

    print('\nst.delete(15)')
    st.delete(15)
    st._print()

    print('\nst.put(15, \'fifteen\')')
    st.put(15, 'fifteen')
    st._print()

    print('\nst.delete(4)')
    st.delete(4)
    st._print()

    print('\nst.put(4, \'four\')')
    st.put(4, 'four')
    st._print()
