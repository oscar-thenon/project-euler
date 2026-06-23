import time
start = time.time()

from math import sqrt

def line(s,point):
    """Return a line given its slope and a point"""
    return (s,point[1]-s*point[0])
def y_line(l,x):
    """Return a y given a line and a x"""
    return l[0]*x+l[1]
def perpendicular(l,point):
    """Return the perpendicular of l passing through point"""
    s = -1/l[0]
    return line(s,point)
def line_from_points(p1,p2):
    """Line passing through p1 and p2"""
    s = (p2[1]-p1[1])/(p2[0]-p1[0])
    return line(s,p1)
def intersect_lines(l1,l2):
    """Intersection of l1 and l2"""
    x = (l2[1]-l1[1])/(l1[0]-l2[0])
    y = y_line(l1,x)
    return (x,y)
def reflexion(d,Delta):
    """Return the reflexion of d with respect to Delta"""
    P = intersect_lines(d,Delta)
    P1x = P[0]+1
    P1 = (P1x,y_line(Delta,P1x))
    Deltap = perpendicular(Delta,P1)
    H = intersect_lines(Deltap,d)
    F = (2*P1[0]-H[0],2*P1[1]-H[1])
    return line_from_points(P,F)
def trinom(a,b,c):
    """Return two solutions of ax²+bx+c=0"""
    delta=b**2-4*a*c
    """print(delta)"""
    return((-b+sqrt(delta))/(2*a),(-b-sqrt(delta))/(2*a))
def intersect_ellipse(l):
    """Give the two intersections of l with the ellipse"""
    a,b=l[0],l[1]
    A,B,C=a**2+4,2*a*b,b**2-100
    (x1,x2) = trinom(A,B,C)
    return((x1,y_line(l,x1)),(x2,y_line(l,x2)))
def tangent(p):
    """Give the tangent of the ellipse passing through p"""
    s = -4*p[0]/p[1]
    return line(s,p)
def distance(p1,p2):
    """Return distance between p1 and p2"""
    return sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
def step(l,p):
    """Next step from line l and point p"""
    T = tangent(p)
    Delta = perpendicular(T,p)
    newl = reflexion(l,Delta)
    p1,p2 = intersect_ellipse(newl)
    d1,d2 = distance(p,p1),distance(p,p2)
    if d1 < d2:
        return newl,p2
    else:
        return newl,p1
def is_out(p):
    """Check if the beam has left"""
    return (p[1] > 0) and (p[0]>=-0.01) and (p[0]<=0.01)

P = (0,10.1) # Start
p = (1.4,-9.6) # First hit
l = line_from_points(P,p) # Beam
hits = 1
while not is_out(p):
    l,p = step(l,p) # New beam, new hit
    hits += 1
    
print("Answer is",hits-1) # We delete one because the last one is not a "hit"
print("\nExecution time :",round(time.time()-start,3))