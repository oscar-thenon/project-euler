def no0(w): # Returns 1 if w doesn't contain 0
    for k in w:
        if k == '0':
            return False
    return True
def distinct(w): # Return 1 if all the digits of w are different
    s = set()
    for k in w:
        s.add(k)
    return len(w) == len(s)

# Part I : a has 1 digit and b 4 digits
    
pan14 = set() # We put the products generated here

for a in range(1, 10):
    for b in range(1000, 10000):
        wa = str(a)
        wb = str(b)
        if no0(wb) and distinct(wa+wb):
            c = a*b
            wc = str(a*b)
            if no0(wc) and distinct(wa+wb+wc):
                pan14.add(c)

# Part II : a has 2 digits and b 3 digits

pan23 = set()

for a in range(10, 100):
    for b in range(100, 1000):
        wa = str(a)
        wb = str(b)
        if no0(wa) and no0(wb) and distinct(wa+wb):
            c = a*b
            wc = str(a*b)
            if no0(wc) and distinct(wa+wb+wc):
                pan23.add(c)
                
# Part III : conclusion

products = pan14.union(pan23)

print "Answer is", sum(products)
