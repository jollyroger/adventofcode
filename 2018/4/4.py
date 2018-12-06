#!/usr/bin/env python3

import os
import re
from datetime import datetime as dt, timedelta as td
from collections import defaultdict
from operator import itemgetter


def parse_record(rec):
    msg_state = {'shift':False, 'sleep':True, 'up':False}
    exp = r'^\[(?P<ts>[\d\s:-]+)\][^\d]+(?P<id>\d+)?.*(?P<msg>shift|up|sleep).*$'
    cexp = re.compile(exp)
    match = re.match(exp, rec)
    if not match:
        return
    ts = dt.strptime(match.group('ts'), "%Y-%m-%d %H:%M")
    guard_id = match.group('id')
    if guard_id:
        guard_id = int(guard_id)
    msg = msg_state[match.group('msg')]
    return (ts, guard_id, msg)


def parse_input(_input):
    records = _input.split("\n")
    data = []
    for record in records:
        rec = parse_record(record)
        if rec:
            data.append(rec)
    return sorted(data, key=itemgetter(0))


def guards_schedule(records):
    schedule = defaultdict(list)
    guard = None
    is_sleeping = False
    old_ts = None
    for ts, new_guard, sleep in records:
        if new_guard:
            if guard:
                schedule[guard].append((old_ts, ts, is_sleeping))
            guard = new_guard
            old_ts = ts
            is_sleeping = False
            continue

        schedule[guard].append((old_ts, ts, is_sleeping))
        old_ts = ts
        is_sleeping = sleep

    # Add the last time interval not closed by a loop
    finish_ts = old_ts.replace(hour=1, minute=0)
    schedule[guard].append((old_ts, finish_ts, is_sleeping))

    return schedule


def iterate_time(start_ts, end_ts, delta=td(minutes=1)):
    it = start_ts
    while it < end_ts:
        yield it
        it += delta


def strategy1(schedule):
    sleep_time = []
    for guard_id, deltas in schedule.items():
        sleep = [x[1] - td(minutes=1) - x[0] for x in deltas if x[2]]
        sleep_time.append((guard_id, sum(sleep, td(0))))

    sleepy_guard, _ = max(sleep_time, key=itemgetter(1))

    minutes = [0] * 60
    for deltas in schedule[sleepy_guard]:
        for ts in iterate_time(deltas[0], deltas[1]):
            if deltas[2]:
                minutes[ts.minute] += 1

    sleepy_minute, _ = max(enumerate(minutes), key=itemgetter(1))
    return (sleepy_guard, sleepy_minute)


def strategy2(schedule):
    minutes = defaultdict(lambda: defaultdict(int))
    for guard_id, deltas in schedule.items():
        for delta in deltas:
            if delta[2]:
                for ts in iterate_time(delta[0], delta[1]):
                    minutes[ts.minute][guard_id] += 1

    pre_result = [[minute]+ [*(max(m_data.items(), key=itemgetter(1)))] for
        minute, m_data in minutes.items()]
    result = max(pre_result, key=itemgetter(2))

    return (result[1], result[0])


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


def task1(schedule):
    print_header("Task 01")
    guard, minute = strategy1(schedule)
    print("Strategy 1 answer: {}".format(guard*minute))

def task2(schedule):
    print_header("Task 01")
    guard, minute = strategy2(schedule)
    print("Strategy 2 answer: {}".format(guard*minute))

import unittest

