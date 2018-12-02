#!/usr/bin/env python

import sys
import re

def nice(s):
    ans1 = len(re.findall(r'[aeiou]', s)) >=3
    ans2 = bool(re.search(r'(.)\1', s))
    ans3 = not re.search(r'ab|cd|pq|xy', s)
    return ans1 and ans2 and ans3

def nice2(s):
    ans1 = bool(re.search(r'(..).*\1',s))
    ans2 = bool(re.search(r'(.).\1',s))
    return ans1 and ans2

def task1():
    sum = 0
    for line in sys.stdin:
        if nice(line):
            sum+=1
    print sum

def task2():
    sum = 0
    for line in sys.stdin:
        if nice2(line):
            sum+=1
    print sum

if __name__ == "__main__":
    locals()["task" + sys.argv[1]]()
