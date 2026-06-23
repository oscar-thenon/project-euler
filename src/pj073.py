from sympy.ntheory import primefactors as pf
from math import ceil

def numberd(d):
    """ Return number of fractions 1/3 < n/d < 1/2 """
    a = int(d/3)+1
    b = ceil(d/2)-1
    l = b-a+1
    f = pf(d)
    notcoprimes = set()
    for p in f:
        t = p*ceil(a/p)
        
        while t <= b:
            notcoprimes.add(t)
            t += p
    return l-len(notcoprimes)
    
D = 12000

def solve():
    ans = 0
    for d in range(2,D+1):
        ans += numberd(d)
    print("Answer is", ans)

solve()