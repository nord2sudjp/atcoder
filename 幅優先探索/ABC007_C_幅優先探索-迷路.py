from collections import deque

f=lambda:map(lambda x : int(x)-1,input().split())

R,C=map(int,input().split())
SY,SX=f()
GY,GX=f()

G=[input() for i in range(R)]
D=[[0]*C for _ in range(R)]
r=[(1,0),(-1,0),(0,1),(0,-1)]
dis=[[-1]*C for _ in range(R)]

dis[SY][SX]=0

d=deque()
d.append((SY,SX))
         
while d:
  py,px = d.popleft()
  for dy,dx in r:
    ny=py+dy;nx=px+dx
    if not(0<=ny<R and 0<=nx<C) or dis[ny][nx]!=-1 or G[ny][nx] == '#' : continue
    dis[ny][nx]=dis[py][px]+1
    d.append((ny,nx))

print(dis[GY][GX])
