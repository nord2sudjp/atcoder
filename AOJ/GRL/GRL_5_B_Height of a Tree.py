# Height of a Tree
# https://hiroyuki.sano.ninja/notes/4d8091cd-87fb-44f5-9f4c-830b76357684
import sys
from collections import deque
sys.setrecursionlimit(1000000)


N=int(input())
G=[[] for _ in range(N)]
Q = sys.stdin.readlines()
for i in Q:
    s,t,w=map(int,i.split())
    G[s].append((w,t))
    G[t].append((w,s))

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
     for w,n in G[v]:
       if dist[n] != -1:
         continue
       dist[n] = dist[v] + w
       d.append(n)
#     for i in range(len(dist)):
#         print(i+1,dist[i])
    return dist

v1=bfs(N,0,G)
best1=max(enumerate(v1), key=lambda x:x[1])

v2=bfs(N,best1[0],G)
best2=max(enumerate(v2), key=lambda x:x[1])

v3=bfs(N,best2[0],G)
best3=max(enumerate(v3), key=lambda x:x[1])

for i in range(N):
    print(max(v2[i], v3[i]))
