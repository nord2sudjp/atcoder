from itertools import *
f=lambda:[*map(int,input().split())]
N,M=f()
x=[f() for i in range(M)]
x=[*x,*[[t,s] for s,t in x]]
 
ans=1
for n in range(2,N+1):
 for d in [*combinations(range(1,N+1),n)]:
  if all(u in x for u in [[i,j] for j in d for i in d if (i<j)]): ans=n
print(ans)