import time
start = time.time()

f1,f2,f3,f4 = 1,2,4,8
for i in range(50-4):
    newf = f1+f2+f3+f4
    f1,f2,f3,f4 = f2,f3,f4,newf

print("Answer is",newf)
print("\nExecution time :",round(time.time()-start,3))
    