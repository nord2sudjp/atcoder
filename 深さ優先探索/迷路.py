H,W=map(int,input().split())
G=[input() for i in range(H)]

f=[[0]*W for _ in range(H)]


def dfs(x,y):
  # Validation
  if not(0<=x<H and 0<=y<W) : return

  # �S�[���ł��邩���m�F����
  if G[x][y] == 'g': # �S�[���̂��߂̏���
 
  # �T���ς݂��A�T���\�����m�F����
  if f[x][y]!=0 or G[x][y] == '#': return

  # Validation�����A�T���͈͓��A�T���\�A�S�[���ȊO����visit�t���O�𗧂Ă�
  f[x][y]=1
 
  # ���̏ꏊ�Ɍ�����
  for dx,dy in d:
     nx=x+dx
     ny=y+dy
     dfs(nx,ny)
  return

d = [(1,0), (0,1), (-1,0), (0,-1)] # ���A�E�A��A��

for i in range(H):
    for j in range(W):
        if G[i][j]=='s': dfs(i, j)