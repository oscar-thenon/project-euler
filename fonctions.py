"""

The symbol * means that the function needs other local
functions. The symbol ° means that the function needs
functions from other libraries.

anagrams(a,b) : Are a and b anagrams ?
arrangements(l,k,f,p=[],lp=0) : Ordered subsets of l with k elemnts
bezout(a,d) : Bézout coefficients
combinations(li,n,k,f,i=0,s=[],l=0) : Sublists of li with k elements
combl(n,k,f,i=0,s=[],l=0) : Subsets (lists) of [0,n[ with k elements
combs(n,k,f,i=0,s=[],l=0) : Subsets of [0,n[ with k elements
cont_fractions(n) : °Continued fractions decomposition
conv_fractions(a0,cycle,k) : °kth convergent
conv_sqrt(n,k=10) : °approximates sqrt(n)
coprimes(n) : °list of coprimes
import_tuples(f,l) : import tuples from f
int_sum(k,n) : #(a_1,...,a_k) with 0<a_i<n+1 increasingly
int_to_roman(n,r="",i=0) : integer to Roman numeral
modinv(a,m) : *modular inverse
multifor(a,b,k,f) : for loop for multiple values
nextpows(lim,pows=[]) : generates powers
partition(n,d=False) : partitions of integer
pythagorean_triples(hypo=100,peri=False,pri=False) : *list of Pythagorean triples
repetitions(l,k,f,p=[],lp=0) : Ordered lists of k l's elements, with repetitions
roman_to_int(r) : Roman numeral to integer
sigma_range(n,proper=False) : Sum of divisors [1,n]
sumdiv(d,m) : *sum of divisors

"""

def anagrams(a,b):
    """ Checking if a and b are anagrams """
    la = len(a)
    lb = len(b)
    if len(a) != len(b):
        return False
    else:
        s = set() # Already checked letters
        for c in a:
            if not (c in s):
                s.add(c)
                if a.count(c) != b.count(c):
                    return False
        return True


def arrangements(l,k,f,p=[],lp=0):
    """ Generates arrangements of list l with k
    elements and treat them with f function."""
    if lp == k:
        f(p)
        return
    for (i,e) in enumerate(l):
        l.pop(i)
        arrangements(l,k,f,p+[e],lp+1)
        l.insert(i,e)

def bezout(a,d):
    """ Return (u,v) such as a*u+d*v = 1.
    a,d : integers such as a > d and gcd(a,d) = 1 """
    qs = []
    l = 0
    r = 0
    while r != 1:
        q = a//d
        qs.append(q)
        r = a-d*q
        a = d
        d = r
        l += 1
    if l == 1:
        return 1,-qs[0]
    elif l == 2:
        return -qs[1], 1+qs[0]*qs[1]
    else:
        u1, v1 = 1,-qs[0]
        u2, v2 = -qs[1], 1+qs[0]*qs[1]
        
        for k in range(2,l):
            u3, v3 = u1-u2*qs[k], v1-v2*qs[k]
            u1, v1 = u2, v2
            u2, v2 = u3, v3
        return u2,v2
    
def combinations(li,n,k,f,i=0,s=[],l=0):
    """ Return all sublists of li with k elements
    and treat them with f; n == len(li); k <= n """
    if l == k:
        f(s)
        return
    for j in range(i,n-k+l+1):
        combinations(li,n,k,f,j+1,s+[li[j]],l+1)
    
def combl(n,k,f,i=0,s=[],l=0):
    """ Return all subsets of [0,n[ with k elements into
    an ordered list and treat them with f; n > 0; k <= n """
    if l == k:
        f(s)
        return
    for j in range(i,n-k+l+1):
        combl(n,k,f,j+1,s+[j],l+1)
        
def combs(n,k,f,i=0,s=set(),l=0):
    """ Return all subsets of [0,n[ with k elements 
    and treat them with function f; n > 0; k <= n """
    if l == k:
        f(s)
        return
    for j in range(i,n-k+l+1):
        s.add(j)
        combs(n,k,f,j+1,s,l+1)
        s.remove(j)
    
def cont_fractions(n):
    from math import sqrt
    """ °Return infinite continued fraction's decomposition
    of sqrt(n). Eg : sqrt(23) = [4;1,3,1,8], thus 
    it will return (4,(1,3,1,8)) """
    def eva(s,x,y):
        """ Return integer part of x/(sqrt(N)-y) """
        return int(x/(s-y))
    s = sqrt(n)
    a0 = int(s)
    cycle = []
    xo,yo = 1,a0
    x,y = 0,0
    p = 0
    while (x != xo) or (y != yo):
        if p == 0:
            x,y = xo,yo
        ak = eva(s,x,y)
        cycle.append(ak)
        q = (n-pow(y,2))//x
        x = q
        y = q*ak-y
        p += 1
    return a0,tuple(cycle)

