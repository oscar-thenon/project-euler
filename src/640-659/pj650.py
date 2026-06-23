from sympy.ntheory import *

def setnearestprime(n, Primes, LP):
    """ Return indexes of largest prime <= n,
    starting from 2"""
    nearestprimes = []
    for i in range(LP-1):
        k = Primes[i+1]-Primes[i]
        for j in range(k):
            nearestprimes.append(i)
            
    nb = len(nearestprimes)
    reste = n-nb-1
    for i in range(reste):
        nearestprimes.append(LP-1)
    return nearestprimes

def nz(n,Primes,LP):
    """ Decompose n in prime factors, n > 0 """
    f = [0]*LP
    if n > 1:
        for (i,p) in enumerate(Primes):
            if n <= 1:
                break
            else:
                while n%p == 0:
                    n /= p
                    f[i] += 1
    return f

def setintz(n, Primes, LP):
    """ Decompose k in prime factors, 2 <= k <= n """
    intz = []
    for k in range(2, n+1):
        intz.append(nz(k,Primes,LP))
    return intz

def powz(f, p, LP, imax):
    """ Decompose f^p. Don't check indexes after imax."""
    new = [0]*LP
    for i in range(imax+1):
        new[i] += f[i]*p
    return new

def timez(f1, f2, LP, imax):
    """ Decompose f1*f2. Don't check indexes after imax."""
    new = [0]*LP
    for i in range(imax+1):
        new[i] = f1[i]+f2[i]
    return new
        
def bn(n, LP, nearestprimes, intz):
    """ Decompose B(n) """
    imax = nearestprimes[n-2]
    p = 3-n
    bnz = powz(intz[0],p,LP,imax)
    for k in range(3, n+1):
        p += 2
        bnz = timez(bnz,powz(intz[k-2],p,LP,imax),LP,imax)
    return bnz

def sumdivisors(bn,LP,imax,Primes):
    """ Calculate sigma(bn) modulo 10^9+7 """
    ans = 1
    MOD = 10**9+7
    for i in range(imax+1):
        p = Primes[i]
        ans = (ans*((pow(p,bn[i]+1)-1)//(p-1))%MOD)%MOD
    return ans
        

def solve(N):
    """ Return S(N) modulo 10^9+7. N = 20000 is what the wording demands. """
    
    Primes = list(sieve.primerange(2, N+1)) # List of primes under N
    LP =len(Primes)
    nearestprimes = setnearestprime(N, Primes, LP)

    intz = setintz(N,Primes,LP)
    ans = 1
    MOD = 10**9+7
    for k in range(2, N+1):
        if (k-1)%100 == 0: # Just to check intermediate results
            print("S(",k-1,") =",ans)
        b = bn(k,LP,nearestprimes,intz)
        ans = (ans+sumdivisors(b,LP,nearestprimes[k-2],Primes))%MOD
    return ans
    