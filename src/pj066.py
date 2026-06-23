from fractions import Fraction
from math import sqrt

def is_square(n):
    return int(sqrt(n))**2 == n

def cont_fractions(n):
    """ Return infinite continued fraction's decomposition
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
    """ Return the kth convergent fraction of [a0,cycle] """
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
    


Dmax = 0
xmax = 0

for D in range(2,1001):
    if not is_square(D):
        a0,cycle = cont_fractions(D)
        k = 1
        while 1:
            f = conv_fractions(a0,cycle,k)
            x = f.numerator
            y = f.denominator
            if (x**2-D*y**2 == 1):
                break
            else:
                k += 1
        if x > xmax:
            Dmax = D
            xmax = x

print("Answer is", Dmax)