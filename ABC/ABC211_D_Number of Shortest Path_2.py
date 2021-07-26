i1=lambda : input()
i2=lambda : int(input())
i3=lambda : map(int,input().split())
i4=lambda : list(map(int,input().split()))
i5=lambda n : [list(map(int,input().split())) for _ in range(n)]
i6=lambda n : [list(input())for _ in range(n)]

mod=10**9+7


import sys
from collections import deque
sys.setrecursionlimit(1000000)


N,M=i3()
G=[[] for _ in range(N+1)]
for _ in range(M):
    a,b=i3()
    G[a].append(b)
    G[b].append(a)
    
MAXN=N+1

    
# N=4
# M=5
# MAXN=N+1
# G=[[], [2, 3], [4, 1, 3], [2, 1, 4], [2, 3]]

def bfs(N,i,G):
    vs=deque()
    dist=[-1]*N
    dist[i]=0

    d=deque()
    d.append(i)

    while d:
     # print(d)
     v = d.popleft()
     vs.append(v)
     for i in G[v]:
       if dist[i] == -1:
           dist[i] = dist[v] + 1
           d.append(i)
    return [dist,vs]

dist,vs=bfs(MAXN,1,G)


#print(dist,vs)

DP=[0]*(MAXN)
DP[1]=1

while vs:
    v=vs.popleft()
    for i in G[v]:
        if dist[i]==dist[v]+1:
            DP[i]+=DP[v]%mod

# print(dist)
# print(parent)
# print(len(parent[N]))

print(DP[N]%mod)
#[-1, 0, 1, 2]
