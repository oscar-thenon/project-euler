def isok(w):
    if len(w) > 9:
        return False
    digits = set()
    for d in w:
        if d == '0':
            return False
        else:
            digits.add(d)
    return len(digits) == len(w)

MAX = 0

# NOMBRES A 1 CHIFFRE
for n in range(1, 10):
    for i in range(5, 9):
        w = ""
        for j in range(1, i+1):
            w += str(j*n)
            if isok(w) == False:
                break
        if isok(w) and len(w) == 9: # On a bien un pandigital product
            N = int(w)
            if N > MAX:
                MAX = N

# NOMBRES A 2 CHIFFRES
for n in range(25, 34):
    w = ""
    for j in range(1, 5):
        w += str(j*n)
        if isok(w) == False:
            break
    if isok(w) and len(w) == 9: # On a bien un pandigital product
        N = int(w)
        if N > MAX:
            MAX = N

# NOMBRES A 3 CHIFFRES
for n in range(100, 334):
    w = ""
    for j in range(1, 4):
        w += str(j*n)
        if isok(w) == False:
            break
    if isok(w) and len(w) == 9: # On a bien un pandigital product
        N = int(w)
        if N > MAX:
            MAX = N

# NOMBRES A 4 CHIFFRES
for n in range(5000, 10000):
    w = ""
    for j in range(1, 3):
        w += str(j*n)
        if isok(w) == False:
            break
    if isok(w) and len(w) == 9: # On a bien un pandigital product
        N = int(w)
        if N > MAX:
            MAX = N

print "Answer is", MAX