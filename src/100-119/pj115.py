import time
start = time.time()

CONFIG = 0 # Number of configurations
DICO = dict() # Dictionary containing previous results
M = 50 # Minimal red block length

def fill(n,r,b):
    """
    n : row's length
    r : length that remains
    b : nature of next cell : True = red, False = gray
    Returns the number of configurations assuming we start by a cell containing 'r'
    """
    global CONFIG,DICO,M
    
    if r == 0:
            CONFIG += 1
    
    elif r < n:
        CONFIG += DICO[r,b]
        
    else:
        if b: # On essaye d'ajouter des cases rouges
            for i in range(M,r+1):
                fill(n,r-i,False)
        else: # On essaye d'ajouter des cases
            for i in range(1,r+1):
                fill(n,r-i,True)

print("n , F(50,n)")

n = 0

while CONFIG <= 10**6:
    n += 1
    CONFIG = 0
    fill(n,n,True)
    confaux = CONFIG
    DICO[(n,True)] = CONFIG
    fill(n,n,False)
    DICO[(n,False)] = CONFIG-confaux
    print(n,",",CONFIG)

print("\nExecution time :",time.time()-start)