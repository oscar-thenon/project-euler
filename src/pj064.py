from math import sqrt

squares = {x**2 for x in range(1,101)}
nsquares = []
for k in range(1,10001):
    if not (k in squares):
        nsquares.append(k)

def eva(s,x,y):
    """ Return integer part of x/(sqrt(N)-y) """
    return int(x/(s-y))

def period(N):
    """ Return 0 if the continued fraction of sqrt(N) has 
    an even period, 1 else. """
    s = sqrt(N)
    a0 = int(s)
    xo,yo = 1,a0
    x,y = 0,0
    p = 0
    while (x != xo) or (y != yo):
        if p == 0:
            x,y = xo,yo
        ak = eva(s,x,y)
        q = (N-pow(y,2))//x
        x = q
        y = q*ak-y
        p += 1
    return p%2

ans = 0

for N in nsquares:
    ans += period(N)

print("Answer is", ans)