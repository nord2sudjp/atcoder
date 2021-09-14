i1=lambda : input()
i2=lambda : int(input())
i3=lambda : map(int,input().split())
i4=lambda : list(map(int,input().split()))
i5=lambda n : [list(map(int,input().split())) for _ in range(n)]
i6=lambda n : [list(input())for _ in range(n)]
i7=lambda n : [tuple(map(int,input().split())) for _ in range(n)]

N,M=i4()
G=i5(M)

import sys
sys.setrecursionlimit(10*18)

def find(x):
    if par[x] == x: # e‚ª©•ª©g‚Ì‚Íroot
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
    
    if sy < sx: # tree y‚ª¬‚³‚¢‚Ì‚ÅAy‚Íx‚É‹zû
        par[y] = x
        size[x] += sy
    else:
        par[x] = y  # tree x‚ª¬‚³‚¢‚Ì‚ÅAx‚Íy‚É‹zû
        size[y] += sx    


# N,M=4,5
# G=[[1, 2, 1], [1, 3, 1], [1, 4, 1], [3, 2, 2], [4, 2, 2]]

# N,M=3,3
# G=[[1, 2, 1], [2, 3, 0], [3, 1, -1]]


par=[i for i in range(N+1)]
size=[1]*(N+1)

edges = []
edges_m = []
all_cost=0
for s,t,w in G:
    if w>=0:
        edges.append((w, s, t))
        all_cost=all_cost+w
    else:
        edges_m.append((w, s, t))

edges_m.sort()

for w,s,t in edges_m:
    unite(s, t)

edges.sort()
cost = 0
for w,s,t in edges:
    if not same(s, t):
        cost += w
        unite(s, t)
        
print(all_cost-cost)