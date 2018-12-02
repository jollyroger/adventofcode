#!/usr/bin/env python
import sys

def move(pos, mv):
    x, y = pos
    if mv == "<":
        x -= 1
    elif mv == ">":
        x += 1
    elif mv == "^":
        y -= 1
    elif mv == "v":
        y += 1
    elif mv in [' ' ,'\t', '\n']:
        return (x, y)
    else:
        raise Exception("Incorrect move: {0}".format(mv))
    return (x, y)

def task1():
    pos = (0, 0)
    presents = dict()
    presents[pos] = 1

    for new_move in sys.stdin.read():
        newpos = move(pos, new_move)

        if newpos in presents:
            presents[newpos] += 1
        else:
            presents[newpos] = 1
        
        pos = newpos

    print len(presents)


from itertools import cycle

def task2():
    santas = 2
    pos_indexes = range(santas)
    positions = [(0,0) for _ in pos_indexes]

    presents = dict()
    for pos in positions:
        if pos in presents:
            presents[pos] += 1
        else:
            presents[pos] = 1

    person = cycle(pos_indexes)
    for new_move in sys.stdin.read():
        idx = person.next()
        pos = positions[idx]
        newpos = move(pos, new_move)
        positions[idx] = newpos

        if newpos in presents:
            presents[newpos] += 1
        else:
            presents[newpos] = 1

    print len(presents) 

if __name__ == "__main__":
    locals()["task" + sys.argv[1]]()
