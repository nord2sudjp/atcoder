# 003 - Longest Circular Road

import sys
from collections import deque
sys.setrecursionlimit(1000000)

G=[[] for _ in range(MAXN)]
for i in range(N-1):
  a, b = map(int, input().split())
  G[a].append(b)
  G[b].append(a)

# N=4
# MAXN=N+1
# G=[[],[2,3],[1,4],[1],[2]]

   

def bfs(N,i,G):
    dist=[-1]*N
    dist[i]=0

    d=deque()
    d.append(i)

    while d:
     # print(d)
     v = d.popleft()
     for i in G[v]:
       if dist[i] != -1:
         continue
       dist[i] = dist[v] + 1
       d.append(i)
#     for i in range(len(dist)):
#         print(i+1,dist[i])
    return dist

v=bfs(MAXN,1,G)
print(v)

#[-1, 0, 1, 2]
