#!/usr/bin/env python

import sys
import re
from functools import partial, reduce

def printeval(x):
    print x
    return eval(x)

def memoize(f):
    class memodict(dict):
        def __missing__(self, key):
            ret = self[key] = f(key)
            return ret 
    return memodict().__getitem__

def build_wires(commands):
    wires = {}
    ops = {
        'NOT': '~',
        'AND': '&',
        'OR': '|',
        'LSHIFT': '<<',
        'RSHIFT': '>>',
    }

    for command in commands:
        expr, output = re.match(r'(.+) -> ([a-z]+)', command).groups()
        expr = reduce(lambda x, y: x.replace(y[0], y[1]), ops.items(), expr)
        expr = re.sub(r'([a-z]+)', 'wires["\\1"]()', expr)
        wires[output] = partial(memoize(printeval), expr)

    return wires

wires = build_wires(sys.stdin)
ans1 = wires['a']()
print(ans1)
