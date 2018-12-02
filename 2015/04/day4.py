#!/usr/bin/env pypy

import md5

x = "bgvyzdsv"
i=0
while True:
    m = md5.new()
    m.update(x + str(i))
    if m.hexdigest().startswith("000000"):
        break
    i += 1
print i
