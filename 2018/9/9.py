#!/usr/bin/env python

import re
import unittest
from collections import deque

class Test(unittest.TestCase):
    def setUp(self):
        self.games = [(9, 25, 32),
                      (10, 1618, 8317),
                      (13, 7999, 146373),
                      (17, 1104, 2764),
                      (21, 6111, 54718),
                      (30, 5807, 37305)]


    def test_part1(self):
        for players, last_marble, score in self.games:
            self.assertEqual(get_highscore(players, last_marble), score)


def parse_input(s):
    return [int(i) for i in re.findall(r'\d+', s)]


def get_input(filename='input'):
    return parse_input(open(filename, 'r').read())


def get_highscore(player_count, last_marble):
    scores = [0] * player_count
    circle = deque([0])

    for marble in range(1,last_marble+1):
        if marble % 23 == 0:
            circle.rotate(7)
            scores[marble % player_count] += marble + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)
    return(max(scores))


def task1(data):
    print("Task 01")
    score = get_highscore(*data)
    print("Winning elf score: {}".format(score))


def task2(data):
    print("Task 02")
    players, last_marble = data
    last_marble *= 100
    score = get_highscore(players, last_marble)
    print("Winning elf score: {}".format(score))


def main(argv):
    data = get_input(argv[1])
    task1(data)
    task2(data)


if __name__ == '__main__':
    import sys
    unittest.main(argv=sys.argv[:1], exit=False, verbosity=0)
    input()
    main(sys.argv)
