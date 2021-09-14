# Kruskal method

import sys
sys.setrecursionlimit(10*18)

def find(x):
    if par[x] == x: # 親が自分自身の時はroot
        return x
    else:
        par[x] = find(par[x]) 
        return par[x]

def same(x,y):
    return find(x) == find(y)

def unite(x,y):
    x = find(x) 
    y = find(y)
    
    if x == y: 
        return 0
    
    sx = size[x] 
    sy = size[y]
    
    if sy < sx: # tree yが小さいので、yはxに吸収
        par[y] = x
        size[x] += sy
    else:
        par[x] = y  # tree xが小さいので、xはyに吸収
        size[y] += sx    

V, E = map(int, input().split())

par=[i for i in range(V+1)]
size=[1]*V

edges = []
for _ in range(E):
    s, t, w = map(int, input().split())
    edges.append((w, s, t))
edges.sort()

cost = 0
for edge in edges:
    w, s, t = edge
    if not same(s, t):
        cost += w
        unite(s, t)
print(cost)