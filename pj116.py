import time
start = time.time()

def g(k,n):
    """
    Calculates the number of ways to fill a row of length n with tiles of length k, allowing the empty row
    k : minimal length of coloured tiles
    n : total length of the row """
    if n < k:
        return 1
    if n == k:
        return 2
    else:
        terms = [1]*(k-1)+[2]
        for i in range(n-k):
            newterm = terms[-1]+terms[-k]
            for j in range(k-1):
                terms[j] = terms[j+1]
            terms[-1] = newterm
        return newterm

def f(k,n):
    """"Calculates the number of ways to fill a row of length n with tiles of length k
    k : minimal length of coloured tiles
    n : total length of the row """
    return g(k,n)-1

ans = 0
for k in range(2,5):
    ans += f(k,50)

print("Answer is",ans)
print("\nExecution time :",round(time.time()-start,3))