from fractions import Fraction

""" Returns true iff the numerator of f has more digits than its denominator """
def num(f):
    return len(str(f.numerator)) > len(str(f.denominator))

counter = 0

u = Fraction(3,2) # First term of the sequence
for i in range(1000):
    counter += num(u)
    u = Fraction(2+u,1+u)
    
print "Answer is", counter