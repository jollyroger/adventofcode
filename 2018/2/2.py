#!/usr/bin/env python3

import os

def parse_input(_input):
        data = _input.replace('\n',' ').split()
        return data


def count_chars1(item):
    letters = {}
    for ch in item:
        if ch in letters:
            letters[ch] += 1
        else:
            letters[ch] = 1
    return letters


def count_2_and_3(item):
    letters = count_chars1(item)
    inv_map = {v: k for k, v in letters.items()}
    return (2 in inv_map, 3 in inv_map)


def solve1(ids):
    count2 = count3 = 0
    for i in ids:
        twos, threes = count_2_and_3(i)
        if twos:
            count2 += 1
        if threes:
            count3 += 1
    return count2 * count3


def compare_ids(id1, id2):
    return [x == y for x, y in zip(id1, id2)].count(False)


def common_chars(id1, id2):
    result = [x for x, y in zip(id1, id2) if x == y]
    return result

from itertools import combinations
def solve2(ids):
    for id1, id2 in combinations(ids,2):
        if compare_ids(id1, id2) == 1:
            return "".join(common_chars(id1, id2))

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


def task1(ids):
    print_header("Task 01")
    checksum = solve1(ids)
    print("The checksum: {}".format(checksum))

def task2(ids):
    print_header("Task 02")
    common = solve2(ids)
    print("Common characters between correct box IDs: {}".format(common))

import unittest
class TestTask1(unittest.TestCase):
    def test1(self):
        self.assertEqual(count_2_and_3("abcdef"), (False, False))

    def test2(self):
        self.assertEqual(count_2_and_3("bababc"), (True, True))

    def test3(self):
        self.assertEqual(count_2_and_3("abbcde"), (True, False))

    def test4(self):
        self.assertEqual(count_2_and_3("abcccd"), (False, True))

    def test5(self):
        self.assertEqual(count_2_and_3("aabcdd"), (True, False))

    def test6(self):
        self.assertEqual(count_2_and_3("abcdee"), (True, False))

    def test7(self):
        self.assertEqual(count_2_and_3("ababab"), (False, True))

class TestTask2(unittest.TestCase):
    def test1(self):
        data = ("abcde "
                "fghij "
                "klmno "
                "pqrst "
                "fguij "
                "axcye "
                "wvxyz")
        self.assertEqual(solve2(parse_input(data)), "fgij")

if __name__ == '__main__':
    import sys
    print_header("Advent of code 2018", "Day 02", "=")

    filename = sys.argv[1]
    with open(filename, 'r') as f:
        data = parse_input(f.read())

    print_header("Running unit tests:")
    unittest.main(argv=sys.argv[:1], exit=False, verbosity=0)

    task1(data)
    task2(data)

    print_footer("=")
