from math import log2,ceil


def cycle(k,rest,s,p=1,e=1,l=0):
    global Nk, decomp
    
    if (l == rest):
        if (s == p) and (s < Nk):
            Nk = s
        return
    else:
        for i in range(e,k+1):
            p *= i
            if p >= Nk:
                break
            s += i
            if s >= Nk:
                break
            cycle(k,rest,s,p,i,l+1)
            s -= i
            p //= i
        
s = set()
for k in range(2,12001):
    if k%1000 == 0:
        print(k)
    Nk = 2*k
    num1 = k-ceil(log2(k)+1)+1 # Minimum number of 1s
    rest = k-num1
    cycle(k,rest,num1)
    s.add(Nk)
print("Answer is", sum(s))