def conv_fractions(a0,cycle,k):
    """ °Return the kth convergent fraction of [a0,cycle] """
    from fractions import Fraction
    if k == 1:
        return a0
    else:
        l = len(cycle)
        q = (k-1)//l
        r = k-1-q*l
        conv = []
        conv.append(a0)
        for c in cycle*q:
            conv.append(c)
        for i in range(r):
            conv.append(cycle[i])
        conv.reverse()
        for (j,c) in enumerate(conv):
            if j == 0:
                f = c
            else:
                f = c+Fraction(1,f)
        return f

def conv_sqrt(n, k = 10):
    """ °Return a fraction which approximates
    sqrt(n) with the k first digits correct """
    from math import sqrt, log2
    from fractions import Fraction
    
    nit = int(log2(k))+1
    
    x = Fraction(int(10*sqrt(n)),10)
    for i in range(nit):
        x = (x+n/x)/2
    return x
    
def coprimes(n):
    """ °n > 0. Return a list of all integers which are coprimes
    with n """
    from sympy import gcd
    coprimes = [1]
    sieve = [x for x in range(2,n)]
    l = n-2
    totest = [True]*l
    for (i,x) in enumerate(sieve):
        if totest[i]:
            if gcd(x,n) != 1:
                j = i+x
                while j < l:
                    totest[j] = False
                    j += x
            else:
                coprimes.append(x)
    return coprimes

def import_tuples(f,l):
    """ Import tuples from file f containing l lines"""
    file = open(f,'r')
    tuples = []
    for i in range(l):
        line = file.readline()
        line = line.rstrip()
        aux = line.split(',')
        for (i,t) in enumerate(aux):
            aux[i] = int(t)
        tuples.append(tuple(aux))
    file.close()
    return tuples

def int_sum(k,n):
    """ Number of (a_1,...,a_k) such as 0<a_i<n+1 and
    (a_i) is increasing (not strictly)"""
    s = [x for x in range(1,n+1)]
    for i in range(k-1):
        ant = 1
        for j in range(1,n):
            s[j] += ant
            ant = s[j]
    return s[-1]

def int_to_roman(n, r = "", i = 0):
    """ Converting a strictly positive integer into its
    valid and optimal roman numeral representation """
    romans = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
    values = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    if n == 0:
        return r
    else:
        while n < values[i]:
            i += 1
        r += romans[i]
        return int_to_roman(n-values[i],r,i)

def modinv(a,m):
    """ *Return b such as a*b = 1 mod m.
    We assume that gcd(a,m) = 1"""
    u,_ = bezout(a,m)
    return u

def multifor(a,b,k,f):
    """ a < b. k > 0. f : function.
    Producing [a,b[^k tuplets and treating them with f
    function. """
    t = [a]*k
    end = False
    while not end: 
        f(tuple(t))
        i = 0
        while t[i] == b-1:
            t[i] = a
            i += 1
            if i == k:
                end = True
                break
        if not end:
            t[i] += 1

def nextpows(lim, pows=[]):
    """ lim : tableau de naturels.
    Si lim = [2, 3, 1], on veut écrire tous les tuplets
    (a, b, c) avec a<=2, b<=3, c<= 1.
    nextpows renvoie la prochaine configuration,
    sachant qu'on en est a la configuration pows. """
    if pows == []:
        return [0]*len(lim)
    
    elif pows[0] < lim[0]:
        pows[0] += 1
        return pows
    
    else:
        i = 0
        while (i < len(lim)) and (pows[i] == lim[i]):
            pows[i] = 0
            i += 1
            
        if i == len(lim):
            return []
        else:
            pows[i] += 1
            return pows

def partition(n,d=False):
    """ n : positive integer.
    return the number of partitions of n as a sum.
    if d = True, return a dictionary of partition(k) for 
    0 <= k <= n """
    
    def p(n):
        ans = 0 # The answer
        k = 1
        signk = True # True iff k > 0
        sign = 1 # Sign of sum's terms
        while 1:
            penta = k*(3*k-1)//2
            if n < penta:
                break
            else:
                ans += sign*ps[n-penta]
                
                if signk:
                    k *= -1
                else:
                    k = -k+1
                    sign *= -1
                signk = not signk
        ps[n] = ans
        return ans
    ps = {0:1} # Already calculated p(n)
    for k in range(1,n):
        _ = p(k)
    if not d:
        return p(n)
    else:
        _ = p(n)
        return ps

