#!/usr/bin/env python

from collections import defaultdict
from operator import itemgetter
import unittest

class Test(unittest.TestCase):
    def setUp(self):
        self.power_tests = [  # x, y, grid serial, power
                (3, 5, 8, 4),
                (122, 79, 57, -5),
                (217, 196, 39, 0),
                (101, 153, 71, 4)]

        grid18 = [[-2, -4,  4,  4,  4],
                  [-4,  4,  4,  4, -5],
                  [ 4,  3,  3,  4, -4],
                  [ 1,  1,  2,  4, -3],
                  [-1,  0,  2, -5, -2]]

        grid42 = [[-3,  4,  2,  2,  2],
                  [-4,  4,  3,  3,  4],
                  [-5,  3,  3,  4, -4],
                  [ 4,  3,  3,  4, -3],
                  [ 3,  3,  3, -5, -1]]

        self.data = [  # grid serial, x and y of the best 3x3,
                       # bounding grid 5x5, best 3x3 sum
                (18, 33, 45, grid18, 29),
                (42, 21, 61, grid42, 30)]

        self.max_data = [  # grid serial, x and y of the best nxn,
                           # square size, best nxn sum
                (18, 90, 269, 16, 113),
                (42, 232, 251, 12, 119)]

    def test_power_calculation(self):
        for x, y, grid_id, power in self.power_tests:
            self.assertEqual(get_power(x, y, grid_id), power)


    def test_generate_small_grid(self):
        for serial, best_x, best_y, grid, _ in self.data:
            test_grid = generate_grid(serial, 5, 5, best_x - 1, best_y - 1)
            self.assertEqual(test_grid, grid)


    def test_search_small_grid(self):
        for serial, best_x, best_y, grid, best_sum in self.data:
            test_sum, test_x, test_y = best_3x3(grid, best_x - 1, best_y - 1)
            self.assertEqual(
                    (test_x, test_y, test_sum),
                    (best_x, best_y, best_sum))


    def test_search_full_grid(self):
        for serial, best_x, best_y, _, best_sum in self.data:
            grid = generate_grid(serial)
            test_sum, test_x, test_y = best_3x3(grid)
            self.assertEqual(
                    (test_x, test_y, test_sum),
                    (best_x, best_y, best_sum))


    def test_search_all_squares(self):
        for serial, best_x, best_y, best_size, best_sum in self.max_data:
            grid = generate_grid(serial)
            test_sum, test_x, test_y, test_size = best_square(grid)
            self.assertEqual(
                    (test_x, test_y, test_size, test_sum),
                    (best_x, best_y, best_size, best_sum))


def get_power(x, y, serial):
    rack_id = x + 10
    tmp = (rack_id * y + serial) * rack_id
    if tmp < 100:
        return -5
    return int(str(tmp)[-3]) - 5

def generate_grid(serial, xsize=300, ysize=300, x0=1, y0=1):
    return [[get_power(i, j, serial) for i in range(x0, x0 + xsize)]
            for j in range(y0, y0 + ysize)]


# Naїve implementation
def best_nxn(grid, x0=1, y0=1, size=3):
    results = defaultdict(int)

    for y in range(len(grid) - size + 1):
        for x in range(len(grid[0]) - size + 1):
            results[(x + x0, y + y0)] = sum(grid[y + j][x + i] \
                    for i in range(size) \
                    for j in range(size))
    best_cell, best_sum = max(results.items(), key=itemgetter(1))
    return (best_sum, *best_cell)

from functools import partial
best_3x3 = partial(best_nxn, size=3)

def best_square(grid, max_size=None, x0=1, y0=1):
    total_results = []  # list to hold (x, y, size, power) tuples
    if not max_size:
        max_size = len(grid)

    for square_size in range(1, max_size + 1):
        total_results.append((*best_nxn(grid, x0, y0, square_size), square_size))
        print("Size {}: {}".format(square_size, total_results[-1]))

    return max(total_results)



def task1(grid):
    print("Task 01")
    best_sum, best_x, best_y = best_3x3(grid)

    print("Best fuel cell coordinate {} gives total power {}".format(
        (best_x, best_y), best_sum))
    print("ANSWER: {},{}".format(best_x, best_y))


def task2(grid):
    print("Task 01")
    best_sum, best_x, best_y, best_size = best_square(grid)

    print("Best fuel cell coordinate {0} of size {1}x{1} gives total power {2}".format(
        (best_x, best_y), best_size, best_sum))
    print("ANSWER: {},{},{}".format(best_x, best_y, best_size))

def main(argv):
    serial = int(argv[1])
    grid = generate_grid(serial)
    task1(grid)
    task2(grid)


if __name__ == '__main__':
    import sys
    unittest.main(argv=sys.argv[:1], exit=False, verbosity=2)
    input()
    main(sys.argv)
