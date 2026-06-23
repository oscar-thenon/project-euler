import numpy as np
from sympy.ntheory import *

Primes = np.array(list(sieve.primerange(2, 20001)))
LP = len(Primes)



def evalz(f):
    """ Calculates f which is a decomposition """
    ans = 1
    for (i,p) in enumerate(Primes):
        ans *= pow(int(p),int(f[i]))
    return ans

def profacz(f1,f2):
    """ Calculates f1*f2 """
    return f1+f2
def divfacz(f1,f2):
    """ Calculates f1/f2. We assume f2 divides f1 """
    return f1-f2
def powerfacz(f,p):
    """ Powering f by p """
    return f*p

def cumulsum(f):
    """ fz : nd-array, do the cumulative sum of arrays """
    fz = np.copy(f)
    for i in range(1,len(fz)):
        fz[i] += fz[i-1]
    return fz

def nz(n):
    """ Decompose n in prime factors, n > 0 """
    f = np.zeros(LP)
    if n > 1:
        for (i,p) in enumerate(Primes):
            if n <= 1:
                break
            else:
                while n%p == 0:
                    n /= p
                    f[i] += 1
    return f
    
def setintz(n):
    """ Generates arrays countaining decomposition of
    all integers <= n """
    aux = [nz(i) for i in range(1,n+1)]
    intz = np.asarray(aux)
    return intz

def setbnz(n):
    """ Generates arrays containing decomposition of
    all B(k), k<=n """
    bnz = []
    bnz.append(np.zeros(LP))
    for k in range(2, n+1):
        num = facz[k-1]
        num = powerfacz(num, k-1)
        den = ultrafacz[k-2]
        den = powerfacz(den,2)
        bnz.append(divfacz(num,den))
    return np.asarray(bnz)

def sumdivisors(m):
    """ Calculates sum of divisors of m"""
    ans = 1
    for (i,p) in enumerate(Primes):
        P = int(p)
        ans = (ans*(((pow(P,int(m[i]))-1)/(P-1))%MOD))%MOD
    return ans

def solve(n):
    ans = 0
    for i in range(n):
        ans = (ans+sumdivisors(bnz[i]))%MOD
    print("Answer is", int(ans))

def write():
    f = open("intz.txt","a")
    for p in intz:
        for i in range(LP):
            if i != LP-1:
                f.write(str(int(p[i]))+";")
            else:
                f.write
        f.write("\n")
    f.close()
        
n = 20000

MOD = 10**9+7
        
intz = setintz(n)
facz = cumulsum(intz)
ultrafacz = cumulsum(facz)
bnz = setbnz(n)
bnz += 1





    
    

