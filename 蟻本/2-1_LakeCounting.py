H,W=map(int,input().split())
G=[input() for i in range(H)]

f=[[0]*W for _ in range(H)]


def dfs(x,y):
  if not(0<=x<H and 0<=y<W) : return
  if G[x][y] == '.' or f[x][y]: return
  f[x][y]=1

  for dx,dy in d:
     nx=x+dx
     ny=y+dy
     dfs(nx,ny)
  return

d = [(1,0), (0,1), (-1,0), (0,-1),(1,1),(1,-1),(-1,1),(-1,-1)] # 下、右、上、左

cnt=0

def prtmaze():
    print('-'*20)
    for g,h in zip(G,f):
        print(''.join(['.' if y==1 else x for x,y in zip(g,h)]))
        
for i in range(H):
    for j in range(W):
        if G[i][j]=='W' and f[i][j]==0: 
            dfs(i,j)
            cnt+=1
            prtmaze()
      
print(cnt)