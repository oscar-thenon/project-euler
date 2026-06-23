lp = [2] # Liste des premiers <= 10000

N = 10000
for i in range(3, N+1, 2):
    b = 0
    for j in lp:
        if i%j == 0:
            b += 1
    if b == 0:
        lp.append(i)
        
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

somme = 0
for i in range(1, N):
    sommediv = d(i)
    if (i != d(i)) and (d(sommediv) == i):
        #print i # Pour afficher les nombres amicaux
        somme += i
        
print "Answer is", somme