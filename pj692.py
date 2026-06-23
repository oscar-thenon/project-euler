from random import randrange
from math import ceil

def game(N):
    c = randrange(1, N)
    
    N -= c
    maxi = min(N,2*c)
    print("   S |", c)
    print("Rest |", N)
    print("Next |", maxi)
    
    play = 1
    
    while N != 0:
        if play%2 == 0:
            c = randrange(1, maxi+1)
            N -= c
            maxi = min(N, 2*c)
            print("   S |", c)
            print("Rest |", N)
            print("Next |", maxi)
        else:
            c = 0
            while (c < 1) or (c > maxi):
                c = int(input("   J | "))
            N -= c
            maxi = min(N, 2*c)
            print("Rest |", N)
            print("Next |", maxi)
        play += 1
        print()
        
wins = dict()

def is_winning(N, maxi,ultimateN):
    """ Are we sure of winning with N pebbles, 
    assuming we're authorized to to take at least maxi pebbles ?"""
    if (N == 1) or (N == 2) or (maxi >= N):
        return True
        
    elif (N,maxi) in wins:
        return wins[(N,maxi)]
    
    else:
        for c in range(1, min(maxi+1,ceil(N/3))):
            if not is_winning(N-c,2*c,ultimateN):
                wins[(N,maxi)] = True
                
                maux = maxi
                naux = N
                b = False
                while maux%2 == 0:
                    maux //=2
                    naux += maux
                    if naux > ultimateN:
                        break
                    wins[(naux,maux)] = b
                    b = not b
                        
                    
                
                return True
        wins[(N,maxi)] = False
        
        maux = maxi
        naux = N
        b = True
        while maux%2 == 0:
            maux //=2
            naux += maux
            if naux > ultimateN:
                break
            wins[(naux,maux)] = b
            b = not b
        
        return False

def G(n):
    ans = 0
    for N in range(1, n+1):
        found = False
        for maxi in range(1,ceil(N/3)):
            if is_winning(N,maxi,N):
                ans += maxi
                print(N,maxi)
                found = True
                break
        if not found:
            print(N,N)
            ans += N
    return ans

F = dict()
fibo = [1,2]

def G2(n):
    F[1] = 1
    F[2] = 2
    a = 1
    b = 2
    while (a+b < n):
        c = a+b
        a = b
        b = c
        F[b] = c
        fibo.append(c)
    
    ans = sum(fibo)
    
    for (i,f) in enumerate(fibo):
        for k in range(f+1, fibo[i+1]):
            pass
            
        
        
    
    
            

