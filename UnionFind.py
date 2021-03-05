import sys
sys.setrecursionlimit(10*18)


N,Q=map(int,input().split())

par=[i for i in range(N+1)]
size=[1]*N

def find(x):
    if par[x] == x: # 親が自分自身の時はroot
        return x
    else:
        # 経路圧縮なし
        #return find(par[x])

        #経路圧縮
        # xの親をrootにしておく
        par[x] = find(par[x]) 
        return par[x]

def same(x,y):
    return find(x) == find(y)

def unite(x,y):
    # 各グループのrootを見つける
    x = find(x) 
    y = find(y)
    
    # すでに同じグループの場合には何もしない
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

for _ in range(Q):
    c,x,y=map(int,input().split())
    if c==0: # unite
        unite(x,y)
    else:    # same
        print(1 if same(x,y) else 0)
        