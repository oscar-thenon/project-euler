from fonctions import pythagorean_triples_hypo

# Importing Pythagorean primitive triples with hypothenuse < 4000
tuples = pythagorean_triples_hypo(6708)

Ma = 100 # Lower bound
Mb = 3000 # Upper bound

def solM(M):
    # Number of solutions for a given M<3000
    M2 = 2*M
    sol = 0
    for t in tuples:
        ot0,ot1 = t[0],t[1]
        t0,t1 = ot0,ot1
        while ((t0 <= M) and (t1 <= 2*M)) or ((t1 <= M) and (t0 <= 2*M)):
            if t0 <= M:
                for b in range(1,t0+1):
                    a = t1-b
                    if (a > 0) and (a <= b):
                        sol += 1
            if t1 <= M:
                for b in range(1,t1+1):
                    a = t0-b
                    if (a > 0) and (a <= b):
                        sol += 1
            t0 += ot0
            t1 += ot1
    return sol


while Ma != Mb-1:
    M = (Ma+Mb)//2 # Middle of bounds
    sol = solM(M)
    
    if sol > 10**6:
        Mb = M
    else:
        Ma = M
    
print("Answer is", Mb)