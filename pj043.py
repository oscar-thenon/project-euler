L = [] # Multiples of 17

def distinct(w): # Return True iff all digits of w are different
    s = set()
    for c in w:
        s.add(c)
    return len(s) == len(w)

# Here I fill L.
c = 1
m = 17
while m <= 999:
    if (m < 100):
        w = "0"+str(m)
        if distinct(w):
            L.append(w)
    else:
        w = str(m)
        if distinct(w):
            L.append(str(m))
    c += 1
    m = 17*c

def reminder(w): # Returns the list of all digits that not occur in w
    d = "0123456789"
    r = ""
    for c in d:
        if (c in w) == 0:
            r += c
    return r

s = 0 # The lal sum

for l in L:
    R17 = reminder(l)
    for r17 in R17:
        if int(r17+l[:2])%13 == 0:
            R13 = reminder(r17+l)
            for r13 in R13:
                if int(r13+r17+l[0])%11 == 0:
                    R11 = reminder(r13+r17+l)
                    for r11 in R11:
                        if int(r11+r13+r17)%7 == 0:
                            R7 = reminder(r11+r13+r17+l)
                            for r7 in R7:
                                if int(r7+r11+r13)%5 == 0:
                                    R5 = reminder(r7+r11+r13+r17+l)
                                    for r5 in R5:
                                        if int(r5+r7+r11)%3 == 0:
                                            R3 = reminder(r5+r7+r11+r13+r17+l)
                                            for r3 in R3:
                                                if int(r3+r5+r7)%2 == 0:
                                                    begin = reminder(r3+r5+r7+r11+r13+r17+l)
                                                    s += int(begin+r3+r5+r7+r11+r13+r17+l)

print "Answer is", s