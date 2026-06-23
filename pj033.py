from fractions import Fraction

def graphictrick(n1,n2): # Returns 1 iff the fraction n1/n2 can be simplified using the graphic trick
    # n1 = ab and n2 = cd
    b = n1%10
    d = n2%10
    if (b == 0) and (d == 0): # Trivial case
        return False
    a = (n1-b)/10
    c = (n2-d)/10
    return ((n1*c == n2*a and b == d) or (n1*d == n2*a and b == c) or (n1*c == n2*b and a == d) or (n1*d == n2*b and a == c))

f = Fraction(1,1)

for n2 in range(10, 100):
    for n1 in range(10, n2):
        if graphictrick(n1,n2):
            f *= Fraction(n1,n2)

print "Answer is", f.denominator