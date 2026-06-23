from random import randrange

knowns = {1}

COUNT = 0

def decomp(n):
    global knowns
    a = randrange(1,n)
    b = n-a


    #print(n,"|",a,b)
    if not a in knowns:
        decomp(a)
    if not b in knowns:
        decomp(b)
    knowns.add(n)


for n in range(2,201):
    mini = n-1
    knowns2 = set()
    for i in range(10**4):
        knowns = {1}
        decomp(n)
        if len(knowns)-1 < mini:
            #print(len(knowns)-1)
            #print(knowns)
            knowns2 = knowns.copy()
            mini = len(knowns)-1
    knowns2 = list(knowns2)
    knowns2.sort()
    print(n,",",mini,",",knowns2,",")
        
    
    