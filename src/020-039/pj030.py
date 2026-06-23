import math

powers = []

for i in range(10):
    powers.append(pow(i,5))
    
solutions = []

def sumdigits(n):
    numbers = "0123456789"
    ns = str(n)
    s = 0
    N = len(ns)
    for i in range(N):
        s += powers[numbers.index(ns[i])]
    return s

for i in range(10, pow(10,6)):
    if i == sumdigits(i):
        solutions.append(i)

s = 0

for i in solutions:
    s += i

print "Answer is", s

""" 443839 """