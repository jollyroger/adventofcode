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
    print sum([1 for i in combs(containers, 150)])

if __name__ == "__main__":
    main()
