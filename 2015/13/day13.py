#!/usr/bin/env python

import sys
import re

from collections import defaultdict
from itertools import permutations

def dmap(lines):
    map = defaultdict(dict)
    v = {"gain": int, "lose": lambda x: - int(x)}
    rexp = r'(\S+) would (gain|lose) (\d+) happiness units by sitting next to (\S+)\.'
    for line in lines:
        user1, action, value, user2 = re.match(rexp, line).groups()
        value = v[action](value)
        map[user1][user2] = value
    return map

def walk_map(map):
    for route in permutations(map.keys()):
        s = sum(map[u1][u2]+map[u2][u1] for u1,u2 in zip(route, route[1:]))
        s += map[route[0]][route[-1]] + map[route[-1]][route[0]]
        yield s

def main():
    map = dmap(sys.stdin)
    print reduce(max,walk_map(map))
    for p in map.keys():
        map["me"][p] = 0
        map[p]["me"] = 0
    print reduce(max,walk_map(map))

if __name__ == "__main__":
    main()
