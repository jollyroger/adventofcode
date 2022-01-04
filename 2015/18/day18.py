#!/usr/bin/env python2

import sys
from functools import partial

def parse(lines):
    result = []

    for line in lines:
        result.append([1 if c == '#' else 0 for c in line.strip()])
    return result

def new_state(state, validation_func=None):
    len_x = len(state[0])
    len_y = len(state)
    result = [[0]*len_x for i in xrange(len_y)]

    def new_value(x, y):
        old_value = state[y][x]
        sub_ = [line[max(x-1, 0):min(x+1+1, len_x)] for line in
                state[max(y-1, 0):min(y+1+1, len_y)]]

        #print "Sub matrix for (%s, %s):" % (x, y)
        #print_state(sub_)

        s = sum([sum(line) for line in sub_]) - old_value
        if s == 3:
            res = 1
        elif s == 2 and old_value == 1:
            res = 1
        else:
            res = 0

        #print "Sub sum: %s, new value is %s" % (s, res)
        return res

    if validation_func:
        _new_value = new_value
        def new_value(x,y):
            value = validation_func(x,y)
            if value:
                #print "Stuck light %s, %s" % (x, y)
                return value
            else:
                return _new_value(x, y)

    for y in xrange(len_y):
        for x in xrange(len_x):
            result[y][x] = new_value(x, y)

    return result


def print_state(state):
    result = "\n".join(["".join(['#' if c == 1 else '.' for c in line]) for line in
            state])
    print(result)

def stuck_lights(x, y, len_x, len_y):
    if x in [0, len_x - 1] and y in [0, len_y - 1]:
        return 1
    else:
        pass

def main():
    init = parse(sys.stdin)
    len_x = len(init[0])
    len_y = len(init)
    old = init
    print "Initial state:"
    print_state(init)

    for i in xrange(4):
        new = new_state(old)
        old = new
        print "Iteration %s complete" % (i+1)
        print_state(new)

    s1 = sum([sum(line) for line in old])
    print "Part 1: %s" % s1

    # adding stuck lights
    init[0][0] = 1
    init[0][len_x - 1] = 1
    init[len_y - 1][0] = 1
    init[len_y - 1][len_x - 1] = 1

    print "Initial state:"
    print_state(init)

    old = init

    validation = partial(stuck_lights, len_x=len_x, len_y=len_y)

    for i in xrange(100):
        new = new_state(old, validation_func=validation)
        old = new
        print "Iteration %s complete" % (i+1)
        print_state(new)

    s2 = sum([sum(line) for line in old])
    print "Part 2: %s" % s2



if __name__ == "__main__":
    main()
