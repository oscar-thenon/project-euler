import time
s = time.time()

def rmax(a):
    am,ap,aa = a-1,a+1,a**2
    m = 2
    if a%2 == 0:
        lim = a
    else:
        lim = 2*a
    for n in range(1,lim,2):
        r = (am**n+ap**n)%aa
        if r > m:
            m = r
    return m
            
sumrmax = 0

for a in range(3,1001):
    sumrmax += rmax(a)

print(sumrmax)
print(round(time.time()-s,3))