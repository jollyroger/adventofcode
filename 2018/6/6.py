#!/usr/bin/env python3

import re
from math import ceil
from operator import itemgetter
from collections import defaultdict

def get_input(filename='input'):
    data = open(filename, 'r').read().strip().split("\n")
    points = []
    for record in data:
        points.append([int(i) for i in re.findall(r'-?\d+', record)])
    return points

def field_size(points):
    x_list, y_list = zip(*points)
    return (min(x_list), min(y_list), max(x_list), max(y_list))

def distance(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)

def largest_area(points):
    id_points = {pos: point for pos, point in enumerate(points)}
    xmin, ymin, xmax, ymax = field_size(points)
    field = [[None for i in range(ymin, ymax+1)] for j in range(xmin, xmax+1)]

    # Collect edge points with unlimited number of closest  points
    edge_points = set()

    # Calculate distances for each point on a field, count distance for every
    # given point and choose the nearest one to put into distances list.
    distances = defaultdict(int)
    for x in range(xmin, xmax+1):
        for y in range(ymin, ymax+1):
            lst = sorted((distance(*p, x, y), p_id) for p_id, p in id_points.items())
            if lst[0][0] != lst[1][0]:
                field[x-xmin][y-ymin] = lst[0]
                distances[lst[0][1]] += 1
                if x == xmin or x == xmax or y == ymin or y == ymax:
                    edge_points.add(lst[0][1])

    return max([(p, d) for p, d in distances.items() \
            if p not in edge_points], key=itemgetter(1))

def part2(points, total_distance=10000):
    id_points = {pos: point for pos, point in enumerate(points)}
    num_points = len(id_points)
    sufficient_distance = ceil(total_distance / num_points)
    center = [sum(i) // num_points for i in zip(*points)] * 2
    xmin, ymin, xmax, ymax = [i + j for i, j in zip(center,
        (-sufficient_distance, -sufficient_distance,
         sufficient_distance, sufficient_distance))]

    field = [[None for i in range(ymin, ymax+1)] for j in range(xmin, xmax+1)]

    size_region = 0
    for x in range(xmin, xmax+1):
        for y in range(ymin, ymax+1):
            size_region += int(sum(distance(*p, x, y) for p in
                id_points.values()) < total_distance)

    return size_region

import unittest

class TestCase1(unittest.TestCase):
    def setUp(self):
        self.points = [(1, 1),
                       (1, 6),
                       (8, 3),
                       (3, 4),
                       (5, 5),
                       (8, 9)]
        self.largest_area = (4, 17)
        self.total_distance = 32
        self.size_region = 16

    def test1(self):
        self.assertEqual(largest_area(self.points), self.largest_area)

    def test2(self):
        self.assertEqual(part2(self.points, self.total_distance),
            self.size_region)

def task1(points):
    print("Task 01")
    point_id, area = largest_area(points)
    print("Point {0} has the largest area: {1}".format(point_id, area))

def task2(points):
    print("Task 02")
    size = part2(points, 10000)
    print("Area size is {}".format(size))

def main(argv):
    data = get_input(argv[1])
    task1(data)
    task2(data)


if __name__ == '__main__':
    import sys
    unittest.main(argv=sys.argv[:1], exit=False, verbosity=0)
    main(sys.argv)
