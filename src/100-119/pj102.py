from math import sqrt, acos, pi
from src.fonctions import import_tuples

def module(x,y):
    return sqrt(x**2+y**2)

def arg(x,y):
    """ Return arg(x+iy), assuming (x,y) != (0,0)
    arg returned is in [0,2pi["""
    if y >= 0:
        t = acos(x/module(x,y))
    else:
        t = -acos(x/module(x,y))
    if t < 0:
        return t+2*pi
    else:
        return t
        

def is_inside(x1,y1,x2,y2,x3,y3):
    if (x1==0 and y1==0) or (x2==0 and y2==0) or (x3==0 and y3==0):
        return False
    else:
        args = []
        args.append(arg(x1,y1))
        args.append(arg(x2,y2))
        args.append(arg(x3,y3))
        args.sort()
        return (args[1]-args[0]<pi) and (args[2]-args[1]<pi) and (pi-args[2]+args[0]<0)

points = import_tuples("pj102_triangles.txt",1000)

ans = 0

for p in points:
    ans += is_inside(p[0],p[1],p[2],p[3],p[4],p[5])

print("Answer is", ans)