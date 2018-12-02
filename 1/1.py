#!/usr/bin/env python3

import os

def parse_input(filename):
    result = []
    with open(filename, 'r') as f:
        for line in f:
            change = int(line)
            result.append(change)

    return result

def task1(changes):
    print("-" * 80)
    print("Part 1")
    final_freq = sum(changes)
    print("Final frequency: {}".format(final_freq))

def task2(changes):
    def solve():
        freq = 0
        seen = set([freq])
        while True:
            for change in changes:
                freq += change
                if freq not in seen:
                    seen.add(freq)
                else:
                    return freq

    print("-" * 80)
    print("Part 2")
    final_freq = solve()
    print("Final frequency: {}".format(final_freq))


if __name__ == '__main__':
    print("=" * 80)
    print("Advent of Code 2018")
    print("Task 1")
    print("=" * 80)
    import sys
    filename = sys.argv[1]
    data = parse_input(filename)
    task1(data)
    task2(data)
    print("=" * 80)
