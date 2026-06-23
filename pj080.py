from fractions import Fraction
from math import sqrt

squares = [x**2 for x in range(1,11)]

def sumdecimals(f):
    """Return sum of 100 first decimals of f"""
    i = int(f)
    ans = i
    f = f-i
    s = ""
    for j in range(99):
        f *= 10
        d = int(f)
        ans += d
        s += str(d)
        f = f-d
    return ans

def convsqrt(n):
    """Return a fraction which approximates
    sqrt(n) with the 100 first digits correct """
    
    x = Fraction(int(10*sqrt(n)),10)
    for i in range(7):
        x = (x+n/x)/2
    return x

def solve():
    ans = 0
    for n in range(1,101):
        if not (n in squares):
            ans += sumdecimals(convsqrt(n))
    print("Answer is", ans)