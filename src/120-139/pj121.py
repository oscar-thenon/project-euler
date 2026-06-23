import time
start = time.time()

from itertools import product
from fractions import Fraction
from math import floor

T = 15 # Number of turns
it = product(['r','b'],repeat=T) # To generate all words "RBR..." of length 15
t = T/2
p = Fraction(0,1) # Probability of winning
for i in it:
    if i.count('b')>t: # This word leads to a win
        paux = Fraction(1,1) # Probability for this word to occur
        for (j,d) in enumerate(i):
            if d == 'b':
                paux *= Fraction(1,j+2)
            else:
                paux *= Fraction(j+1,j+2)
        p += paux

print("Answer is",floor(1/p))
print("\nExecution time :",round(time.time()-start,3))