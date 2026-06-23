from math import sqrt

def isprime(n):
    if n < 2:
        return False
    elif n ==2:
        return True
    else:
        for i in range(2,int(sqrt(n))+1):
            if n%i == 0:
                return False
        return True

def iscandidate(n): # A candidate is an integer which doesn't countain 2,4,5,6,8 or 0
    for d in str(n):
        if ((d == '0') or (d == '2') or (d == '4') or (d == '5') or (d == '6') or (d == '8')):
            return False
    return True

Candidates = {2,5}
Circular = set()

def setCandidates(n): # We put all candidates integers
    global Candidates
    for i in range(3, n, 2):
        if iscandidate(i) and isprime(i):
            Candidates.add(i)
            
def setcircular(n):
    global Circular
    Circular.add(n)

setCandidates(1000000)

def circular(n):
    w = str(n)
    N = len(w)
    for i in range(N):
        if (int(w) in Candidates) == False:
            return False
        w = w[1:]+w[0]
    # Here we know that n is a circular prime
    # We put in Circular n and its permutations to gain time
    for i in range(N):
        setcircular(int(w))
        w = w[1:]+w[0]
    return True

for n in Candidates:
    if ((n in Circular) == False): # No need to check n if it's already in Circular
        nothing = circular(n)

print "Answer is", len(Circular)