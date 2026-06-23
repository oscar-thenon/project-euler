from sympy.ntheory import primerange, sieve
import sys

T = 5000 # Target

N1 = 2 # Lower bound
N2 = 4 # Upper bound

primes = [p for p in primerange(N1,N2)]
lprimes = len(primes)

while 1:
    for n in range(N1,N2):
        w = 0 # Number of ways to write n as a sum
        def solve(n, i = 0, s = 0):
            global w
            if s == n:
                w += 1
                if w > T:
                    print("Answer is", n)
                    sys.exit()
                    
            for j in range(i, lprimes):
                p = primes[j]
                add = s+p
                if add > n:
                    return
                else:
                    solve(n,j, add)
        solve(n)
        
    # Solution was not found. Doubling bounds.
    N1 *= 2
    N2 *= 2
    paux = [p for p in primerange(N1,N2)]
    primes += paux
    lprimes += len(paux)