import time
from math import sqrt

def temp_even(nw,l,maxi,tab):
    """nw : remaining template to decompose
    l : length of remaining template
    maxi : maxi/2
    tab : lengths saved"""
    global stock
    if l == 0:
        m = max(tab)
        if m == maxi: # At least one term as to have a length of maxi-1
            stock.append(tuple(tab))
    for i in range(min(maxi,l),0,-1):
        temp_even(nw[i:],l-i,maxi,tab+[i])

# Set templates for even lengths
stock = []
temp_even('_'*2,2,1,[])
temp_2 = stock.copy()
stock = []
temp_even('_'*4,4,2,[])
temp_4 = stock.copy()
stock = []
temp_even('_'*6,6,3,[])
temp_6 = stock.copy()
stock = []
temp_even('_'*8,8,4,[])
temp_8 = stock.copy()
stock = []
temp_even('_'*10,10,5,[])
temp_10 = stock.copy()
stock = []
temp_even('_'*12,12,6,[])
temp_12 = stock.copy()

def temp_odd(nw,l,maxi,tab):
    """nw : remaining template to decompose
    l : length of remaining template
    maxi : maxi/2
    tab : lengths saved"""
    global stock
    if l == 0:
        m = max(tab)
        if m == maxi: # At least one term as to have a length of maxi-1
            stock.append(tuple(tab))
    for i in range(min(maxi,l),0,-1):
        temp_even(nw[i:],l-i,maxi,tab+[i])



def decompose(n,t):
    """Decomposing n following the template t"""
    s,a,b = 0,0,0
    for k in t:
        b += k
        s += int(n[a:b])
        a = b
    return s

st = time.time()

perc = 0
k = 9


for r in range(int(sqrt(10**k))+1,int(sqrt(10**(k+1)))):
    s = r**2
    
    
    for t in temp_10:
        if decompose(str(s),t) == r:
            print(s,r)
        
print(time.time()-st)
    
    