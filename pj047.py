from math import sqrt

# Primes
Primes = {3}
def setPrimes(n):
    global Primes
    Primes.add(n)
def isprime(n):
    if n < 2:
       return False
    elif n == 2:
        setPrimes(n)
        return True
    else:
        for i in range(2,int(sqrt(n))+1):
            if n%i == 0:
                return False
        setPrimes(n)
        return True

""" The following function adds the entry n in the dictionary dico.
dico[n] = 1 if n has F prime factors
dico[n] = 0 if n has F-1 prime factors
dico[n] = -1 else"""
def Fdiv(dico, n): 
    f = 0 # Number of prime factors
    
    # Testing with already calculated primes
    for p in Primes:
        if n%p == 0:
            f += 1
        if f > F:
            dico[n] = -1
            return dico
    
    # Adding necessary primes
    p = max(Primes)
    while p <= n/3:
        p += 2
        if isprime(p) and (n%p == 0):
            f += 1
        if f > F:
            dico[n] = -1
            return dico
    
    if f == F:
        dico[n] = 1
    elif f == F-1:
        dico[n] = 0
    else:
        dico[n] = -1
        
    return dico

F = 4 # Number of prime factors you want
cons = 0 # Consecutive numbers who have F prime factors
n = 5 # The number we are testing

dico = {1:-1, 2:-1, 3:-1, 4:-1} # First 4 entries
C = [0,0,0,0] # First 4 entries

while cons != F:
    if C[-F] == 1: # We just want to count the F last numbers
        cons -= 1
    
    if n%2 != 0: # If n is odd, then we look at dictonary
        dico = Fdiv(dico, n)
    
        if dico[n] == 1: # n has F prime factors
            C.append(1)
            cons += 1
        else:
            C.append(0)
    
    else: # If n is even
        m = n
        while (m%2 == 0):
            m /= 2
        
        divm = dico[m]
        
        if divm == 0:
            C.append(1)
            cons += 1
        else:
            C.append(0)
    
    n += 1
    
print "Answer is", n-F