# 003 - Longest Circular Road

import sys
sys.setrecursionlimit(1000000)


# N=3
# G=[[], [2], [1, 3], [2]]

def dfs(i,G,v,depth):
    v[i]=depth
    for p in G[i]:
        if v[p]==-1:
            dfs(p,G,v,depth+1)
    return

N=int(input())
MAXN=N+1

G = [[] for i in range(MAXN)]

for l in sys.stdin.readlines():
    a,b = map(int, l.split())
    G[a].append(b)
    G[b].append(a)

v=[-1]*(MAXN)

dfs(1,G,v,0)

f_i=1
f_d=0
for i,value in enumerate(v):
    #print(i,value)
    if f_d < value:
        f_i=i
        f_d=value # ‚±‚±‚ð–Y‚ê‚Ä‚¢‚½

#print(f_i)

v=[-1]*(MAXN)
dfs(f_i,G,v,0)

print(max(v)+1)