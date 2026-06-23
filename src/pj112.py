def isbouncy(w,l):
    """Is w a bouncy number ?
    w:string of number
    l:length of number"""
    inc = True
    dec = True
    for i in range(l-1):
        if inc and (w[i]>w[i+1]):
                inc = False # Not an increasing number
        if dec and (w[i]<w[i+1]):
                dec = False # Not a decreasing number
    return (not inc) and (not dec)
    
def reach(p):
    """Return first integer for which the proportion
    of bouncy numbers reach p"""
    reached = False # Have we reached the proportion ?
    l = 2 # Length of numbers
    bouncies = 0 # Number of boucy numbers we have met
    while not reached:
        l += 1
        for n in range(10**(l-1),10**l): # Testing all numbers with length l
            bouncies += isbouncy(str(n),l)
            pn = bouncies/n # pn is the actual proportion of bouncy numbers 
            if pn >= p:
                reached = True
                first = n
                break
    return first

print(reach(0.99))