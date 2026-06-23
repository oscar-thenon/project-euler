cb = {}

def comb(n,k):
    if cb.has_key((n,k)):
        return cb[(n,k)]
    elif (k == 0) or (n == k):
        cb[(n,k)] = 1
        return 1
    else:
        v1 = comb(n-1,k-1)
        if v1 == 0:
            cb[(n,k)] = 0
            return 0
        else:
            v2 = comb(n-1,k)
            if v2 == 0:
                cb[(n,k)] = 0
                return 0
            else:
                v = v1+v2
                if v > 1000000:
                    cb[(n,k)] = 0
                    return 0
                else:
                    cb[(n,k)] = v
                    return v
counter = 0

for n in range(1, 101):
    for k in range(0,n+1):
        if comb(n,k) == 0:
            counter += 1

print "Answer is", counter