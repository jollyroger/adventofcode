#!/usr/bin/env python
import sys

def task1():
    floor = 0
    for char in sys.stdin.read():
        if char == "(":
            val = 1
        elif char == ")":
            val = -1
        elif char in [' ' ,'\t', '\n']:
            continue
        else:
            raise Exception("Incorrect input: {0}".format(char))
        floor += val

    print floor

def task2():
    floor = 0
    position = 0

    for char in sys.stdin.read():
        if char == "(":
            val = 1
        elif char == ")":
            val = -1
        elif char in [' ' ,'\t', '\n']:
            continue
        else:
            raise Exception("Incorrect input: {0}".format(char))
        position += 1
        floor += val

        if floor == -1:
            break

    print position



if __name__ == "__main__":
    locals()["task" + sys.argv[1]]()
