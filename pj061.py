import sys

""" Following functions are generating numbers """
def gen3(n):
    return n*(n+1)//2
def gen4(n):
    return n**2
def gen5(n):
    return n*(3*n-1)//2
def gen6(n):
    return n*(2*n-1)
def gen7(n):
    return n*(5*n-3)//2
def gen8(n):
    return n*(3*n-2)

numbers = [[],[],[],[],[],[]]

def setnumbers():
    """ Setting numbers list"""
    
    # Triangle
    n = 45
    p = gen3(n)
    while p < 10**4:
        numbers[0].append((str(p)[:2],str(p)[2:]))
        n += 1
        p = gen3(n)
        
    # Square
    n = 32
    p = gen4(n)
    while p < 10**4:
        numbers[1].append((str(p)[:2],str(p)[2:]))
        n += 1
        p = gen4(n)
        
    # Pentagonal
    n = 26
    p = gen5(n)
    while p < 10**4:
        numbers[2].append((str(p)[:2],str(p)[2:]))
        n += 1
        p = gen5(n)
    
    # Hexagonal
    n = 23
    p = gen6(n)
    while p < 10**4:
        numbers[3].append((str(p)[:2],str(p)[2:]))
        n += 1
        p = gen6(n)
    
    # Heptagonal
    n = 21
    p = gen7(n)
    while p < 10**4:
        numbers[4].append((str(p)[:2],str(p)[2:]))
        n += 1
        p = gen7(n)
    
    # Octagonal
    n = 19
    p = gen8(n)
    while p < 10**4:
        numbers[5].append((str(p)[:2],str(p)[2:]))
        n += 1
        p = gen8(n)

setnumbers()

def answer(candidates):
    ans = 0
    for c in candidates:
        ans += int(c[0]+c[1])
    return ans

def solve(oriprefix, prefix, candidates, cat, lcat):
    """ oriprefix : prefix of the original octagonal number
    prefix : prefix to find;
    candidates : numbers already found;
    cat : categories to find;
    lcat : len(cat)"""
    
    for (i,c) in enumerate(cat):
        for n in numbers[c-3]:
            
            if oriprefix == "":
                solve(n[0],n[1],[n],[7,6,5,4,3],5)
                
            elif n[0] == prefix:
                candidates.append(n)
                cat.pop(i)
                lcat -= 1
            
                if (lcat == 0) and (n[1] == oriprefix):
                    print("Answer is", answer(candidates))
                    sys.exit()
                
                if lcat != 0:
                    solve(oriprefix,n[1],candidates,cat, lcat)
                
                candidates.pop(-1)
                cat.insert(i,c)
                lcat += 1
    
    return

solve("","",[],[8,7,6,5,4,3],6)

print("No solution found.")