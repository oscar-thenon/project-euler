from math import sqrt
from math import pow

""" Primes """
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

""" Copy the list l """
def copy(l):
    new = []
    for k in l:
        new.append(k)
    return new

""" Calculates the next position of stars """
def nextstar(s,n):
    l = len(s)
    
    if s[-1] != n-1:
        s[-1] += 1
        return s
    else:
        i = -1
        while (i != -l) and (s[i] == n+i):
            i -= 1
        if (i == -l) and (s[0] == n-l):
            return []
        else:
            first = s[i]+1
            s[i] = first
            for j in range(i+1,0):
                s[j] = s[j-1]+1
            return s

"""Generates a tabular with all possible positions of i <= n stars."""
def setmegastar(n):
    megastar = []
    for i in range(1,n+1):
        superstar = []
        star = []
        for j in range(i):
            star.append(j)
        while star != []:
            superstar.append(copy(star))
            star = nextstar(star,n)
        megastar.append(superstar)
    return megastar

digits = "0123456789"

""" n is a number put in a list, s the list
of indexes of stars. Ex. : n = 8651 and
s = [0,2] tests the family *6*1.
family returns True iff the family generates F primes """
def family(n,s,nF):
    t = list(str(n))
    
    if s[0] == 0:
        notprime = 1
        digitsp = digits[1:]
    else:
        notprime = 0
        digitsp = digits
        
    for i in digitsp:
        for k in s:
            t[k] = i
            
        if not (int("".join(t)) in Primes):
            notprime += 1
            if notprime > nF:
                return False
    return notprime == nF

"""Test primes with stars """
def teststars(stars,ans,nF):
    for p in Primes:
        for S in stars:
            for s in S:
                if family(p,s,nF):
                    if p < ans[0]:
                        ans = [p,s]
    return ans

F = 8 # Number of primes in the generated families we want
nF = 10-F

ANS = pow(10,15)
n = 2 # Number of digits we are testing

""" Main """
while ANS == pow(10,15):
    
    Primes = set()
    for p in range(int(pow(10,n-1)+1), int(pow(10,n)), 2):
        nothing = isprime(p)
        
    stars = setmegastar(n-1)
    
    ans = teststars(stars, [ANS,[]], nF)
    
    if ans[0] < ANS:
        p = ans[0]
        s = ans[1]
        t = list(str(p))
        if s[0] == 0:
            digitsp = digits[1:]
        else:
            digitsp = digits

        for k in s:
            t[k] = digitsp[0]
                
        ANS = int("".join(t))
        print "Answer is", ANS
    else :
        print "Answer is not among", n, "digits."
        
    n += 1