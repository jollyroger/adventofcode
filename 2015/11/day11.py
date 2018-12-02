#!/usr/bin/env python
from functools import partial

def take_n_and_shift(n, s):
    for i in xrange(len(s)-n+1):
        yield s[i:i+n]

take3 = partial(take_n_and_shift, 3)
take2 = partial(take_n_and_shift, 2)

def three_in_a_row(s):
    rs = []

    for s1 in take3(s):
        rs1 = []
        for x, y in take2(s1):
            rs1.append(ord(y) - ord(x) == 1)
        rs.append(reduce(lambda x,y: x and y, rs1))

    return reduce(lambda x, y: x or y, rs)

def count_groups(s):
    c = {}
    for a,b in take2(s):
        if a == b:
            c[a] = 1
    return len(c)

def checkpass(s):
    if s.lower() != s:
        return False
    if len(s) != 8:
        return False
    if reduce(lambda x, y: x or y, [(i in s) for i in ['i','o','l']]):
        return False
    if not three_in_a_row(s):
        return False
    if count_groups(s) < 2 :
        return False

    return True

def chplus(c):
    return chr(ord(c)+1)

def nextpass(s):
    sx = [i for i in s]
    while True:
        for i in xrange(len(s)-1,0,-1):
            sx[i] = chplus(sx[i])
            if sx[i] > 'z':
                sx[i] = 'a'
                continue
            break
        newpass = "".join(sx)
        if checkpass(newpass):
            return newpass
            

assert(checkpass("hijklmmn")==False)
assert(checkpass("abbceffg")==False)
assert(checkpass("abbcegjk")==False)
assert(checkpass("abcdffaa")==True)
assert(nextpass("abcdefgh") == "abcdffaa")
assert(checkpass("ghjaabcc")==True)
assert(nextpass("ghijklmn") == "ghjaabcc")

if __name__ == '__main__':
    import sys
    pass1 = nextpass(sys.argv[1])
    print pass1
    pass2 = nextpass(pass1)
    print pass2
