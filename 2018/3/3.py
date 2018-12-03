#!/usr/bin/env python3

import os
import re

def parse_input(_input):
    records = _input.split("\n")
    data = []
    for record in records:
        rec = parse_record(record)
        if rec:
            data.append(rec)
    return data


def parse_record(rec):
    fmt = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')
    match = fmt.match(rec)
    if match:
        return tuple([int(i) for i in match.groups()])
    else:
        return None


def get_geometry(record_list):
    min_x = min_y = float('inf')
    max_x = max_y = float('-inf')

    for i, x, y, w, h in record_list:
        min_x = min(min_x, x)
        min_y = min(min_y, y)
        max_x = max(max_x, x+w)
        max_y = max(max_y, y+h)

    return ((min_x, max_x), (min_y, max_y))


def get_fabric_and_overlaps(record_list):
    x, y = get_geometry(record_list)
    fabric = [[set() for i in range(x[1])] for i in range(y[1])]
    overlaps = {}

    for i, x1, y1, w, h in record_list:
        overlaps[i] = set()
        x2 = x1 + w
        y2 = y1 + h
        for x in range(x1, x2):
            for y in range(y1, y2):
                if fabric[y][x]:
                    for number in fabric[y][x]:
                        overlaps[number].add(i)
                        overlaps[i].add(number)
                fabric[y][x].add(i)

    return (fabric, overlaps)

def count_conflicts(fabric):
    return sum([[len(ix) > 1 for ix in line].count(True) for line in fabric])

def find_intact_id(overlaps):
    return [k for k in overlaps if len(overlaps[k]) == 0][0]


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


def task1(fabric):
    print_header("Task 01")
    conflicts = count_conflicts(fabric)
    print("The number of conflicting square inches: {}".format(conflicts))

def task2(overlaps):
    print_header("Task 02")
    conflicts = find_intact_id(overlaps)
    print("The id that does not overlap: {}".format(conflicts))

import unittest
class TestTask1(unittest.TestCase):
    def setUp(self):
        self.data = ["#1 @ 1,3: 4x4",
                     "#2 @ 3,1: 4x4",
                     "#3 @ 5,5: 2x2",
                     "#4 @ 1,1: 3x3"]
        self.out = [(1, 1, 3, 4, 4),
                    (2, 3, 1, 4, 4),
                    (3, 5, 5, 2, 2),
                    (4, 1, 1, 3, 3)]
        self.geometry = ((1,7), (1,7))
        fabric_sets = [[[], [],     [],     [],        [],     [],  []],
                       [[], [4],    [4],    [4, 2],    [2],    [2], [2]],
                       [[], [4],    [4],    [4, 2],    [2],    [2], [2]],
                       [[], [4, 1], [4, 1], [4, 1, 2], [1, 2], [2], [2]],
                       [[], [1],    [1],    [1, 2],    [1, 2], [2], [2]],
                       [[], [1],    [1],    [1],       [1],    [3], [3]],
                       [[], [1],    [1],    [1],       [1],    [3], [3]]]
        self.fabric = [[set(i) for i in line] for line in fabric_sets]
        self.conflicts = 8
        self.non_overlaping_id = 3

    def test1(self):
        self.assertEqual(parse_record(self.data[0]), self.out[0])

    def test2(self):
        self.assertEqual(parse_input("\n".join(self.data)), self.out)

    def test3(self):
        self.assertEqual(get_geometry(self.out), self.geometry)

    def test4(self):
        fabric, _ = get_fabric_and_overlaps(self.out)
        self.assertEqual(fabric, self.fabric)

    def test5(self):
        self.assertEqual(count_conflicts(self.fabric), self.conflicts)

    def test6(self):
        _, overlaps = get_fabric_and_overlaps(self.out)
        self.assertEqual(find_intact_id(overlaps), self.non_overlaping_id)

if __name__ == '__main__':
    import sys
    print_header("Advent of code 2018", "Day 02", "=")

    print_header("Running unit tests:")
    unittest.main(argv=sys.argv[:1], exit=False, verbosity=0)

    filename = sys.argv[1]
    with open(filename, 'r') as f:
        fabric, overlaps = get_fabric_and_overlaps(parse_input(f.read()))
    task1(fabric)
    task2(overlaps)

    print_footer("=")
