roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
def roman_to_int(r):
    """ Converting a valid roman numeral r into an integer """
    n = 0
    l = len(r)
    i = 0
    while i < l:
        a = roman[r[i]]
        if i < l-1:
            b = roman[r[i+1]]
            if a >= b:
                n += a
                i += 1
            else:
                n += b-a
                i += 2
        else:
            n += a
            i += 1
    return n

romans = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
values = [1000,900,500,400,100,90,50,40,10,9,5,4,1]

def int_to_roman(n, r = "", i = 0):
    """ Converting a strictly positive integer into its
    valid and optimal roman numeral representation """
    if n == 0:
        return r
    else:
        while n < values[i]:
            i += 1
        r += romans[i]
        return int_to_roman(n-values[i],r,i)
    
ans = 0

f = open("pj089_roman.txt", "r")

for i in range(1000):
    r = f.readline().rstrip()
    lr = len(r)
    n = roman_to_int(r)
    o = int_to_roman(n)
    lo = len(o)
    ans = ans+(lr-lo)
    
f.close()

print("Answer is", ans)