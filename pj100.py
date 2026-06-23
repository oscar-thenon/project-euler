from sympy.ntheory.continued_fraction import *
from sympy.ntheory.primetest import is_square
from sympy import sqrt
it = continued_fraction_convergents(continued_fraction_iterator(sqrt(2)))

while 1:
    f = next(it) # Next continued fraction
    y, x = f.p, f.q
    if 2*x**2 == 1+y**2 and y%2 == 1:
        t = (1+y)//2
        if t > 10**12:
            print("Answer is", (1+int(sqrt(1+2*t*(t-1))))//2)
            break