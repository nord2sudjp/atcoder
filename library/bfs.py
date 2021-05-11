# 003 - Longest Circular Road

import sys
from collections import deque
sys.setrecursionlimit(1000000)


N=3
MAXN=N+1
G=[[], [2], [1, 3], [2]]

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
