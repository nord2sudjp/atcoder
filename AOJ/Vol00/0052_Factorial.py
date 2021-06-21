## 0052 Factorial

import math

#N=10000

while True:
    N=int(input())
    if N==0: break
    x=str(math.factorial(N))

    ans=0
    l=len(x)-1
    for i in range(l,-1,-1):
        if x[i]=="0":ans+=1
        else:
            break
    print(ans)