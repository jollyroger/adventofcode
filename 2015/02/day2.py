#!/usr/bin/env python

import sys

def task1():
    sum = 0
    for geometry in sys.stdin:
        dims = [int(i) for i in geometry[:-1].split("x")]
        dims.sort()
        l, w, h = dims
        sum += 3*l*w + 2*w*h + 2*l*h

    print sum

def task2():
    length = 0
    for geometry in sys.stdin:
        dims = [int(i) for i in geometry[:-1].split("x")]
        dims.sort()
        l, w, h = dims
        length += 2*l + 2*w + l*w*h

    print length

if __name__ == "__main__":
    locals()["task" + sys.argv[1]]()
