from math import sqrt

Squares = {1}
Primes = {2, 3}

def setPrimes(n):
    global Primes
    Primes.add(n)
def setSquares(n):
    global Squares
    Squares.add(n)

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
        
odd = 9
lastp = 3 # Last prime in Primes
square = 1 # Last square in Squares
lasts = 1 # sqrt(square)

counterexample = False

while counterexample == False:

    while isprime(odd) == True: # odd shouldn't be prime
        odd += 2
    
    boundp = odd-2 # upper bound for primes
    bounds = int((odd-2)/2)+1 # upper bound for squares
    
    # Adding necessary primes
    while lastp < boundp:
        lastp += 2
        nothing = isprime(lastp)
    
    # Adding necessary squares
    while square < bounds:
        lasts += 1
        square = lasts*lasts
        Squares.add(square)
    
    # Test if odd is a counterexample or not
    counterexample = True
    for s in Squares:
        for p in Primes:
            if (odd == p+2*s):
                counterexample = False
                break
        if counterexample == False:
            break
    
    if counterexample:
        # odd is a counterexample was found
        print "Answer is", odd
    
    odd += 2