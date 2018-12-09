#!/usr/bin/env python

from collections import defaultdict
import re
import unittest

def generate_id(start=0):
    current = start
    while True:
        yield current
        current += 1

nodeid_generator = generate_id(0)

class Node(object):
    def __init__(self, parent=None, metadata=None):
        self._id = next(nodeid_generator)

        if metadata == None:
            self.metadata = []
        else:
            self.metadata = list(metadata)

        if parent == None:
            self._tree = {}
            self._parent = None
        else:
            self._tree = parent._tree
            self._parent = parent._id
            self._tree[self._parent]._children.append(self._id)

        self._children = []
        self._tree[self._id] = self


    @property
    def id(self):
        return self._id


    @property
    def parent(self):
        if self._parent != None:
            return self._tree[self._parent]
        return None


    @parent.setter
    def set_parent(self, parent):
        if isinstance(parent, Node):
            p_id = parent.id
        elif isinstance(parent, int):
            p_id = parent
        elif parent == None:
            self._tree[self._parent].children.remove(self._id)
            self._parent = None
            return

        if self._parent == p_id:
            return

        if self._parent:
            self._tree[self._parent].children.remove(self._id)

        self._parent = p_id
        self._tree[p_id]._children.append(self._id)


    @property
    def children(self):
        return [self._tree[i] for i in self._children]


    @children.setter
    def set_children(self, children):
        c_ids = set([i.id for i in children])
        for c_id in self._children:
            if c_id in c_ids:
                c_ids.remove(c_id)
            else:
                self._tree[c_id].parent = None

        for c_id in c_ids:
            self._tree[c_id].parent = self

    def __repr__(self):
        result = "Node(id={}, parent={}, children={}, metadata={})".format(
                self._id, self._parent, self._children, self.metadata)
        return result


class TestNode(unittest.TestCase):
    def setUp(self):
        self.root = Node()
        a = Node(parent=self.root)
        b = Node(parent=self.root)
        c = Node(parent=a)


    def testNodeRelations(self):
        root = [i for i in self.root._tree.values() if i.parent == None][0]
        a = [i for i in root.children if i.children][0]
        c1 = a.children.pop()
        c2 = a.children.pop()
        self.assertEqual(c1, c2)
