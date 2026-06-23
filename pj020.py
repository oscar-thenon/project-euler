def setn(n):
    for i in range(200):
        n.append(0)
def resetn(n):
    for i in range(200):
        n[i] = 0
        
def copie(a,b): #copie a dans b
    for i in range(200):
        b[i] = a[i]
    
def somme(number):
    c = 0
    for i in number:
        c += i
    return c

def longueur(n):
    l = 0
    while (l < 200) and (n[l] == 0):
        l += 1
    return 200-l

def addition(n1, n2, n3):
    dizaine = 0
    for i in range(-1, -201, -1):
        k = n1[i]+n2[i]+dizaine
        unite = k%10
        n3[i] = unite
        dizaine = (k-unite)/10
    return n3
        
def multiplication(n1, n2, n3):
    n4 = []
    n5 = []
    setn(n4)
    setn(n5)
    N1 = longueur(n1)
    for i in range(-1, -N1-1,-1):
        ret = 0
        for j in range(-1,-201,-1):
            k = n1[j]*n2[i]+ret
            unite = k%10
            if (j+i>-201):
                n3[j+i+1] = unite
            ret = (k-unite)/10
        n5 = addition(n3,n4,n5)
        copie(n5, n4)
        resetn(n3)
        resetn(n5)
    return n4
        
n1 = []
n2 = []
n3 = []
setn(n1)
setn(n2)
setn(n3)
n1[-1] = 1
n2[-1] = 1

n = 100

for i in range(n-1):
    if n1[-1] < 9:
        n1[-1] += 1
    else:
        c = -1
        while n1[c] == 9:
            n1[c] = 0
            c -= 1
        n1[c] += 1
    
    n3 = multiplication(n2,n1,n3)
    copie(n3,n2)
    resetn(n3)

print "Answer is", somme(n2)