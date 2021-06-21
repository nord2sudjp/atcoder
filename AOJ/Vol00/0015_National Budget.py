# 0015:   National Budget
from decimal import Decimal, getcontext
getcontext().prec = 101

N=int(input())


for _ in range(N):
    a = Decimal(input())
    b = Decimal(input())
    ans=str(a+b)
    if len(ans)>80:
        print("overflow")
    else:
        print(ans)

