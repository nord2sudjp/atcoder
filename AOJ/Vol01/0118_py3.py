# 0118 Property Distribution
import sys
sys.setrecursionlimit(1000000)


def dfs(x,y,s,c):

    if not(0<=x<H and 0<=y<W) : return
    if G[x][y] != s: return
    if f[x][y]!=0 : return
    f[x][y]=c

    for dx,dy in d:
        nx=x+dx
        ny=y+dy
        dfs(nx,ny,s,c)
    return

d = [(1,0), (0,1), (-1,0), (0,-1)]

while True:
    H,W=map(int,input().split())
    if H==0 and W==0:break
    G=[list(input()) for i in range(H)]
    f=[[0]*W for _ in range(H)]

    cnt=1
    for i in range(H):
        for j in range(W):
            if f[i][j]==0:
                s=G[i][j]
                dfs(i,j,s,cnt)
                #print(i,j,s)
                cnt+=1
        
    
    ans=0      
    for i in f:
        ans=max(ans, max(i))
    print(ans)