import time
start = time.time()

from math import inf

""" === Importing network """

f = open("pj107_network.txt","r")
lines = f.readlines()
f.close()
N = len(lines) # Number of vertices
network = [] # network
for l in lines:
    laux = l.split(',')
    networkl = []
    for n in laux:
        if (n == '-') or (n == '-\n'):
            networkl.append(inf)
        else:
            networkl.append(int(n))
    network.append(networkl.copy())

""" === Importing netwok's original weight """ 

W = 0 # Original weight

for i in range(N):
    for j in range(i):
        w = network[i][j]
        if w != inf:
            W += network[i][j]

print("Original weight :",W)

""" === Main program """

founds = {0} # Set of vertices we have met 
foundl = [0] # Same but into a list

def findmin():
    """ Find the closest next vertice """
    minweight, minweightind = inf,inf
    for i in foundl:
        for j in range(N):
            if not (j in founds):
                minweightcandidate = network[i][j]
                if minweightcandidate < minweight:
                    minweight = minweightcandidate
                    minweightind = j
    return (minweight,minweightind)

w = 0 # Weight of the optimal network

for i in range(N-1):
    mw,mwi = findmin()
    w += mw
    founds.add(mwi)
    foundl.append(mwi)

print("Optimal weight :",w)
    
print("\nAnswer is",W-w)
print("\nExecution time :",round(time.time()-start,3))