#!/usr.bin/python
# coding UTF-8
"""try to make the recursional function
"""

def facto(n, a=1):
    if n == 0:
        return a
    return facto(n-1, n*a)

print(facto(4))

