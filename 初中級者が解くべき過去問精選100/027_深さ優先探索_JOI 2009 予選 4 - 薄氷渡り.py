import sys

sys.setrecursionlimit(1000000)

D = [(1,0), (0,1), (-1,0), (0,-1)] # ���A�E�A��A���A�΂�

def dfs(x,y,cnt):
      global ans
      # Validation
      if not(0<=x<H and 0<=y<W) : return

      # �T���ς݂��A�T���\�����m�F����
      if f[x][y]!=0 or G[x][y] == 0: return

      # Validation�����A�T���͈͓��A�T���\�A�S�[���ȊO����visit�t���O�𗧂Ă�
      f[x][y]=1
      #G[x][y]=0
    
      ans=max(ans,cnt)

      #print(x,y,f,cnt)
      # ���̏ꏊ�Ɍ�����
      cnt+=1
      for dx,dy in D:
         nx=x+dx
         ny=y+dy
         dfs(nx,ny,cnt)
      f[x][y]=0
      return

W=int(input())
H=int(input())
G_x=[list(map(int,input().split())) for _ in range(H)]

# W=3
# H=3
# G_x=[[1, 1, 0], [1, 1, 1], [1, 1, 0]]

import copy

ans=0

for i in range(H):
    for j in range(W):
            f=[[0]*W for _ in range(H)]
            if G_x[i][j]==1:
                G=copy.deepcopy(G_x)
                dfs(i, j, 1)
                # print(i,j,f)
print(ans)