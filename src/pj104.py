import time
start = time.time()

"""def ispan(i):
    """ Return True iff i is 1-9 pandigital"""
    s = set(str(i))
    return not('0' in s) and (len(s) == 9)

def ispans(s):
    """ Same as ispan, but s is a string here"""
    s = set(s)
    return not('0' in s) and (len(s) == 9)

def maj_candidates(f1,f2,n,p):
    # Calculates candidates whose index is less than 10^p
    candidates = []
    while n < 10**p:
        n += 1
        f3 = (f1+f2)%10**9
        f1 = f2
        f2 = f3
        if ispan(f2):
            candidates.append(n)
    return(tuple(candidates),f1,f2,n)

def find(f1,f2,n,p,candidates):
    # Try to find the answer whose index is less than 10^p among candidates
    i = 0 # Index of the next candidate
    c = candidates[i] # Next candidate
    N = len(candidates)
    while (n < 10**p) and (not cond):
        n += 1
        f3 = f1+f2
        f1 = f2
        f2 = f3
        if (n == c):
            if ispans(str(f2)[:9]):
                print("Answer is",n)
                return 0,0,0,True
            else:
                if i < N-1:
                    i += 1
                    c = candidates[i]
                
    return (f1,f2,n,cond)

cond = False
f1m,f2m,nm = 39088169,63245986,39 # We start with F(39)
f1,f2,n = 39088169,63245986,39

p = 3 # Indexes less than 10^p
while not cond:
    candidates,f1m,f2m,nm = maj_candidates(f1,f2,n,p)
    f1,f2,n,cond = find(f1,f2,n,p,candidates)
    p += 1"""
    
print("\nExecution time :",round(time.time()-start,3))