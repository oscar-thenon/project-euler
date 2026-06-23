def isol(a, p):
    if (p*(2*a-p))%(2*(a-p)) != 0:
        return False
    else:
        return (p*(2*a-p))/(2*(a-p))>a
    
CMAX = 0
PMAX = 0
        
for p in range(2, 1001, 2):
    c = 0
    for a in range(1, p/2):
        c += isol(a, p)
    if c > CMAX:
        CMAX = c
        PMAX = p

print "Answer is", PMAX