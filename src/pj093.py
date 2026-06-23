from src.fonctions import combl, arrangements, repetitions
from math import inf

# Setting all possible operations
ope = ['+', '-', '*', '/']
repope = []
def farr(o):
    repope.append(o)
repetitions(ope,3,farr)

# Numbers that we have generated
numbers = set()

def isposint(n):
    if n <= 0:
        return False
    return n == int(n)

def operation(a,b,o):
    if o == '+':
        return a+b
    elif o == '-':
        return a-b
    elif o == '*':
        return a*b
    else:
        if b == 0:
            return inf
        else:
            return a/b

def frep(o,arr):
    global numbers
    
    # Right composition
    ans = operation(arr[0],arr[1],o[0])
    ans = operation(ans,arr[2],o[1])
    ans = operation(ans,arr[3],o[2])
    if (ans != inf) and (ans != -inf) and isposint(ans):
        numbers.add(int(ans))
    
    # Left composition
    ans = operation(arr[1],arr[0],o[0])
    ans = operation(arr[2],ans,o[1])
    ans = operation(arr[3],ans,o[2])
    if (ans != inf) and (ans != -inf) and isposint(ans):
        numbers.add(int(ans))

def farr(arr):
    for o in repope:
        frep(o,arr)

nmax = 0
ans = ""
g = 0

def fcomb(l):
    global nmax, ans, numbers, g
    g = 0
    
    numbers = set()
    arrangements(l,4,farr)
    n = 1
    while n in numbers:
        n += 1
    n -= 1
    if n > nmax:
        nmax = n
        ans = ""
        for k in l:
            ans += str(k)
        
combl(10,4,fcomb)

print("Answer is", ans)