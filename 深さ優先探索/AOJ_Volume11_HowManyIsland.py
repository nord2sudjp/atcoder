import sys

sys.setrecursionlimit(1000000)

D = [(1,0), (0,1), (-1,0), (0,-1), (-1,-1),(1,-1),(-1,1),(1,1) ] # ���A�E�A��A���A�΂�

def dfs(x,y):
  # Validation
  if not(0<=x<H and 0<=y<W) : return

  # �T���ς݂��A�T���\�����m�F����
  if f[x][y]!=0 or G[x][y] == 0: return

  # Validation�����A�T���͈͓��A�T���\�A�S�[���ȊO����visit�t���O�𗧂Ă�
  f[x][y]=1
 
  # ���̏ꏊ�Ɍ�����
  for dx,dy in D:
     nx=x+dx
     ny=y+dy
     dfs(nx,ny)
  return

def main():

    cnt=0
    for i in range(H):
        for j in range(W):
            if f[i][j]==0 and G[i][j]: 
                dfs(i, j)
                cnt+=1
    print(cnt)

while True:
    W,H=map(int,input().split())
    if W==0 and H==0: break
    G=[list(map(int,input().split())) for _ in range(H)]
    f=[[0]*W for _ in range(H)]

    main()