#!/usr/bin/env python

import sys


def task1():
    s = 0
    for line in sys.stdin:
        s +=len(line[:-1])
        s -=len(eval(line[:-1]))
    print s

def task2():
    s = 0
    for line in sys.stdin:
        s += 2 + line.count('"') + line.count('\\')
    print s

if __name__ == "__main__":
    locals()["task" + sys.argv[1]]()
