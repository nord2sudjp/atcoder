# 0408 Cave for Cats
N=int(input())
*C,=list(map(int,input().split()))

# N=4
# C=[1,2,-3,-1]
from collections import deque
d=deque()
s=set()

ans=True
for i in range(N):
    c=C[i]
    if c>0:
        if c in s:
            ans=False
            break
        d.append(c)
        s.add(c)
    else:
        if len(d)==0:
            ans=False
            break
        c1=d.pop()
        if c1!=-c:
            ans=False
            break
        s.remove(-c)
print('OK' if ans else i+1)