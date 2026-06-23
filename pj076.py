from math import ceil
            
Saves = {}

""" #ways to get N with a additions, the right number is <= lim """
def S(N, a, lim):
    if a == 1: # There's only one addition
        return min(lim, N-a)-ceil(N/2)+1
    
    elif (a == N-1) or (a == N-2): # Simplifications
        return 1
    
    elif (N, a, lim) in Saves: # Memoization
        return Saves[(N, a, lim)]
    
    else:
        ans = 0
        realim = min(lim, N-a)
        
        for k in range(ceil(N/(a+1)), realim+1):
            ans += S(N-k, a-1, k)
            
        Saves[(N, a, lim)] = ans
        return ans
            
N = 100

answer = 0
for a in range(1, N):
    answer += S(N,a,N-a)

print("Answer is", answer)



        
    
    

        


        
    
    