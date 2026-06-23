from math import sqrt

Primes = set()
def setPrimes(n):
    global Primes
    Primes.add(n)
def isprime(n):
    if n < 2:
       return False
    elif n == 2:
        setPrimes(n)
        return True
    else:
        for i in range(2,int(sqrt(n))+1):
            if n%i == 0:
                return False
        setPrimes(n)
        return True
    
for p in range(1001, 10000, 2):
    nothing = isprime(p)
    

def works(f1, r):
    # We check if f1 is divisible by 5
    aux1 = str(f1)
    if aux1[-1] == '5':
        return False
    
    # We check if f2 is divisible by 5
    f2 = f1+r
    aux2 = str(f2)
    if aux2[-1] == '5':
        return False
    
    # We check if f1 and f2 are permutations
    f1w = sorted(aux1)
    f2w = sorted(aux2)
    
    if f1w != f2w:
        return False
    
    # We check if f3 is divisible by 5
    f3 = f2+r
    aux3 = str(f3)
    if aux3[-1] == '5':
        return False

    # We check if f3 and f2 are permutations
    f3w = sorted(aux3)
    if f3w != f2w:
        return False
    
    # Finally, we check if f1, f2 and f3 are primes
    return (f1 in Primes) and (f2 in Primes) and (f3 in Primes)

cont = True

for r in range(2, 4500, 2):
    for f1 in range(1001, 10000-2*r, 2):
        if works(f1, r) and (f1 != 1487):
            print "Answer is", str(f1)+str(f1+r)+str(f1+r+r)
            cont = False
            break
    if cont == False:
        break