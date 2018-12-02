#!/usr/bin/env python

import sys
import re

def dmap(lines):
    map = {}
    for line in lines:
        loc1, loc2, dist = re.match(r'(.+) to (.*) = (\d+)', line).groups()
        dist = int(dist)
        if not loc1 in map:
            map[loc1] = {}
        if not loc2 in map:
            map[loc2] = {}

        map[loc1][loc2] = dist
        map[loc2][loc1] = dist
    return map

def permute(xs, low=0):
    if low + 1 >= len(xs):
        yield xs
    else:
        for p in permute(xs, low + 1):
            yield p        
        for i in range(low + 1, len(xs)):        
            xs[low], xs[i] = xs[i], xs[low]
            for p in permute(xs, low + 1):
                yield p        
            xs[low], xs[i] = xs[i], xs[low]

def walk_list(list):
    l = len(list)
    for i in xrange(l-1):
        yield (list[i], list[i+1])

def walk_map(map):
    for route in permute(map.keys()):
        s = sum(map[loc1][loc2] for loc1, loc2 in walk_list(route))
        yield s

distances = dmap(sys.stdin)
print reduce(min,walk_map(distances))
print reduce(max,walk_map(distances))
