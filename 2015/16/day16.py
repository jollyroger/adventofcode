#!/usr/bin/env python

import re
import sys
from collections import defaultdict

grandma = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
}

def parse(lines):
    grandmas = defaultdict(dict)
    for line in lines:
        index, values = re.match(r'^Sue (\d+): (.*)$', line).groups()
        [grandmas[int(index)].__setitem__(a, int(b)) for a, b in (i.split(": ") for i in values.split(', '))]

    return grandmas

def compare(grannies):
    for index, granny in grannies.iteritems():
        if all(item in grandma.items() for item in granny.items()):
            return index

def compare2(grannies):
    eq = lambda x, y: cmp(x, y) == 0
    gt = lambda x, y: cmp(x, y) > 0
    lt = lambda x, y: cmp(x, y) < 0
    cmpd = {
        "children": eq,
        "cats": gt,
        "samoyeds": eq,
        "pomeranians": lt,
        "akitas": eq,
        "vizslas": eq,
        "goldfish": lt,
        "trees": gt,
        "cars": eq,
        "perfumes": eq
    }

    for index, granny in grannies.iteritems():
        if all(key in grandma and cmpd[key](value, grandma[key]) for key, value in granny.items()):
            return index

def main():
    grannies = parse(sys.stdin)
    print compare(grannies)
    print compare2(grannies)

if __name__ == "__main__":
    main()
