import time
start = time.time()

from sympy import isprime

def count9(d):
    """Returns S(10,d) where d in [0,10]\{0,2,8}"""
    s = 0
    for a in range(10):
        for ia in range(10):
            candidatel = [d for i in range(10)]
            candidatel[ia] = str(a)
            if candidatel[0] != '0':
                candidates = ""
                for c in candidatel:
                    candidates += c
                candidate = int(candidates)
                if isprime(candidate):
                    s += candidate
    return s

def count8(d):
    """Returns S(10,d) where d in {0,2,8}"""
    s = 0
    for a in range(10): # first non-d number
        for b in range(10): # second non-d number
            for ia in range(10):
                for ib in range(ia):
                    candidatel = [d for i in range(10)]
                    candidatel[ia],candidatel[ib] = str(a),str(b)
                    if candidatel[0] != '0':
                        candidates = ""
                        for c in candidatel:
                            candidates += c
                        candidate = int(candidates)
                        if isprime(candidate):
                            s += candidate
    return s


S = 0
for d in range(10):
    if (d==0) or (d==2) or (d==8):
        S += count8(str(d))
    else:
        S += count9(str(d))

print("Answer is :",S)
print("Execution time :",round(time.time()-start,3))