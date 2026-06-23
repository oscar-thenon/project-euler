from math import *
from fractions import Fraction

N = 1000000


""" Calculating primes using a sieve """
sieve = [i for i in range(2,N)]
primes = []
for (i,n) in enumerate(sieve):
    if (n != 0):
        primes.append(n)
        for j in range(i+n, N-2, n):
            sieve[j] = 0
Primes = set(primes) # I also put primes in a set for searching, which is much faster using sets.
        

Phi = {1:1} # Convention

def phi(n):
    if n in Phi:
        return Phi[n]
    else:
        if (n%2 == 0):
            np = n//2
            if np%2 == 0:
                answer = 2*phi(np)
                Phi[n] = answer
                return answer
            else:
                answer = phi(np)
                Phi[n] = answer
                return answer
        else:
            if n in Primes:
                Phi[n] = n-1
                return n-1
            else:
                
                answer = n
                
                lim = n//3
                i = 0
                p = 2
                while (p <= lim):
                    if n%p == 0:
                        
                        answer *= (1-Fraction(1,p))
                    i += 1
                    p = primes[i]
                answer = answer.numerator
                Phi[n] = answer
                return answer
                    
rmax = 0
answer = 0

for n in range(30, N, 30):
    r = n/phi(n)
    if r > rmax:
        rmax = r
        answer = n

print("Answer is", answer)