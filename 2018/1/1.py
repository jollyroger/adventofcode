#!/usr/bin/env python3

import os

def parse_input(_input):
        data = _input.replace('\n',' ').split()
        result = [int(i) for i in data]
        return result

# To solve the first part we just need to sum up the items in the list, hence
# no ancy function here
solve1 = sum

def solve2(changes):
    freq = 0
    seen = set([freq])
    while True:
        for change in changes:
            freq += change
            if freq not in seen:
                seen.add(freq)
            else:
                return freq


def print_header(title, subtitle=None, separator=None):
    if not separator:
        separator = '-'
    print(separator * (70 // len(separator)))
    print(title)
    if subtitle:
        print(subtitle)

def print_footer(separator=None):
    if not separator:
        separator = '-'
    print(separator * (70 // len(separator)))


def task1(changes):
    print_header("Task 01")
    final_freq = sum(changes)
    print("Final frequency: {}".format(final_freq))


def task2(changes):
    print_header("Task 02")
    final_freq = solve2(changes)
    print("Final frequency: {}".format(final_freq))

import unittest
class TestTask1(unittest.TestCase):
    def test1(self):
        self.assertEqual(solve1(parse_input("+1 -2 +3 +1")), 3)

    def test2(self):
        self.assertEqual(solve1(parse_input("+1 +1 +1")), 3)

    def test3(self):
        self.assertEqual(solve1(parse_input("+1 +1 -2")), 0)

    def test4(self):
        self.assertEqual(solve1(parse_input("-1 -2 -3")), -6)

class TestTask2(unittest.TestCase):
    def test1(self):
        self.assertEqual(solve2(parse_input("+1 -2 +3 +1")), 2)

    def test2(self):
        self.assertEqual(solve2(parse_input("+1 -1")), 0)

    def test3(self):
        self.assertEqual(solve2(parse_input("+3 +3 +4 -2 -4")), 10)

    def test4(self):
        self.assertEqual(solve2(parse_input("-6 +3 +8 +5 -6")), 5)

    def test5(self):
        self.assertEqual(solve2(parse_input("+7 +7 -2 -7 -4")), 14)

if __name__ == '__main__':
    import sys
    print_header("Advent of code 2018", "Day 01", "=")

    filename = sys.argv[1]
    with open(filename, 'r') as f:
        data = parse_input(f.read())

    print_header("Running unit tests:")
    unittest.main(argv=sys.argv[:1], exit=False, verbosity=0)

    task1(data)
    task2(data)

    print_footer("=")
