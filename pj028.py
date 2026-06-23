N = 1001

first = 1
last = 7

somme = 0

for i in range(2,N+1,2):
    somme += 2*(first+last)
    first = last + i
    last = first + 3*(i+2)
    if (i == N-1):
        somme += first

print "Answer is", somme

""" 669171001 """