from itertools import product

""" IMPORTANT : ce Project Euler a été
résolu essentiellement à la main, voir le fichier
txt pour voir le post écrit sur le forum"""

def f(k):
    fk = 0
    for p in product([0,1],repeat=k):
        if (p[0] == 0) and (p.count(0) == k//2) and (p.count(1) == k//2):
            l = list(p)
            for i in range(k//2):
                if l[0] == 1:
                    fk += 1
                    break
                else:
                    l.remove(0)
                    l.remove(1)
    return fk

print("k , f(k)")
for k in range(4,13,2):
    print(k," , ",f(k))