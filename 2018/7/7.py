#!/usr/bin/env python

from collections import defaultdict
import re
import unittest

class Test(unittest.TestCase):
    def setUp(self):
        self.steps = [("C", "A"),
                      ("C", "F"),
                      ("A", "B"),
                      ("A", "D"),
                      ("B", "E"),
                      ("D", "E"),
                      ("F", "E")]
        self.sequence1 = "CABDFE"
        self.sequence2 = "CABFDE"
        self.workers = 2
        self.duration = 0
        self.tta = 15


    def test1(self):
        self.assertEqual(get_order(self.steps), self.sequence1)


    def test_cost(self):
        self.assertEqual(cost("A"), 1)
        self.assertEqual(cost("Z"), 26)


    def test2(self):
        self.assertEqual(get_tta(self.steps, self.workers, self.duration),
                (self.sequence2, self.tta))


def get_order(steps):
    order_p = defaultdict(set)
    order_c = defaultdict(set)
    for p, c in steps:
        order_p[p].add(c)
        order_c[c].add(p)

    parents = set(order_p.keys())
    children = set(order_c.keys())
    parents.difference_update(children)
    if len(parents) > 1:
        print("wow, we've got multiple roots")

    sequence = []
    available = sorted(parents)
    while len(available) > 0:
        step = available.pop(0)
        sequence.append(step)
        children = order_p[step]
        for child in children:
            order_c[child].remove(step)
            if len(order_c[child]) == 0:
                available.append(child)
        available.sort()

    return "".join(sequence)


def cost(work):
    return ord(work) - 64


def get_tta(steps, workers=5, duration=60):
    order_p = defaultdict(set)
    order_c = defaultdict(set)
    for p, c in steps:
        order_p[p].add(c)
        order_c[c].add(p)

    parents = set(order_p.keys())
    children = set(order_c.keys())
    parents.difference_update(children)
    if len(parents) > 1:
        print("wow, we've got multiple roots")

    timer = 0 # wall clock indicating overall spent time
    tasks = [(0, None)] * workers # (duration left, Task ID)
    sequence = [] # tasks done
    workers_busy = 0 # Number of workers that still have jobs assigned
    available = sorted(parents)

    # Start here
    while len(available) > 0 or workers_busy:
        # Load workers
        for worker_id in range(workers):
            if tasks[worker_id][0] == 0:
                task = tasks[worker_id][1]
                if task:
                    print("Worker {0} completed task {1}".format(worker_id,
                        task))
                    sequence.append(task)
                    children = order_p[task]
                    for child in children:
                        order_c[child].remove(task)
                        if len(order_c[child]) == 0:
                            print("New work available: {}".format(child))
                            available.append(child)

                    tasks[worker_id] = (0, None)
                    available.sort()

        for worker_id in range(workers):
            if tasks[worker_id][0] == 0:
                task = tasks[worker_id][1]
                try:
                    work = available.pop(0)
                    tasks[worker_id] = (cost(work) + duration, work)
                    print("Worker {0} is assigned task {1}".format(worker_id,
                        work))
                except IndexError:
                    print("No more work currently available."
                          "Waiting for someone to finish")

        workers_busy = len([task for _, task in tasks if task])
        print("There are {} busy worker(s)..".format(workers_busy))
        # Wait until someone finishes work
        if workers_busy:
            wait_time = min([time for time, task in tasks if task])
            print("Waiting {} seconds..".format(wait_time))
            timer += wait_time
            tasks = [(max(t - wait_time, 0), task) for t, task in tasks]

    return ("".join(sequence), timer)


def get_input(filename='input'):
    steps = []
    expr = re.compile(r'Step ([A-Z]) must be finished before step ([A-Z]) can begin.')
    records = open(filename, 'r').read().strip().split("\n")

    for record in records:
        m = expr.match(record)
        if m:
            steps.append(m.groups())

    return steps


def task1(steps):
    print("Task 01")
    steps_order = get_order(steps)
    print("Correct steps order: {}".format(steps_order))

def task2(steps):
    print("Task 01")
    answer = get_tta(steps)
    print(answer)
    print("Correct steps order is {} and takes {} seconds".format(*answer))


def main(argv):
    data = get_input(argv[1])
    task1(data)
    task2(data)


if __name__ == '__main__':
    import sys
    unittest.main(argv=sys.argv[:1], exit=False, verbosity=0)
    input()
    main(sys.argv)
