from sympy import divisor_count as dc
from sympy import prime

exceeds = 1000

def f(n):
    return 3**n//2+1 

np = 0
while f(np) <= exceeds:
    np += 1
    
primes = [prime(i) for i in range(1,np+1)]
multiplicity = [0 for i in range(np)]


def setfork():
    
    
    


    


#print("\nExecution time :",round(time.time()-start,3))