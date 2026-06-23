from math import *

n = 1 # Starting with 1 digit
A = 1 # ceil(10^(1-1/n))

counter = 0

while A < 10:
    counter += 10-A
    n += 1
    A = int(ceil(pow(10,1-1./n)))
    
print "Answer is", counter