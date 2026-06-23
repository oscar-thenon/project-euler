def ispalindrom(w): # Returns True iff w is a palindrom
    for i in range(len(w)/2):
        if w[i] != w[-i-1]:
            return False
    return True

def incrementn2(n2): # Calculates n2+2 which is written in base 2
    if n2[-1] == '0':
        return n2[:-1] + '1'
    else:
        L = len(n2)
        i = -2
        while (i >= -L) and (n2[i] == '1'):
            i -= 1
        if (i >= -L):
            return n2[:i] + '1' + '0'*(-i-1)
        else:
            return '1' + '0'*(-i-1)

s = 1
n2 = "1"

for n in range(3, 1000000, 2):
    n2 = incrementn2(n2)
    n2 = incrementn2(n2)
    if ispalindrom(str(n)) and ispalindrom(n2):
        s += n
        
print "Answer is", s