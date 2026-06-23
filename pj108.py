import time
start = time.time()

from sympy import divisor_count as dc

for k in range(1,100):
    n = 1
    while dc(n**2)//2+1 <= k:
        n += 1
    print(k,",",n,",",fi(n),",",pf(n))
    


print("\nExecution time :",round(time.time()-start,3))