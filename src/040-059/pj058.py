from math import sqrt

def isprime(n):
    if n < 2:
       return False
    elif n == 2:
        return True
    else:
        for i in range(2,int(sqrt(n))+1):
            if n%i == 0:
                return False
        return True

n = 1 # current number in the diagonal

N = 1 # Numbers in the diagonals 
P = 0 # Primes in the diagonals
r = 1 # ratio

k = 1 # Coefficient
L = 1 # Length of the square

while r >= 0.1:
    L += 2
    for i in range(3):
        n += 2*k
        P += isprime(n)
        
    n += 2*k
    N += 4
    r = P/(N+0.0)
    k += 1

print L