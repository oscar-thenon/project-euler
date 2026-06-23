import math

terms = {4}

for a in range(2, 101):
    for b in range(2, 101):
        r = pow(a,b)
        terms.add(r)

print "Answer is", len(terms)

""" 9183 """