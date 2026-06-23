def multi(a,b):
    return (a*b)%10000000000
def add(a,b):
    return (a+b)%10000000000

def calculn(n): # Calculates 10 last digits of n^n
    p = 1
    for i in range(n):
        p = multi(p,n)
    return p

s = 0
for n in range(1, 1001):
    s = add(s,calculn(n))

print "Answer is", s