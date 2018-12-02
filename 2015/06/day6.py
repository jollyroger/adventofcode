#!/usr/bin/env python

import re

def task1():
    m = [[False for i in xrange(1000)] for j in xrange(1000)]
    actions = {
        "turn on": lambda x: True,
        "turn off": lambda x: False,
        "toggle": lambda x: not x
    }

    for line in sys.stdin:
        op, x1, y1, x2, y2 = \
            re.match(r'(.+) ([0-9]+),([0-9]+) through ([0-9]+),([0-9]+)', line).groups()

        for i in xrange(int(x1), int(x2)+1):
            for j in xrange(int(y1), int(y2)+1):
                m[i][j] = actions[op](m[i][j])

    print sum([sum(x) for x in m])

def task2():
    m = [[0 for i in xrange(1000)] for j in xrange(1000)]
    actions = {
        "turn on": lambda x: x + 1,
        "turn off": lambda x: max (0, x - 1),
        "toggle": lambda x: x+2
    }

    for line in sys.stdin:
        op, x1, y1, x2, y2 = \
            re.match(r'(.+) ([0-9]+),([0-9]+) through ([0-9]+),([0-9]+)', line).groups()

        for i in xrange(int(x1), int(x2)+1):
            for j in xrange(int(y1), int(y2)+1):
                m[i][j] = actions[op](m[i][j])

    print sum([sum(x) for x in m])

import sys
if __name__ == "__main__":
    locals()["task" + sys.argv[1]]()
