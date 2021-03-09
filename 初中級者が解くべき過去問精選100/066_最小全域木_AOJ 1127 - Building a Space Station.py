# Building a Space Station

# Building a Space Station

def is_overlap(p1,p2):
    d=dis(p1[:3],p2[:3])
    r1=p1[-1]
    r2=p2[-1]
    if r1+r2<d:
        return False
    else:
        return True

def dis(p1,p2):
    x1,y1,z1=p1
    x2,y2,z2=p2
    dis=((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)**0.5
    return dis


import sys
sys.setrecursionlimit(10*18)

def find(x):
    if par[x] == x: # e‚ªŽ©•ªŽ©g‚ÌŽž‚Íroot
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
    
    if sy < sx: # tree y‚ª¬‚³‚¢‚Ì‚ÅAy‚Íx‚É‹zŽû
        par[y] = x
        size[x] += sy
    else:
        par[x] = y  # tree x‚ª¬‚³‚¢‚Ì‚ÅAx‚Íy‚É‹zŽû
        size[y] += sx    

while True:
    N=int(input())
    if N==0:break
    
    par=[i for i in range(N)]
    size=[1]*N
    
    P=[list(map(float,input().split())) for _ in range(N)]
    
    edges = []
    for i in range(N-1):
        for j in range(i+1,N):
            if is_overlap(P[i],P[j]):
              # w=0
              unite(i,j)
            else:
              w=dis(P[i][:3],P[j][:3])
              w-=P[i][-1]+P[j][-1]
              edges.append((w, i, j))
    edges.sort()

    cost = 0
    for edge in edges:
        w, s, t = edge
        if not same(s, t):
            cost += w
            unite(s, t)
    print('{:.3f}'.format(cost))