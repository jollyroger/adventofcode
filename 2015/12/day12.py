#!/usr/bin/env python

import sys
import json

def task1(data):
    if isinstance(data, int):
        return data
    elif isinstance(data, list):
        return sum(task1(i) for i in data)
    elif isinstance(data, dict):
        return sum(task1(i) for i in data.values())
    else:
        return 0

def task2(data):
    if isinstance(data, int):
        return data
    elif isinstance(data, list):
        return sum(task2(i) for i in data)
    elif isinstance(data, dict):
        values = data.values()
        if "red" in values:
            return 0
        return sum(task2(i) for i in values)
    else:
        return 0

def main(jsonfile):
    data = json.loads(open(jsonfile, 'r').read())
    print task1(data)
    print task2(data)


if __name__ == "__main__":
    main(sys.argv[1])
