N,X,Y=map(int,input().split())
 
from collections import deque
G=[[] for i in range(N+1)]
 
for i in range(1,N):
  G[i].append(i+1)
  G[i+1].append(i)
 
G[X].append(Y)
G[Y].append(X)
 
# print(G)

ans=[0]*(N+1)

 
for a in range(1,N+1):
    d=deque()
    d.append(a)
    cdis=0
    dis={a:0}
 
    while d:
      i=d.popleft()
      cdis=dis.get(i,0)
      for p in G[i]:
        if not (p in dis):
            dis[p]=cdis+1
            d.append(p)
      # print(a,dis)
    for i in range(N+1):
        ans[dis.get(i,0)]+=1
    
for i in range(1,N):
    print(ans[i]//2)