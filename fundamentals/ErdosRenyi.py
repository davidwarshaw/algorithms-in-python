#!/usr/bin/env python

import random
import math

from UnionFind import WeightedQuickUnionPathCompression

random.seed(1)


class ErdosRenyi(object):
    def __init__(self, n):
        self.uf = WeightedQuickUnionPathCompression(n)
        self.count = self.uf.count()
        self.pairs = 0

        while self.count != 1:
            p = random.randint(0, n - 1)
            q = random.randint(0, n - 1)
            if not self.uf.connected(p, q):
                self.uf.union(p, q)
                self.pairs += 1
            self.count = self.uf.count()


if __name__ == '__main__':
    a = ErdosRenyi(10)
    print(a.count)
    print(a.pairs)

    ns = range(2, 20 + 1)
    pairs = []
    for n in ns:
        a = ErdosRenyi(n)
        pairs.append(a.pairs)
    print(pairs)
    for trial in zip(ns, pairs):
        estimated_pairs = int(round(0.5 * trial[0] * math.log(trial[0])))
        print(str(trial[1]) + ' ~= ' + str(estimated_pairs))
