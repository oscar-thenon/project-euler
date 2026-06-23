from math import pow

starts = [1]

def addstart(n):
    s = 0
    for k in range(1, n):
        s += k*pow(10,k-1)
    s *= 9
    s += 1
    starts.append(int(s))
    
def d(n):
    while starts[-1] < n:
        addstart(len(starts)+1)
    i = 0
    while starts[i] < n:
        i += 1
    i -= 1 # d(n) is among numbers with i+1 digits
    s = starts[i]
    k = int((n-s)/(i+1))
    w = str(int(pow(10,i))+k) # d(s+(i+1)k) is the first digit of w
    reminder = n-s-(i+1)*k
    
    return int(w[reminder])

p = 1

for i in range(1, 7):
    p *= d(int(pow(10,i)))
    
print "Answer is", p