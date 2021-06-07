import sys
sys.setrecursionlimit(1000000)

import sys
sys.setrecursionlimit(10**7)
 
N, Q = map(int, input().split())
G = [[] for i in range(N)]
cnt = [0]*N
 
# “ü—Í‚µ‚È‚ª‚çƒOƒ‰ƒt‚ğì¬
for i in range(N-1):
  a, b = map(int, input().split())
  a, b = a-1, b-1
  G[a].append(b)
  G[b].append(a)
 
 
N=3
G=[[], [2], [1, 3], [2]]

def dfs(i,G,v,depth):
    v[i]=depth
    for p in G[i]:
        if v[p]==-1:
            dfs(p,G,v,depth+1)
    return

MAXN=N+1

v=[-1]*(MAXN)

dfs(1,G,v,0)

print(v)

# [-1, 0, 1, 2]