class TestCase1(unittest.TestCase):
    def setUp(self):
        self.input = ["[1518-11-01 00:00] Guard #10 begins shift",
                      "[1518-11-01 00:05] falls asleep          ",
                      "[1518-11-01 00:25] wakes up              ",
                      "[1518-11-01 00:30] falls asleep          ",
                      "[1518-11-01 00:55] wakes up              ",
                      "[1518-11-01 23:58] Guard #99 begins shift",
                      "[1518-11-02 00:40] falls asleep          ",
                      "[1518-11-02 00:50] wakes up              ",
                      "[1518-11-03 00:05] Guard #10 begins shift",
                      "[1518-11-03 00:24] falls asleep          ",
                      "[1518-11-03 00:29] wakes up              ",
                      "[1518-11-04 00:02] Guard #99 begins shift",
                      "[1518-11-04 00:36] falls asleep          ",
                      "[1518-11-04 00:46] wakes up              ",
                      "[1518-11-05 00:03] Guard #99 begins shift",
                      "[1518-11-05 00:45] falls asleep          ",
                      "[1518-11-05 00:55] wakes up              "]
        self.parsed_data = [(dt(1518,11, 1, 0, 0), 10, False),
                            (dt(1518,11, 1, 0, 5), None, True),
                            (dt(1518,11, 1, 0, 25), None, False),
                            (dt(1518,11, 1, 0, 30), None, True),
                            (dt(1518,11, 1, 0, 55), None, False),
                            (dt(1518,11, 1, 23, 58), 99, False),
                            (dt(1518,11, 2, 0, 40), None, True),
                            (dt(1518,11, 2, 0, 50), None, False),
                            (dt(1518,11, 3, 0, 5), 10, False),
                            (dt(1518,11, 3, 0, 24), None, True),
                            (dt(1518,11, 3, 0, 29), None, False),
                            (dt(1518,11, 4, 0, 2), 99, False),
                            (dt(1518,11, 4, 0, 36), None, True),
                            (dt(1518,11, 4, 0, 46), None, False),
                            (dt(1518,11, 5, 0, 3), 99, False),
                            (dt(1518,11, 5, 0, 45), None, True),
                            (dt(1518,11, 5, 0, 55), None, False)]
        self.guards_schedule = {
                10:[(dt(1518, 11, 1, 0, 0),   dt(1518, 11, 1, 0, 5),   False),
                    (dt(1518, 11, 1, 0, 5),   dt(1518, 11, 1, 0, 25),  True),
                    (dt(1518, 11, 1, 0, 25),  dt(1518, 11, 1, 0, 30),  False),
                    (dt(1518, 11, 1, 0, 30),  dt(1518, 11, 1, 0, 55),  True),
                    (dt(1518, 11, 1, 0, 55),  dt(1518, 11, 1, 23, 58), False),
                    (dt(1518, 11, 3, 0, 5),   dt(1518, 11, 3, 0, 24),  False),
                    (dt(1518, 11, 3, 0, 24),  dt(1518, 11, 3, 0, 29),  True),
                    (dt(1518, 11, 3, 0, 29),  dt(1518, 11, 4, 0, 2),   False)],
                99:[(dt(1518, 11, 1, 23, 58), dt(1518, 11, 2, 0, 40),  False),
                    (dt(1518, 11, 2, 0, 40),  dt(1518, 11, 2, 0, 50),  True),
                    (dt(1518, 11, 2, 0, 50),  dt(1518, 11, 3, 0, 5),   False),
                    (dt(1518, 11, 4, 0, 2),   dt(1518, 11, 4, 0, 36),  False),
                    (dt(1518, 11, 4, 0, 36),  dt(1518, 11, 4, 0, 46),  True),
                    (dt(1518, 11, 4, 0, 46),  dt(1518, 11, 5, 0, 3),   False),
                    (dt(1518, 11, 5, 0, 3),   dt(1518, 11, 5, 0, 45),  False),
                    (dt(1518, 11, 5, 0, 45),  dt(1518, 11, 5, 0, 55),  True),
                    (dt(1518, 11, 5, 0, 55),  dt(1518, 11, 5, 1, 0),   False)]}

        self.sleepy_guard1 = 10
        self.sleepy_minute1 = 24

        self.sleepy_guard2 = 99
        self.sleepy_minute2 = 45

    def test_parse_input(self):
        self.assertEqual(parse_input("\n".join(self.input)), self.parsed_data)

    def test_process_deltas(self):
        self.assertEqual(guards_schedule(self.parsed_data), self.guards_schedule)

    def test_solution1(self):
        guard, minute = strategy1(self.guards_schedule)
        self.assertEqual(guard, self.sleepy_guard1)
        self.assertEqual(minute, self.sleepy_minute1)

    def test_solution2(self):
        guard, minute = strategy2(self.guards_schedule)
        self.assertEqual(guard, self.sleepy_guard2)
        self.assertEqual(minute, self.sleepy_minute2)

if __name__ == '__main__':
    import sys
    print_header("Advent of code 2018", "Day 04", "=")

    print_header("Running unit tests:")
    unittest.main(argv=sys.argv[:1], exit=False, verbosity=0)

    filename = sys.argv[1]
    with open(filename, 'r') as f:
        data = parse_input(f.read())
        schedule = guards_schedule(data)
    task1(schedule)
    task2(schedule)

    print_footer("=")
