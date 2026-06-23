from fractions import Fraction

D = 10**6
fbest = 0

for d in range(D, 1, -1):
    f = Fraction((3*d)//7,d)
    
    
    if (f > fbest) and (f != Fraction(3,7)):
        fbest = f
        print(fbest)
        
print("Answer is", fbest.numerator)