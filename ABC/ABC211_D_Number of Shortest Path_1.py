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
    cnt=[0]*MAXN
    cnt[1]=1  # 初期パラメータ
    dist=[-1]*N
    dist[i]=0

    d=deque()
    d.append(i)

    while d:
     # print(d)
     v = d.popleft()
     for i in G[v]:
       if dist[i] == -1:
           dist[i] = dist[v] + 1
           d.append(i)
           cnt[i]=cnt[v] # 足すのはその前のcnt
       elif dist[i] == dist[v] + 1:
           cnt[i]=(cnt[i]+cnt[v])%mod # 足すのはその前のcnt
       else:
         continue
#     for i in range(len(dist)):
#         print(i+1,dist[i])
    return [dist,cnt]

dist,cnt=bfs(MAXN,1,G)

# print(dist)
#print(cnt)
# print(len(parent[N]))

print(cnt[N]%mod)
#[-1, 0, 1, 2]
