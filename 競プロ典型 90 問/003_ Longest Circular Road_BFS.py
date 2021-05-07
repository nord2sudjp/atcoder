# 003 - Longest Circular Road

import sys
from collections import deque
sys.setrecursionlimit(1000000)


# N=3
# MAXN=N+1
# G=[[], [2], [1, 3], [2]]

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


N=int(input())
MAXN=N+1

G = [[] for i in range(MAXN)]

for l in sys.stdin.readlines():
    a,b = map(int, l.split())
    G[a].append(b)
    G[b].append(a)

v=bfs(MAXN,1,G)

f_i=1
f_d=0
for i,value in enumerate(v):
    #print(i,value)
    if f_d < value:
        f_i=i
        f_d=value # ‚±‚±‚ð–Y‚ê‚Ä‚¢‚½
# print(v)
# print(f_i)

v=bfs(MAXN,f_i,G)

print(max(v)+1)