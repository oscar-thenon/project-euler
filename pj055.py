""" Returns true iff s is palindromic """
def ispalin(s):
    for i in range(int(len(s)/2)):
        if s[i] != s[-i-1]:
            return False
    return True

""" Returns true iff n is a lychrel number """
def lychrel(n):
    n += int(str(n)[::-1]) # Calculates the sum of n and its inverse
    i = 1 # Number of iterations
    
    while i < 50:
        s = str(n)
        if ispalin(s):
            return False
        else:
            n += int(s[::-1])
            i += 1
    return True

counter = 0

for n in range(1, 10000):
    counter += lychrel(n)
    
print "Answer is", counter