from itertools import permutations

dig = {k:str(k) for k in range(1, 11)}

a = [1,2,3,4,5,6,7,8,9,10]

pmax = 0

def t_to_string(t):
    # Convert a line into string
    s0 = dig[t[0]]+dig[t[5]]+dig[t[6]]
    s1 = dig[t[1]]+dig[t[6]]+dig[t[7]]
    s2 = dig[t[2]]+dig[t[7]]+dig[t[8]]
    s3 = dig[t[3]]+dig[t[8]]+dig[t[9]]
    s4 = dig[t[4]]+dig[t[9]]+dig[t[5]]
    return s0,s1,s2,s3,s4

for p in permutations(a):
    
    # Calculatinf one line to have the sum
    somme = p[0]+p[5]+p[6]
    
    # Testing if other lines match
    if (p[1]+p[6]+p[7] == somme) and (p[2]+p[7]+p[8] == somme) and (p[3]+p[8]+p[9] == somme) and (p[4]+p[9]+p[5] == somme): 
        
        # Convert lines into strings
        s0,s1,s2,s3,s4 = t_to_string(p)
        
        if len(s0+s1+s2+s3+s4) == 16:
        
            # Find the smallest external node and make the global string
            if (p[0] < p[1]) and (p[0] < p[2]) and (p[0] < p[3]) and (p[0] < p[4]):
                s = int(s0+s1+s2+s3+s4)
            elif (p[1] < p[0]) and (p[1] < p[2]) and (p[1] < p[3]) and (p[1] < p[4]):
                s = int(s1+s2+s3+s4+s0)
            elif (p[2] < p[0]) and (p[2] < p[1]) and (p[2] < p[3]) and (p[2] < p[4]):
                s = int(s2+s3+s4+s0+s1)
            elif (p[3] < p[0]) and (p[3] < p[1]) and (p[3] < p[2]) and (p[3] < p[4]):
                s = int(s3+s4+s0+s1+s2)
            else:
                s = int(s4+s0+s1+s2+s3)
                
            # Updates pmax
            if s > pmax:
                print(s)
                pmax = s
            
print("Answer is", pmax)