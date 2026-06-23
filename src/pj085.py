from math import sqrt, inf, floor

Q = 32*10**6

def l(h):
    delta = 1+Q/(h*(h+1))
    return 0.5*(sqrt(delta)-1)

def frac(n):
    """ Fractional part of n """
    return n-int(n)

optih = 0 # Optimal h
optiflh = inf # Optimal frac(l(optih))

for h in range(1,2000):
    flh = frac(l(h))
    if flh < optiflh: # We've found a better candidate
        optih, optiflh = h, flh
    
optil = floor(l(optih))

print("Answer is", optil,optih,optil*optih)