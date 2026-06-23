digits = "0123456789"

def summation(n):
    s = 0
    for d in n:
        s += digits.index(d)
    return s

MAX = 0

for a in range(99,0,-1):
    for b in range(99,0,-1):
        s = summation(str(pow(a,b)))
        if s > MAX:
            MAX = s

print "Answer is", MAX