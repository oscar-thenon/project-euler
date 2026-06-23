def copie(l): # Retourne une copie de l
    l2 = []
    for i in l:
        l2.append(i)
    return l2

def join(l1, l2): # Concatenne l1 et l2 dans ce sens
    l = []
    for k in l1:
        l.append(k)
    for k in l2:
        l.append(k)
    return l

def listostr(t): # Convertie une liste de chiffres en chaine de chiffres
    numbers = "0123456789"
    s = ""
    for k in t:
        s += numbers[k]
    return s

C = 0 # Variable globale qui va compter les permutations

def incrementeC():
    global C
    C += 1

L = [] # Liste globale qui va prendre la N-ieme permutation

def setL(t):
    global L
    for k in t:
        L.append(k)

def permutations(perm, ant, N): # Genere les permutations
    if len(perm) == 1:
        incrementeC()
        if (C == N):
           setL(join(ant, perm))
    else:
        for k in perm:
            ant2 = copie(ant)
            ant2.append(k)
            perm2 = copie(perm)
            perm2.remove(k)
            permutations(perm2, ant2, N)
   

perm = []
N = 9
for i in range(N+1):
    perm.append(i)

permutations(perm, [], pow(10,6))

print "Answer is", listostr(L)