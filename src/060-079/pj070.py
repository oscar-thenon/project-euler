from sympy.ntheory import sieve

primes = [i for i in sieve.primerange(10**3,4*10**4)]

digits = {str(d):d for d in range(10)}

def is_perm(a,b):
    """ Is b a permutation of a ? """
    sa = str(a)
    sb = str(b)
    if len(sa) != len(sb):
        return False
    else:
        occa,occb = [0]*10,[0]*10
        for d in sa:
            occa[digits[d]] += 1
        for d in sb:
            aux = digits[d]
            occb[aux] += 1
            if occb[aux] > occa[aux]:
                return False
        return True

minratio = 1.2 # According to the wording, the answer should be < 1.2
minn = 0

def solve(minratio,minn):
    for p1 in primes:
        lim = 10**7/p1
        for p2 in primes:
            if p2 >= lim:
                break
            else:
                n = p1*p2
                p = int(n*(1-1/p1)*(1-1/p2)) # p = phi(n)
                if is_perm(n,p):
                    ratio = n/p
                    if ratio < minratio:
                        minratio = ratio
                        minn = n
    print("Answer is", minn)
    
solve(minratio,minn)