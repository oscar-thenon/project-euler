from math import factorial

fac = []
for i in range(0, 10):
    fac.append(factorial(i))
    
def setfac(n): # This function does nothing : I use it to set fac as a global variable
    global fac
    n.append(n)

def issumfac(n):
    m = n
    s = 0
    while m > 0:
        s += fac[m%10]
        if (s > n):
            return False
        m /= 10
    return n == s

s = 0

for n in range(10, 2696498):
    if issumfac(n):
        s += n

print "Answer is", s