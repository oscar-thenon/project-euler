chain = {1:1,89:89}

squares = {'0':0,'1':1,'2':4,'3':9,'4':16,'5':25,'6':36,'7':49,'8':64,'9':81}

def sumsquare(n):
    nw = str(n)
    s = 0
    for d in nw:
        s += squares[d]
    return s
        
def whichcycle(n):
    if chain.has_key(n):
        return chain[n]
    else:
        ans = whichcycle(sumsquare(n))
        chain[n] = ans
        return ans
    
counter = 0

for n in range(1, 10000000):
    if whichcycle(n) == 89:
        counter += 1

print "Answer is", counter