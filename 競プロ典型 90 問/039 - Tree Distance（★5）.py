# 039 - Tree DistanceÅiÅö5Åj
import sys
sys.setrecursionlimit(1000000)


N=int(input())
C=[list(map(int,input().split())) for  _ in range(N-1)]

# N=4
# C=[[1,2],[1,3],[1,4]]

DP=[0]*(N+1)
G=[[] for _ in range(N+1)]
for s,t in C:
    G[s].append(t)
    G[t].append(s)

def dfs(pos, par):
    DP[pos]=1
    for child in G[pos]:
        if child==par:continue
        dfs(child,pos)
        DP[pos]=DP[pos] + DP[child]
        
dfs(1,1)

ans=0

for pos in range(N+1):
    ans += DP[pos] * (N - DP[pos]);


print(ans)


N=int(input())
C=[list(map(int,input().split())) for  _ in range(N-1)]

# N=4
# C=[[1,2],[1,3],[1,4]]

DP=[0]*(N+1)
G=[[] for _ in range(N+1)]
for s,t in C:
    G[s].append(t)
    G[t].append(s)

def dfs(pos, par):
    DP[pos]=1
    for child in G[pos]:
        if child==par:continue
        dfs(child,pos)
        DP[pos]=DP[pos] + DP[child]
        
dfs(1,1)

ans=0

for pos in range(N+1):
    ans += DP[pos] * (N - DP[pos]);


print(ans)