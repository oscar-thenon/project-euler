def isright(xP,yP,xQ,yQ):
    """ Return True if O,P,Q form a right triangle """
    dis = []
    dis.append(xP**2+yP**2)
    dis.append(xQ**2+yQ**2)
    dis.append((yP-yQ)**2+(xP-xQ)**2)
    dis.sort()
    return dis[0]+dis[1] == dis[2]

def equal(xP,yP,xQ,yQ):
    """ Return True if O,P,Q are all different """
    O = (0,0)
    P = (xP,yP)
    Q = (xQ,yQ)
    
    return ((O == P) or (O == Q) or (P == Q))

N = 50

ans = 0

for xP in range(N+1):
    for yP in range(N+1):
        for xQ in range(N+1):
            for yQ in range(N+1):
                if isright(xP,yP,xQ,yQ) and not (equal(xP,yP,xQ,yQ)):
                    ans += 1

print("Answer is", ans//2)