def pythagorean_triples_hypo(h):
    """ °Return list of primitive pythagorean triples whose
    hypothenuse do not exceed h >= 5 """
    import numpy
    A = numpy.array([[1,-2,2],[2,-1,2],[2,-2,3]])
    B = numpy.array([[1,2,2],[2,1,2],[2,2,3]])
    C = numpy.array([[-1,2,2],[-2,1,2],[-2,2,3]])
    t = numpy.array([3,4,5])
    definitivetriples = [[3,4,5]]
    triples = [numpy.array([3,4,5])]
    l = 1
    while l != 0:
        l = 0
        aux = []
        for t in triples:
            na = numpy.dot(A,t)
            if na[-1] <= h:
                aux.append(na)
                definitivetriples.append(list(na))
                l += 1
            nb = numpy.dot(B,t)
            if nb[-1] <= h:
                aux.append(nb)
                definitivetriples.append(list(nb))
                l += 1
            nc = numpy.dot(C,t)
            if nc[-1] <= h:
                aux.append(nc)
                definitivetriples.append(list(nc))
                l += 1
        triples = aux.copy()
    return definitivetriples

def pythagorean_triples_peri(p):
    """ °Return list of primitive pythagorean triples whose
    perimeter do not exceed p >= 12 """
    import numpy
    A = numpy.array([[1,-2,2],[2,-1,2],[2,-2,3]])
    B = numpy.array([[1,2,2],[2,1,2],[2,2,3]])
    C = numpy.array([[-1,2,2],[-2,1,2],[-2,2,3]])
    t = numpy.array([3,4,5])
    definitivetriples = [[3,4,5]]
    triples = [numpy.array([3,4,5])]
    l = 1
    while l != 0:
        l = 0
        aux = []
        for t in triples:
            na = numpy.dot(A,t)
            if numpy.sum(na) <= p:
                aux.append(na)
                definitivetriples.append(list(na))
                l += 1
            nb = numpy.dot(B,t)
            if numpy.sum(nb) <= p:
                aux.append(nb)
                definitivetriples.append(list(nb))
                l += 1
            nc = numpy.dot(C,t)
            if numpy.sum(nc) <= p:
                aux.append(nc)
                definitivetriples.append(list(nc))
                l += 1
        triples = aux.copy()
    return definitivetriples
    
def repetitions(l,k,f,p=[],lp=0):
    """ Generates arrangements of list l with k
    elements, allowing repetitions, and treat them
    with f function."""
    if lp == k:
        f(p)
        return
    for e in l:
        repetitions(l,k,f,p+[e],lp+1)

def roman_to_int(r):
    """ Converting a valid roman numeral r into an integer """
    roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    n = 0
    l = len(r)
    i = 0
    while i < l:
        a = roman[r[i]]
        if i < l-1:
            b = roman[r[i+1]]
            if a >= b:
                n += a
                i += 1
            else:
                n += b-a
                i += 2
        else:
            n += a
            i += 1
    return n

def sigma_range(n,proper=False):
    """ Return a list of sum of k's divisors, for 
    k in [0, n]. If proper = True, then we substract n.
    We consider sigma(0)=0 in both cases by convention"""
    c = proper+1
    sieve = [0]*(n+1)
    for i in range(1,n+1):
        for j in range(c*i,n+1,i):
            sieve[j] += i
    return sieve

def sumdiv(d,m=0):
    """ *Return the sum of divisors of d mod m.
    d is a 2d-list, first line are prime factors, second is
    their multiplicity. e.g : 2^3*5^4 corresponds to
    d = [[2,5],[3,4]]. Requires modinv function. """
    pinv = [modinv(p-1,m) for p in d[0]]
    ans = 1
    for (i,p) in enumerate(d[0]):
        ans = (ans*(((pow(p,d[1][i]+1,m)-1)*pinv[i])%m))%m
    return ans

def lambert(x,step=100):
    """ Solve y*exp(y) = x for y.
    There's at most 2 solutions"""
    from math import exp,nan
    def f(x):
        return x*exp(x)
    def lcroiss(x,a,b,step):
        for i in range(step):
            y = (a+b)/2
            v = f(y)
            if v < x:
                a = y
            else:
                b = y
        return y
    def ldecroiss(x,a,b,step):
        for i in range(step):
            y = (a+b)/2
            v = f(y)
            if v < x:
                b = y
            else:
                a = y
        return y
    if x == 0:
        return 0,nan
    elif x == -1/(exp(1)):
        return -1,nan
    elif x == (exp(1)):
        return 1,nan
    elif x > 0:
        a = 0
        b = 1
        while f(b) < x:
            a = b
            b *= 2
        return lcroiss(x,a,b,step),nan
    elif x > -1/(exp(1)):
        x1 = lcroiss(x,-1,0,step)
        a,b = -2,-1
        while f(a) < x:
            b = a
            a *= 2
        x2 = ldecroiss(x,a,b,step)
        return x2,x1
    else:
        return nan,nan