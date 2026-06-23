def div(a,b):
    if (a%b == 0):
        return [0]
    else:
        if (a < b):
            while a < b/10:
                a *= 10
        elif (a > b):
            while b < 10*a:
                b *= 10
        
        restes = []
        quotients = []
        cont = True
        while cont:
            a *= 10
            
            if a < b:
                quotients.append(0)
                restes.append(a)
            else:
                reste = a%b
                if reste == 0:
                    return [0]
                
                if reste in restes:
                    quotients.append((a-reste)/b)
                    i = -1
                    while (restes[i] != reste):
                        i -= 1
                    quotients = quotients[i:]
                    cont = False
                else:
                    restes.append(reste)
                    quotient = (a-reste)/b
                    quotients.append(quotient)
                a = reste
        return quotients
            
cycles = []

for d in range(2, 1001):
    c = div(1, d)
    cycles.append(c)

m = 0
dm = 0

for d in range(2, 1001):
    if len(cycles[d-2]) > m:
        dm = d
        m = len(cycles[d-2])
        
def listostr(t): # Convertie une liste de chiffres en chaine de chiffres
    numbers = "0123456789"
    s = ""
    for k in t:
        s += numbers[k]
    return s

print "Answer is", dm