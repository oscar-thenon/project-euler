lp = [2] # Liste des premiers <= 10000

N = 28123

for i in range(3, N+1, 2):
    b = 0
    for j in lp:
        if i%j == 0:
            b += 1
    if b == 0:
        lp.append(i)

print "Prime numbers done"
        
def decomp(n, facteurs):
    if n == 1:
        return [[1],[1]]
    for p in lp:
        if (p <= n) and (n%p == 0):
            facteurs[0].append(p)
            facteurs[1].append(0)
            while (n%p == 0):
                n /= p
                facteurs[1][-1] += 1
    return facteurs

def d(n):
    if n == 1:
        return 0
    facteurs = [[],[]] #decomposition en facteurs
    facteurs = decomp(n, facteurs)
    somme = 0
    puissances = []
    N = len(facteurs[0])
    for i in range(N):
        puissances.append(0)
    c = -1 # Condition d'arret
    while c >= -N:
        # On ajoute a la somme
        p = 1
        for i in range(N):
            p *= pow(facteurs[0][i],puissances[i])
        somme += p
        
        # On met a jour les puissances
        if puissances[-1] < facteurs[1][-1]:
            puissances[-1] += 1
        else:
            c = -1
            while (c >= -N) and (puissances[c] == facteurs[1][c]):
                puissances[c] = 0
                c -= 1
            if (c >= -N):
                puissances[c] += 1
    return somme-n

def is_abundant(n):
    return n < d(n)

def is_sum_abundants(n):
    N = n/2
    for i in range(1, N+1):
        if (is_abundant(i)) and (is_abundant(n-i)):
            return 1
    return 0

def ajout(t, n): # Ajoute un element a une liste deja triee
    # Cas particuliers
    if len(t) == 0:
        t = [n]
        return t
    if n > t[-1]:
        t.append(n)
        return t
    if n < t[0]:
        t.insert(0,n)
        return t
    if (n == t[0]) or (n == t[-1]):
        return t
    
    a = 0
    b = len(t)-1

    while (b != a+1):
        c = (b+a)/2
        e = t[c]
        if (n == e):
            return t
        else:
            if (n < e):
                b = c
            else:
                a = c
    t.insert(b, n)
    return t

listabundants = [] # Liste des nombres abondants < N
sum_abundants = [] # Liste des sommes de nombres abondants < N

for i in range(1, N):
    if (is_abundant(i) == 1):
        listabundants.append(i)
        
print "Abundant numbers done"

for i in range(0, len(listabundants)):
    for j in range(0, i+1):
        sum_abundants = ajout(sum_abundants, listabundants[i]+listabundants[j])
        
print "Numbers sum of abundant numbers done"
        
def complementaire(t,n): # Complementaire de la liste t dans [1, n]
    comp = []
    a = 1
    for k in t:
        if k <= N:
            for i in range(a, k):
                comp.append(i)
            a = k+1
    for i in range(a, n+1):
        comp.append(i)
    return comp

# Nombre < N ne s'ecrivant pas comme somme de deux abondants
non_sum_abundants = complementaire(sum_abundants, N)

print "Complementaires done"

somme = 0

for i in non_sum_abundants:
    somme += i

print "Answer is", somme