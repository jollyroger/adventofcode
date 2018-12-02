#!/usr/bin/env python

def look_and_say(s):
    i0 = s[0]
    n = 0
    res = ""
    for i in s:
        if i == i0:
            n += 1
        else:
            res += str(n) + i0
            i0 = i
            n = 1
    res += str(n) + i0
    return res

import sys
# base seed: 3113322113
key0 = sys.argv[1]
print "Initial key:\t{}".format(key0)

for _ in xrange(40):
    key = look_and_say(key0)
    key0=key

print len(key)

for _ in xrange(10):
    key = look_and_say(key0)
    key0=key

print len(key)
