#!/usr/bin/env python

from collections import defaultdict
import re
import unittest
from tree import Node

class TestTasks(unittest.TestCase):
    def setUp(self):
        self.input = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"
        self.tree = parse_data(parse_input(self.input))[1]
        self.node_sum = 138
        self.value = 66

    def test_solution1(self):
        self.assertEqual(count_metadata(self.tree), self.node_sum)

    def test_solution2(self):
        self.assertEqual(count_value(self.tree), self.value)


def parse_input(s):
    return [int(i) for i in re.findall(r'\d+', s)]


def get_input(filename='input'):
    return parse_input(open(filename, 'r').read())


def parse_data(lst, start=0, root=None):
    node = Node(parent=root)
    num_leafs = lst[start]
    num_metadata = lst[start+1]

    pos = start+2
    for i in range(num_leafs):
        pos, _ = parse_data(lst, pos, node)

    metadata = lst[pos:pos+num_metadata]
    node.metadata = metadata
    return (pos + num_metadata, node)


def count_metadata(root):
    return sum([sum(i.metadata) for i in root._tree.values()])

def count_value(node):
    if len(node.children) == 0:
        s = sum(node.metadata)
        return s
    else:
        result = 0
        for index in node.metadata:
            try:
                result += count_value(node.children[index-1])
            except IndexError:
                continue
        return result


def task1(_tree):
    print("Task 01")
    checksum = count_metadata(_tree)
    print("Metadata checksum: {}".format(checksum))


def task2(_tree):
    print("Task 02")
    checksum = count_value(_tree)
    print("Value checksum: {}".format(checksum))


def main(argv):
    data = get_input(argv[1])
    _, mytree = parse_data(data)
    task1(mytree)
    task2(mytree)


if __name__ == '__main__':
    import sys
    unittest.main(argv=sys.argv[:1], exit=False, verbosity=0)
    input()
    main(sys.argv)
