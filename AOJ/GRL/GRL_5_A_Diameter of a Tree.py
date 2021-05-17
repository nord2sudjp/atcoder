# Diameter of a Tree

import sys
from collections import deque
sys.setrecursionlimit(1000000)


N=int(input())
G=[[] for _ in range(N)]
COST={}
for i in range(N-1):
    s,t,w=map(int,input().split())
    G[s].append(t)
    G[t].append(s)
    COST[(s,t)]=w
    COST[(t,s)]=w

# N=4
# G=[[1], [0, 2, 3], [1], [1]]
# COST={(0, 1): 2, (1, 0): 2, (1, 2): 1, (2, 1): 1, (1, 3): 3, (3, 1): 3}


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
       dist[i] = dist[v] + COST[(v,i)]
       d.append(i)
#     for i in range(len(dist)):
#         print(i+1,dist[i])
    return dist

v=bfs(N,0,G)
#print(v)

h_v=0
h_i=0
for i,t in enumerate(v):
    if h_v<t:
        h_i=i
        h_v=t

#print(h_i,h_v)

v=bfs(N,h_i,G)

h_v=0
h_i=0
for i,t in enumerate(v):
    if h_v<t:
        h_i=i
        h_v=t
print(h_v)