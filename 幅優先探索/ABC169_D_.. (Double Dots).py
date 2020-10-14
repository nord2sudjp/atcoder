f=lambda:map(int,input().split())
N,M=f()
D=[[] for _ in range(N+1)]
for _ in range(M):
    a,b=f()
    D[a].append(b)
    D[b].append(a)


F=[-1]*(N+1)
F[0]=F[1]=0

from collections import deque

d=deque()
d.append((1,D[1]))

c=1
while 0<len(d):
    #print(d)
    a,b=d.popleft()
    for j in b:
        #print(a,j)
        if F[j]!=-1:continue
        F[j]=a
        d.append((j,D[j]))
if F.count(-1)!=0:
    print('No')
else:
    print('Yes')
    for i in range(2,N+1):print(F[i])