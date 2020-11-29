H,W=map(int,input().split())
G=[input() for i in range(H)]

f=[[0]*W for _ in range(H)]


def dfs(x,y):
  # Validation
  if not(0<=x<H and 0<=y<W) : return

  # ゴールであるかを確認する
  if G[x][y] == 'g': # ゴールのための処理
 
  # 探索済みか、探索可能かを確認する
  if f[x][y]!=0 or G[x][y] == '#': return

  # Validation完了、探索範囲内、探索可能、ゴール以外＝＞visitフラグを立てる
  f[x][y]=1
 
  # 次の場所に向かう
  for dx,dy in d:
     nx=x+dx
     ny=y+dy
     dfs(nx,ny)
  return

d = [(1,0), (0,1), (-1,0), (0,-1)] # 下、右、上、左

for i in range(H):
    for j in range(W):
        if G[i][j]=='s': dfs(i, j)