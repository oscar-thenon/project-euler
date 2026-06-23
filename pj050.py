from math import sqrt

# Caculation of primes
Primes = [2]
def setPrimes(n):
    global Primes
    Primes.append(n)
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
for p in range(3, 1000000, 2):
    nothing = isprime(p)
    
# somme(n) returns the sum of the c first primes
def somme(n):
    s = 0
    for i in range(n):
        s += Primes[i]
    return s

n = 546

ans = False # ans = False iff we do not have the answer

while not ans:
    s = somme(n)
    i = 0
    while s < 1000000:
        if s in Primes:
            print "Answer is", s
            ans = True
            break
        else:
            s -= Primes[i]
            s += Primes[i+n]
            i += 1
    n -= 1


    



