""" Returns 1 iff a and b have the same digits """
def samedigits(a,b):
    at = list(str(a))
    bt = list(str(b))
    at.sort()
    bt.sort()
    return at == bt

a = 1

while 1:
    ans = True
    b = a
    for i in range(2, 7):
        b += a
        if not samedigits(a,b):
            ans = False
            break
    if ans:
        print "Answer is", a
        break
    a += 1