#086_UnionFind_ABC_075_C - Bridge

import sys
sys.setrecursionlimit(10*18)


N=7
M=7
VE=[(1, 3), (2, 7), (3, 4), (4, 5), (4, 6), (5, 6), (6, 7)]


def find(x):
    if par[x] == x:
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
    
    if sy < sx:
        par[y] = x
        size[x] += sy
    else:
        par[x] = y
        size[y] += sx    

cnt=0
for i in range(M):
    # 順番に辺を取り除いていく
    t=[VE[j] for j in range(M) if i!=j]
    
    par=[i for i in range(N+1)] # parentsは自分自身
    size=[1]*(N+1) # size=1

    # Unite
    for x,y in t: 
        unite(x,y)
    
    # 1とそれ以外で分割しているかを確認
    isisolate=False
    for t in range(2,N+1):
        if same(1,t)==False:
            isisolate=True
            break
    if isisolate:
      cnt+=1
    #print(isisolate,VE[i],t)
    #print(par)
print(cnt)