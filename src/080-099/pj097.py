m = 1
for i in range(7830457):
    m = (2*m)%(10**10)
    
print "Answer is", (28433*m+1)%(10**10)