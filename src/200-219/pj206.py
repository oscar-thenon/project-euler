digits = ['2','3','4','5','6','7','8','9']

def answer(n):
    s = str(n**2)
    for i in range(1,9):
        if s[2*i] != digits[i-1]:
            
            return False
    return True

for n in range(10**9+70,142*10**7,100):
    if answer(n):
        print "Answer is", n
        break