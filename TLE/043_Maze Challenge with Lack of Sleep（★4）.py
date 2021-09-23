# 043 - Maze Challenge wihh Lack of Sleep
from collections import deque

H,W=map(int,input().split())
RS,CS=map(int,input().split())
RT,CT=map(int,input().split())
G=[list(input()) for i in range(H)]

RS,CS=RS-1,CS-1
RT,CT=RT-1,CT-1

INF=float('inf')

dirs={0:"D",1:"R",2:"U",3:"L",}


def bfs(sh,sw,G):
    direction = [(1,0), (0,1), (-1,0), (0,-1)] # 下、右、上、左
    DIST=[[INF]*4*W for _ in range(H)]
    d=deque()

    start=sh*W+sw
    
    for i in range(4):
        DIST[sh][sw*4+i]=0
        # DIST[sh][sw+i]=0 This is bug
        d.append((sh,sw,i))
    while d:
        h,w,tdir= d.popleft() # Startの場所と方向
        cost=DIST[h][w*4+tdir]

        # ゴール処理
        if h==RT and w==CT:return cost
        
        for j,(dh,dw) in enumerate(direction): # i=探索する方向
            # 探索するマス目    
            hh=h+dh
            ww=w+dw
            next_=hh*W+ww
            # 次のマス目を探索する条件
            if tdir==j:
                if (0 <= hh and hh < H and 0 <= ww and ww < W and G[hh][ww] == '.' and 
                    DIST[hh][ww*4+j] > cost):
                    DIST[hh][ww*4+j]=cost
                    d.appendleft((hh,ww,j))
            else:
                if (0 <= hh and hh < H and 0 <= ww and ww < W and G[hh][ww] == '.' and
                    DIST[hh][ww*4+j] > cost+1):
                    DIST[hh][ww*4+j]=cost+1
                    d.append((hh,ww,j))
    return INF

print(bfs(RS, CS, G))