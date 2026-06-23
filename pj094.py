from sympy.ntheory.continued_fraction import *
from sympy.ntheory.primetest import is_square
from sympy import sqrt

it = continued_fraction_convergents(continued_fraction_iterator(sqrt(3)))

limc = 10**9//3 

cd = [] # (c,c,c-1)
cu = [] # (c,c,c+1)

while 1:
    c = 0
    f = next(it) # f is the next continued fraction
    y = 2*f.p
    s = 2*f.q 
    if y**2-3*s**2 == 4: # Checking if (*) is solved
        if (-1+y)%3 == 0:
            c = (-1+y)//3
            ad = (c-1)*int(sqrt((c+1)*(3*c-1))) # ad = 4*A_d(c)
            if (c > 1) and (c <= limc) and (ad%4) == 0:
                cd.append(c)
        if (1+y)%3 == 0:
            c = (1+y)//3
            au = (c+1)*int(sqrt((c-1)*(3*c+1))) # au = 4*A_u(c)
            if (c > 0) and (c <= limc) and (au%4) == 0:
                cu.append(c)
    if c > limc:
        break
    
ans = 0

# Adding the perimeters
for c in cd:
    ans += 3*c-1
for c in cu:
    ans += 3*c+1
    
print("Answer is", ans)