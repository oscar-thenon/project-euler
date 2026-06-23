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

def rm(w,e): # Remove 'e' in the string w
    c = 0
    while w[c] != e:
        c += 1
    return w[:c] + w[c+1:]

MAX = 0

def maj(n): # Updates MAX
    global MAX
    if n > MAX:
         MAX = n

def permutations(perm, ant): # Generating all permutations
    if len(perm) == 1:
        if isprime(int(ant+perm)): # We check if the permutation is a prime
            maj(int(ant+perm))
    else:
        for k in perm:
            ant2 = ant
            ant2 += k
            perm2 = perm
            perm2 = rm(perm2,k)
            permutations(perm2, ant2)

permutations("7654321","")

if MAX == 0: # If there is no primes found THEN we check 4-digits pandigitals
    permutations("4321","")

print "Answer is", MAX