from math import sqrt

Primes = set()

def setprimes(n):
    global Primes
    Primes.add(n)
    
def isprime(n):
    if n in Primes:
        return True
    else:
        if n < 2:
           return False
        elif n == 2:
            setprimes(n)
            return True
        else:
            for i in range(2,int(sqrt(n))+1):
                if n%i == 0:
                    return False
            setprimes(n)
            return True
        
def isallprime(w):
    l = len(w)
    for i in range(l):
        if (isprime(int(w[l-i-1:])) == False) or (isprime(int(w[:i+1])) == False):
            return False
    return True

def iscandidate(w):
    for (i,v) in enumerate(w):
        if (v == '0') or (v == '4') or (v == '6') or (v == '8'):  
            return False
        elif ((v == '2') or (v == '5')) and (i != 0):
            return False
    return True

c = 0
s = 0
n = 11

while (c != 11):
    w = str(n)
    if iscandidate(w) and isallprime(w):
        c += 1
        s += n
    n += 2
    
print "Answer is", s