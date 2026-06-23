import numpy
import scipy.stats

N = 93

L = [1, 1] # Terms of sequence
Li = [1, 2] # Indexes

def setL(k): # Terms of sequence stocked
    global L
    L.append(k)
    
def setLi(k): # Indexes of sequence stocked
    global Li
    Li.append(k)

def fibo(n):
    if n in Li:
        return L[Li.index(n)]
    else:
        setL(fibo(n-1) + fibo(n-2))
        setLi(n)
        return L[-1]

e = fibo(N) # Calculation of N first terms 

logL = numpy.log10(L)
logL += 1 # Number of digits of each term

a,b,_,_,_ = scipy.stats.linregress(Li[5:],logL[5:]) # Calculation of the best line passing through the points : a is the slope, b the intercept 

n = (1000-b)/a # Solving the equation

print "Answer is", numpy.ceil(n)