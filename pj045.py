from math import sqrt

n = 285
t = 40755

def isint(n):
    return n-int(n) == 0

while 1:
    t += n+1
    
    deltah = sqrt(1+8*t)
    if isint(deltah) and (deltah+1)%4 == 0:
         deltap = sqrt(1+24*t)
         if isint(deltap) and (deltap+1)%6 == 0:
             print "Answer is", t
             break
    n += 1