# 043 - Maze Challenge with Lack of Sleep
import sys
sys.setrecursionlimit(1000000)

H,W=map(int,input().split())
RS,CS=map(int,input().split())
RT,CT=map(int,input().split())


G=[input() for i in range(H)]

# H,W=3,3
# RS,CS=1,1
# RT,CT=3,3
# G=['..#', '#.#', '#..']

RS,CS=RS-1,CS-1
RT,CT=RT-1,CT-1

INF=float('inf')

f=[[INF]*W for _ in range(H)]


def dfs(x,y,corner,motion):
  # Validation
  if not(0<=x<H and 0<=y<W) : return
  #print(x,y,corner,motion,G[x][y])

  # �T���\�����m�F����
  if G[x][y] == '#': return
  
  # ���炩�ɂȂ��Ă���R�[�i�[��<=���݂̒T���Ȃ�ΒT���̕K�v�Ȃ�
  if f[x][y]<=corner: return

  #if f[x][y]!=0 and f[x][y]<=corner: return

  # Validation�����A�T���͈͓��A�T���\�A�S�[���ȊO����visit�t���O�𗧂Ă�
  #print(f,corner)

  f[x][y]=corner

  # �S�[���ł��邩���m�F����
  if x==RT and y==CT:return

  # ���̏ꏊ�Ɍ�����
  for i in range(1,5):
     #n_motion=i
     n_c=corner
     if motion!=0 and motion != i:
        n_c=corner+1
           
     nx=x+d[i-1][0]
     ny=y+d[i-1][1]
     dfs(nx,ny,n_c,i)
  return

d = [(1,0), (0,1), (-1,0), (0,-1)] # ���A�E�A��A��

dfs(RS, CS, 0,0)
print(f[RT][CT])