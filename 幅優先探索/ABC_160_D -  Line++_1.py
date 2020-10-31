N,X,Y=map(int,input().split())

from collections import deque
G=[[] for i in range(N+1)]

for i in range(1,N):
  G[i].append(i+1)
  G[i+1].append(i)

G[X].append(Y)
G[Y].append(X)

# print(G)

dis=[0]*(N+1)



for a in range(1,N):
    d=deque()
    d.append((a,0))
    cdis=0
    v=[False]*(N+1)

    while d:
      i,cdis=d.popleft()
      if v[i]:continue
      #print(i)
      v[i]=True
      #print(i,cdis)
      if a<i:
            dis[cdis]+=1
            #print(a,i,cdis)
      for p in G[i]:
            d.append((p,cdis+1))

for i in range(1,N):
    print(dis[i])