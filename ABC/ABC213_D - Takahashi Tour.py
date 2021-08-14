import sys
sys.setrecursionlimit(1000000)

import sys
sys.setrecursionlimit(10**7)

N=int(input())
MAXN=N+1

G=[[] for _ in range(MAXN)]
for i in range(N-1):
  a, b = map(int, input().split())
  G[a].append(b)
  G[b].append(a)

# N=4
# MAXN=N+1
# G=[[],[3,2],[1,4],[1],[2]]


for g in G:
    g.sort()

print(G)

def dfs(i,par):
    ans.append(i)
    for c in G[i]:
        if c==par:continue
        dfs(c,i)
        ans.append(i)
    return

ans=[]

dfs(1,-1)
print(' '.join(map(str,ans)))