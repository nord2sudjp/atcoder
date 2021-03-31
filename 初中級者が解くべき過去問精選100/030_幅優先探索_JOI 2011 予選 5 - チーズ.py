from collections import deque

# H=4
# W=5
# N=2
# G=[".X..1","....X",".XX.S",".2.X."]

H,W,N=map(int,input().split())
G=[input() for i in range(H)]

P={}
for h in range(H):
    for w in range(W):
        if G[h][w]=="S":
            P[0]=(h,w)
        elif '1' <= G[h][w] <= '9':
            P[int(G[h][w])]=(h,w)
#print(P)

r=[(1,0),(-1,0),(0,1),(0,-1)]

ans=0

for s in range(N):
    # reset queue 
    d=deque()
    d.append(P[s])
    
    # reset distance
    dis=[[-1]*W for _ in range(H)]
    dis[P[s][0]][P[s][1]]=0

    while d:
      py,px = d.popleft()
      for dy,dx in r:
        ny=py+dy;nx=px+dx
        if not(0<=ny<H and 0<=nx<W) or dis[ny][nx]!=-1 or G[ny][nx] == 'X' : continue
        dis[ny][nx]=dis[py][px]+1
        d.append((ny,nx))

    gx,gy=P[s+1]    
    #print(dis[gx][gy])
    ans+=dis[gx][gy]
print(ans)    