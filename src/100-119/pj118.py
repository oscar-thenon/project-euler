import time
start = time.time()

from sympy import isprime
from bisect import insort_left
from itertools import permutations

templates = set()

def make_templates(n=9,t=[]):
    """ Templates for creating sets """
    if n == 0:
        t.sort()
        templates.add(tuple(t))
    for i in range(1,n+1):
        make_templates(n-i,t+[i])

make_templates()
templates = list(templates)

def apply_template(t,n):
    """Apply template t to number n.
    If a non-prime occurs, return False
    If all are primes, return True and the made set"""
    b = 0
    s = []
    for i in t:
        a = b
        b += i
        p = int(n[a:b])
        if not isprime(p):
            return False,None
        insort_left(s,p)
    return True, tuple(s)

sets = set()
for x in permutations("123456789",9):
    n = ""
    for c in x:
        n += c
    for temp in templates:
        isallprime,k = apply_template(temp,n)
        if isallprime:
            sets.add(k)
print(len(sets))
print(round(time.time()-start,3))

    

    
