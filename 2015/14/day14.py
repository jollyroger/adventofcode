#!/usr/bin/env python

import re
import sys

class Reindeer:
    def __init__(self, name, speed, fly_time, rest_time):
        self.name = name
        self.speed = speed
        self.fly_time = fly_time
        self.rest_time = rest_time

    def fly(self, time):
        intervals = time / (self.fly_time + self.rest_time)
        time_left = time % (self.fly_time + self.rest_time)
        d1 = self.fly_time * intervals * self.speed
        d2 = min(self.fly_time, time_left) * self.speed
        return d1+d2

    def __repr__(self):
        return "{3}({0}, {1}, {2})".format(self.speed,
                self.fly_time, self.rest_time, self.name)

def parse(lines):
    m = []
    rexp = r'(\S+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.'

    for line in lines:
        name, speed, fly_time, rest_time = re.match(rexp,line).groups()
        m.append(Reindeer(name, int(speed), int(fly_time), int(rest_time)))

    return m

def race(deers, time):
    scores = [0 for i in xrange(len(deers))]

    for t in xrange(time):
        d = [x.fly(t+1) for x in deers]
        m = reduce(max,d)
        for i in xrange(len(deers)):
            if d[i] == m:
                scores[i] += 1
    return scores

def main():
    d = parse(sys.stdin)
    time = 2503
    print reduce(max, [x.fly(time) for x in d])
    print reduce(max, race(d, time))

if __name__ == "__main__":
    main()
