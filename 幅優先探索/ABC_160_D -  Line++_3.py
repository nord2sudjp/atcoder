N,X,Y=map(int,input().split())
 
ans=[0]*(N+1)

from collections import deque

def push(p,cdis):
    if p in dis:return
    dis[p]=cdis
    d.append(p)
    # print(dis,d)
 
for a in range(1,N+1):
    d=deque()
    d.append(a)
    cdis=0
    dis={a:0}
 
    while d:
      i=d.popleft()
      c=dis.get(i,0)
      if i-1>=1: push(i-1,c+1)
      if i+1<=N: push(i+1,c+1)
      if i==X: push(Y,c+1)
      if i==Y: push(X,c+1)
    # print(a,dis)
    for i in range(N+1):
        ans[dis.get(i,0)]+=1
    
for i in range(1,N):
    print(ans[i]//2)