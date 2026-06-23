"""from sympy.ntheory import *

N = 10**6+1

primes = [i for i in sieve.primerange(2,N)]

pinv = dict()
for p in primes:
    pinv[p] = 1-1/p
    
phis = dict() # phis contain (1-1/p) for all p prime

def phi(n):
    if n in phis:
        return phis[n]
    elif n%2 == 1:
        ans = n
        for p in primefactors(n):
            ans *= pinv[p]
        ans = round(ans)
        phis[n] = ans
        return ans
    else:
        m = n//2
        if m%2 == 0:
            ans = 2*phi(m)
        else:
            ans = phi(m)
        phis[n] = ans
        return ans

def solve():
    ans = 0
    for d in range(2, N):
        ans += phi(d)
    print("Answer is", ans)

solve()"""

from sympy.ntheory import sieve

print(sum([d for d in sieve.totientrange(2,10**6+1)]))

""" 303963152391 """



