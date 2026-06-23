from sympy.ntheory import isprime

lim = 14 # Maximum number of digits
H = set() # Here we put strong, right truncatable Harshad primes
punits = [1,3,7,9] # Possible units of a prime

def harshad(n,sumd,ln):
    
    """ Find strong, right truncatable Harshad primes
    numbers by backtracking.
    
    - n : the integer we're checking
    - sumd : sum of n's digits
    - ln : length of n"""
    
    global H
    
    for d in range(10):
        if (d != 0) or (n != 0): # We avoid the case n = 0
            naux = 10*n+d
            sumdaux = sumd+d
            
            if naux%sumdaux == 0: # Testing if n is a Harshad
                n = naux
                sumd = sumdaux
                ln += 1
                
                if isprime(n//sumd): # Testing if n is a strong Harshad
                    for p in punits:
                        paux = n*10+p
                        if isprime(paux): # Trying to generate strong, right truncatable Harshad primes from n 
                            H.add(paux)
                
                if ln == lim: # We only want to test integers less than lim digits
                    return
                
                else:
                    harshad(n,sumd,ln) 
                    sumd -= d # Backtracking
                    n //= 10
                    ln -= 1
            
    return

harshad(0,0,0)

print("Answer is", sum(H))
        
    
    
    
    
    
    
        
    





    
    
        
    




    
