from collections import deque


H,W=map(int,input().split())
G=[input() for i in range(H)]

r=[(1,0),(-1,0),(0,1),(0,-1)]

def bfs(si,sj):
    dis=[[-1]*W for _ in range(H)]
    dis[si][sj]=0

    d=deque()
    d.append((si,sj))

    while d:
      pi,pj = d.popleft()
      for di,dj in r:
        ni=pi+di;nj=pj+dj
        if not(0<=ni<H and 0<=nj<W) or dis[ni][nj]!=-1 or G[ni][nj] == '#' : continue
        dis[ni][nj]=dis[pi][pj]+1
        maxdis=dis[ni][nj]
        d.append((ni,nj))
    # print(maxdis)
    return(maxdis)

maxdis=0
for i in range(H):
    for j in range(W):
        if G[i][j]=='.': 
            maxdis=max(maxdis, bfs(i, j))
print(maxdis)