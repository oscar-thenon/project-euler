from sympy.ntheory import primerange

numbers = set()

primes = list(primerange(2,7069+1))

N = 50*10**6

for c in range(primes.index(83)+1):
    p4 = primes[c]**4
    for b in range(primes.index(367)+1): 
        p3 = primes[b]**3
        p4p3 = p4+p3
        if p4p3 < N:
            for a in primes:
                p2 = a**2
                p4p3p2 = p4p3+p2
                if p4p3p2 < N:
                    numbers.add(p4p3p2)
                else:
                    break
        else:
            break
                    
print("Answer is", len(numbers))