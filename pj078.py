ps = {0:1} # Already calculated p(n)

def p(n):
    ans = 0 # The answer
    k = 1
    signk = True # True iff k > 0
    sign = 1 # Sign of sum's terms
    
    while 1:
        penta = k*(3*k-1)//2
        if n < penta:
            break
        else:
            ans += sign*ps[n-penta]
            
            if signk:
                k *= -1
            else:
                k = -k+1
                sign *= -1
            signk = not signk

    ps[n] = ans
    return ans

D = 10**6

n = 1
while 1:
    if p(n)%D == 0:
        print("Answer is", n)
        break
    else:
        n += 1