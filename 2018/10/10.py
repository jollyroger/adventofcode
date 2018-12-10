#!/usr/bin/env python

from collections import defaultdict
import re
import unittest


class Test(unittest.TestCase):
    def setUp(self):
        self.points = ["position=< 9,  1> velocity=< 0,  2>",
                       "position=< 7,  0> velocity=<-1,  0>",
                       "position=< 3, -2> velocity=<-1,  1>",
                       "position=< 6, 10> velocity=<-2, -1>",
                       "position=< 2, -4> velocity=< 2,  2>",
                       "position=<-6, 10> velocity=< 2, -2>",
                       "position=< 1,  8> velocity=< 1, -1>",
                       "position=< 1,  7> velocity=< 1,  0>",
                       "position=<-3, 11> velocity=< 1, -2>",
                       "position=< 7,  6> velocity=<-1, -1>",
                       "position=<-2,  3> velocity=< 1,  0>",
                       "position=<-4,  3> velocity=< 2,  0>",
                       "position=<10, -3> velocity=<-1,  1>",
                       "position=< 5, 11> velocity=< 1, -2>",
                       "position=< 4,  7> velocity=< 0, -1>",
                       "position=< 8, -2> velocity=< 0,  1>",
                       "position=<15,  0> velocity=<-2,  0>",
                       "position=< 1,  6> velocity=< 1,  0>",
                       "position=< 8,  9> velocity=< 0, -1>",
                       "position=< 3,  3> velocity=<-1,  1>",
                       "position=< 0,  5> velocity=< 0, -1>",
                       "position=<-2,  2> velocity=< 2,  0>",
                       "position=< 5, -2> velocity=< 1,  2>",
                       "position=< 1,  4> velocity=< 2,  1>",
                       "position=<-2,  7> velocity=< 2, -2>",
                       "position=< 3,  6> velocity=<-1, -1>",
                       "position=< 5,  0> velocity=< 1,  0>",
                       "position=<-6,  0> velocity=< 2,  0>",
                       "position=< 5,  9> velocity=< 1, -2>",
                       "position=<14,  7> velocity=<-2,  0>",
                       "position=<-3,  6> velocity=< 2, -1>"]
        self.steps = 3
        self.sign = "\n".join(["............",
                               ".#...#..###.",
                               ".#...#...#..",
                               ".#...#...#..",
                               ".#####...#..",
                               ".#...#...#..",
                               ".#...#...#..",
                               ".#...#...#..",
                               ".#...#..###.",
                               "............"])

    def test(self):
        data = parse_input("\n".join(self.points))
        simulation = Simulation(data)
        solve(simulation)
        self.assertEqual(simulation.ts, 3)
        self.assertEqual(simulation.__str__(), self.sign)


def parse_input(s):
    steps = []
    expr = re.compile(r'-?\d+')
    records = s.strip().split("\n")

    for record in records:
        m = tuple(int(i) for i in expr.findall(record))
        if m:
            steps.append(m)

    return steps


def get_input(filename='input'):
    return parse_input(open(filename, 'r').read())


class Simulation(object):
    def __init__(self, start_state):
        self.state = list(start_state)
        self.ts = 0  # timestamp

    def step(self, steps=1):
        self.ts += steps
        for i, p in enumerate(self.state):
            x, y, dx, dy = p
            self.state[i] = (x + dx * steps, y + dy * steps, dx, dy)

    def region(self):
        min_x = max_x = self.state[0][0]
        min_y = max_y = self.state[0][1]
        for x, y, _, _ in self.state:
            min_x = min(x, min_x)
            max_x = max(x, max_x)
            min_y = min(y, min_y)
            max_y = max(y, max_y)
        return (min_x, min_y, max_x, max_y)

    def __str__(self):
        x1, y1, x2, y2 = self.region()
        points = {(x, y): set() for x, y, _, _ in self.state}
        result = ""

        for y in range(y1-1, y2+2):
            for x in range(x1-1, x2+2):
                char = "#" if (x, y) in points else "."
                result += char
            result += "\n"

        return result[:-1]


def solve(simulation):
    region = simulation.region()
    area = abs(region[2] - region[0]) * abs(region[3] - region[1])
    new_area = area
    while True:
        simulation.step()
        region = simulation.region()
        new_area = abs(region[2] - region[0]) * abs(region[3] - region[1])
        if new_area > area:
            simulation.step(-1)
            break
        area = new_area
    return


def main(argv):
    data = get_input(argv[1])
    simulation = Simulation(data)
    print("Task 01")
    solve(simulation)
    print(simulation)
    print("Task 02")
    print("Found minimum at {} seconds".format(simulation.ts))


if __name__ == '__main__':
    import sys
    unittest.main(argv=sys.argv[:1], exit=False, verbosity=0)
    raw_input()
    main(sys.argv)
