#!/usr/bin/env python3

from operator import itemgetter
from string import ascii_lowercase

def get_input(filename='input'):
    data = open(filename, 'r').read()
    return list(data.strip())

def simplify_polymer(polymer, ignore=None):
    new_polymer = []
    if ignore:
        ignore = ignore.lower()

    for new_ch in polymer:
        if new_ch.lower() == ignore:
            continue
        try:
            ch = new_polymer.pop()
            if abs(ord(ch) - ord(new_ch)) == 32:
                continue
            new_polymer.append(ch)
            new_polymer.append(new_ch)
        except IndexError:
            new_polymer.append(new_ch)
    return new_polymer


def task1(data):
    print("Task 01")
    result = len(simplify_polymer(data))
    print("Size of the simplified polymer is: {}".format(result))

def task2(data):
    print("Task 01")
    result = min([(unit, len(simplify_polymer(data, ignore=unit))) for unit in
        ascii_lowercase], key=itemgetter(1))
    print("Best size of the simplified polymer is: {}".format(result))


import unittest

class TestCase1(unittest.TestCase):
    def setUp(self):
        self.polymer = 'dabAcCaCBAcCcaDA'
        self.simplified_polymer = list('dabCBAcaDA')
        self.simplified_no_a = list('dbCBcD')
        self.simplified_no_b = list('daCAcaDA')
        self.simplified_no_c = list('daDA')
        self.simplified_no_d = list('abCBAc')

    def test_simplify1(self):
        self.assertEqual(simplify_polymer(self.polymer),
                self.simplified_polymer)

    def test_simplify2(self):
        self.assertEqual(simplify_polymer(self.polymer, 'a'),
                self.simplified_no_a)
        self.assertEqual(simplify_polymer(self.polymer, 'b'),
                self.simplified_no_b)
        self.assertEqual(simplify_polymer(self.polymer, 'c'),
                self.simplified_no_c)
        self.assertEqual(simplify_polymer(self.polymer, 'd'),
                self.simplified_no_d)


def main(argv):
    data = get_input(argv[1])
    task1(data)
    task2(data)


if __name__ == '__main__':
    import sys
    unittest.main(argv=sys.argv[:1], exit=False, verbosity=0)
    main(sys.argv)
