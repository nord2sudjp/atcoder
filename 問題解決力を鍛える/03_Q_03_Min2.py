import random
A=([random.randint(0, 100) for i in range(10)])

min1=float('infinity')
min2=float('infinity')   
 
for a in A:
    if a<=min1:
        min2=min1
        min1=a
    elif a<=min2:
        min2=a
print(sorted(A))
print(min1,min2)