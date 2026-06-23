from fonctions import combinations, import_tuples

sums = []

def fcomb(s):
    global sums
    sums.append(sum(s))

def is_special_sum(s,n):
    """ Is s a special sum ?
    Return 0 if not;
    Return sum(s) if yes;
    n = len(s) """
    global sums
    currentmax = 0
    for k in range(1,n+1):
        sums = []
        combinations(s,n,k,fcomb) # Generates sublists of s with lenfth k
        for x in sums:
            if sums.count(x) > 1:
                return 0
        if min(sums) <= currentmax:
            return 0
        currentmax = max(sums)
    return currentmax

ts = import_tuples("pj105_sets.txt",100)

ans = 0

for t in ts:
    ans += is_special_sum(t,len(t))

print("Answer is", ans)
        