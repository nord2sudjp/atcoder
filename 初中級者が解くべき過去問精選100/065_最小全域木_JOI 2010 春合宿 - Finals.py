import sys
sys.setrecursionlimit(10*18)
 
V,E,K = map(int, input().split())
 
par=[i for i in range(V)]
size=[1]*V
branch=V
 
def find(x):
    if par[x] == x: # 親が自分自身の時はroot
        return x
    else:
        par[x] = find(par[x]) 
        return par[x]
 
def same(x,y):
    return find(x) == find(y)
 
def unite(x,y):
    global branch
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
    branch-=1
 
 
 
edges = []
for _ in range(E):
    s, t, w = map(int, input().split())
    edges.append((w, s, t))
edges.sort()
 
cost = 0
 
if V==K:
    print(0)
    exit()
 
for edge in edges:
    w,s,t = edge
    s-=1
    t-=1
    if not same(s, t):
        cost += w
        unite(s, t)
        if branch==K:
            break
print(cost)