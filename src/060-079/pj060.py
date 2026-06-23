import sys
from sympy import sieve
from sympy.ntheory import isprime

N = 10**4 # We'll check all primes under N
COUNTER = 5 # The number of primes we want

Primes = [i for i in sieve.primerange(3, N)]
Primestr = [str(p) for p in Primes]
last = len(Primes)

def arecoprimes(a,b):
    """ Are a and b coprimes ? """
    return isprime(int(a+b)) and isprime(int(b+a))

def solve(first, coprimes, lcoprimes):
    
    """ first : the index where we're starting
    checks : primes to check
    lchecks : len(checks) """
    
    for ip in range(first, last):
        p = Primestr[ip]
        
        iscoprime = True
        for c in coprimes:
            if not arecoprimes(p,c):
                iscoprime = False
                break
            
        if iscoprime: # p is coprime with all primes in coprimes
            coprimes.append(p)
            lcoprimes += 1
            
            if lcoprimes == COUNTER: # A solution is found !
                ans = sum([int(c) for c in coprimes])
                print("Answer is", ans)
                sys.exit() # Since a solution is found, we can stop the program
            
            solve(ip+1,coprimes,lcoprimes) # Let's tracking the next prime
            
            coprimes.pop(-1) # No next prime found : the current prime is not good
            lcoprimes -= 1
    return

solve(0,[],0)

print("No solution found. You have to increase N.")