def int_sum(k,n):
    """ Number of (a_1,...,a_k) such as 0<a_i<n+1 and
    (a_i) is increasing"""
    s = [x for x in range(1,n+1)]
    for i in range(k-1):
        ant = 1
        for j in range(1,n):
            s[j] += ant
            ant = s[j]
    return s[-1]

def nonbouncies(k):
    """How many non-bouncies integers under 10^k there
    are ?"""
    inc = [int_sum(l,9) for l in range(1,k+1)] # Increasing numbers
    dec = [int_sum(l,10)-1 for l in range(1,k+1)] # Decreasing numbers
    nb = [inc[i]+dec[i]-9 for i in range(k)] # NBN numbers
    return sum(nb)
    
print(nonbouncies(100))