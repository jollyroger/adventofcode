#!/usr/bin/env python

import re
import sys
from itertools import product

def parse(lines):
    m = {}
    rexp = r'(\S+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)'
    for line in lines:
        name, cap, dur, fla, tex, cal = re.match(rexp, line).groups()
        m[name] = [int(cap), int(dur), int(fla), int(tex), int(cal)]
    return m

def combination(count, total):
    for values in product(range(total+1), repeat=count):
        if sum(values) == total:
            yield values

    
def main():
    ingredients = parse(sys.stdin)
    params_count = len(ingredients.values()[0])
    print ingredients

    def score(amounts):
        s = [0]*(params_count-1)
        for name, amount in amounts:
            for i in xrange(params_count-1):
                s[i] += amount * ingredients[name][i]

        s = [max(i, 0) for i in s]
        return reduce(lambda a,b: a*b, s)

    def score2(amounts):
        s = [0]*(params_count)
        for name, amount in amounts:
            for i in xrange(params_count):
                s[i] += amount * ingredients[name][i]

        s = [max(i, 0) for i in s]
        if s[-1] != 500:
            return 0
        return reduce(lambda a,b: a*b, s[:-1])

    ing_list = ingredients.keys()

    points = []
    points2 = []
    for c in combination(len(ing_list),100):
        s = score(zip(ing_list, c))
        s2 = score2(zip(ing_list, c))
        #print c, s, s2
        points.append(s)
        points2.append(s2)

    print max(points)
    print max(points2)

    

if __name__ == "__main__":
    main()
