#!/usr/bin/env python

import sys
from itertools import combinations

def parse(lines):
    result = []
    for line in lines:
        result.append(int(line))
    return result

def combs(items, total):
    for i in range(1, len(items)+1):
        for j in combinations(items, i):
            if sum(j) == total:
                yield j

def combs2(items, total):
    for i in range(1, len(items)+1):
        for j in combinations(items, i):
            if sum(j) == total:
                yield j
def main():
    containers = parse(sys.stdin)
    c =  [i for i in combs(containers, 150)]
    c_len = len(c)
    print "Task 1: %s" % c_len

    c_len = [len(i) for i in c]
    min_c_len = min(c_len)
    c2_len = sum([1 for i in c_len if i == min_c_len])
    print "Task 2: %s" % c2_len

if __name__ == "__main__":
    main()
