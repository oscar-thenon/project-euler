from fractions import Fraction

digits = {str(d):d for d in range(10)}

cs = [2,1]
for i in range(33):
    cs.append(2*(i+1))
    cs.append(1)
    cs.append(1)
cs = cs[:100]

cs.reverse()

def sum_digits(n):
    ans = 0
    for d in str(n):
        ans += digits[d]
    return ans

for (j,c) in enumerate(cs):
    if j == 0:
        f = c
    else:
        f = c+Fraction(1,f)

print("Answer is", sum_digits(f.numerator))