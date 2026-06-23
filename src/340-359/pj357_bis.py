from math import sqrt, ceil
import time

start_time = time.time()

def works(n):
    """ n natural > 2.
    returns true iff n respects given conditions and
    in case updates isToTest """
    for d in range(3, ceil(sqrt(n))):
        if (n%d == 0) and not ((d+n/d) in Primes):
            return False
    return True

answer = 1 # 1 works and won't be tested

N = 10**7+1

Primes = [2]

sieve = [i for i in range(3,N+1,2)]
L = len(sieve)
for (i,n) in enumerate(sieve):
    if (n != 0):
        Primes.append(n)
        while Primes[0] < 2*sqrt(n-1):
            Primes.pop(0)
            
        if ((n+3)/2) in Primes: # Divisor 2 of p-1 works
            if works(n-1):
                answer += n-1
        
        for j in range(i+n, L, n):
            sieve[j] = 0
        
print("Answer is", answer)

print("\n --- %s s ---" % (int(time.time() - start_time)+1))
