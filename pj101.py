""" Polynomial operations """

def vpoly(p,x):
    """ Calculating p(x) where p is a polynom.
    Eg : p = [1,2,3], then result is 1+2x+3x^2 """
    ans = 0
    for (i,k) in enumerate(p):
        ans += k*pow(x,i)
    return ans
def pro(p1,d1,p2,d2):
    """ Calculating p1*p2 """
    if (p1 == [0]) or (p2 == [0]):
        return [0], 0
    else:
        q = [0]*(d1+d2+1)
        for (i,k) in enumerate(p1):
            for (j,l) in enumerate(p2):
                q[i+j] += k*l
        return q, d1+d2
def add(p1,d1,p2,d2):
    """ Calculating p1+p2 """
    if d1 > d2:
        dq = d1
        q = [0]*(dq+1)
        for i in range(d2+1):
            q[i] = p1[i]+p2[i]
        for i in range(d2+1, d1+1):
            q[i] = p1[i]
    else:
        dq = d2
        q = [0]*(dq+1)
        for i in range(d1+1):
            q[i] = p1[i]+p2[i]
        for i in range(d1+1, d2+1):
            q[i] = p2[i]
    # Updating polynom degree if necessary
    i = -1
    while (q[i] == 0) and (i >= -dq):
        i -= 1
    i += 1
    if i != 0:
        return q[:i], dq+i
    else:
        return q, dq
def sca(p,d,s):
    """ Calculating s*p where s is a scalar """
    if (s == 0):
        return [0],0
    else:
        for (i,x) in enumerate(p):
            p[i] = s*x
        return p,d

def lagrange(p,n):
    """Given a list p of n points, return the polynom
    that interpolates these points using Lagrange method"""
    pi, dpi = [0], 0 # Final polynom
    for i in range(n):
        lp, lpd = [1], 0
        for j in range(n):
            if j != i:
                q, dq = add([0,1],1,[-p[j][0]],0)
                q, dq = sca(q, dq,1/(p[i][0]-p[j][0]))
                lp, lpd = pro(lp,lpd,q,dq) # lp is now a Lagrange polynomial
        lp,lpd = sca(lp,lpd,p[i][1])
        pi, dpi = add(pi,dpi,lp,lpd)
    return pi, dpi

p, dp = [pow(-1,i) for i in range(11)], 10 # u_n polynomial

points = []
for i in range(100):
    points.append((i+1,vpoly(p,i+1)))
    
ans = 0

for k in range(10):
    pi,dpi = lagrange(points[:k+1],k+1)
    i = 1
    while 1:
        v = round(vpoly(pi,i)) # Due to approximations
        if v != points[i-1][1]:
            ans += v
            break
        i += 1
print("Answer is", ans)