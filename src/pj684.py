fib = {0:0,1:1}

def fibo(i):
    if i in fib:
        return fib[i]
    else:
        fi = fibo(i-1)+fibo(i-2)
        fib[i] = fi
        return fi

mod = 1000000007

def S(a,b): # Calulates S(9a+b) with b < 9
    return (pow(10,a,mod)*(((b+1)*(b+2))//2+5)-3*(2+3*a)-b)%mod

answer = 0

for i in range(2, 91):
    f = fibo(i)
    a = f//9
    b = f%9
    answer = (answer+S(a,b))%mod
    
print("Answer is", answer)