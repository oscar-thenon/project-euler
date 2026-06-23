even = {'0','2','4','6','8'}

def inv(sn):
    l = list(sn)
    l.reverse()
    ans = ""
    for k in l:
        ans+=k
    return int(ans)

def isrev(n,sn):
    somme = str(n+inv(sn))
    for d in somme:
        if d in even:
            return False
    return True
    
def ans(n):
    pass
    c = 0
    for k in range(n):
        sk = str(k)
        if sk[-1] != '0':
            c += isrev(k,sk)
    return c

"""
k , ans(10^k)
1 , 0
2 , 20
3 , 120
4 , 720
5 , 720
6 , 18720
7 , 68720
"""
            
