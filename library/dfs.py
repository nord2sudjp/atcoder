mport sys
sys.setrecursionlimit(1000000)


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
