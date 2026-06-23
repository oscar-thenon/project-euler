from sympy import factorial
from random import randrange

digfac = {str(d):factorial(d) for d in range(10)}

def sumfac(n):
    """ Return sum of factorial digits of n """
    ans = 0
    for d in str(n):
        ans += digfac[d]
    return ans

chain = {} # Memoization
        
def setchain(n):
    if n in chain: # Nothing to do
        return chain[n]
    
    else:
        N = n # Saving n which will be modified later
        c = [n] # c contains the cycle
        L = 1 # len(c)
        n = sumfac(n)
        ninc = n in c
        ninchain = n in chain
        
        while not ninchain and not ninc: # We stop when we get a number already known
            c.append(n)
            L += 1
            n = sumfac(n)
            ninc = n in c
            ninchain = n in chain
            
        if ninchain: # The known int is in chain
            l = chain[n]+1
            for i in range(-1,-L-1,-1):
                chain[c[i]] = l # Memoization
                l += 1
        else: # The know int is in c
            i = c.index(n)
            l = L
            for j in range(i+1):
                chain[c[j]] = l
                l -= 1
            l += 1
            for j in range(i+1,L):
                chain[c[j]] = l
                
        return chain[N]

counter = 0
for n in range(10**6):
    counter += setchain(n) == 60

print("Answer is", counter)