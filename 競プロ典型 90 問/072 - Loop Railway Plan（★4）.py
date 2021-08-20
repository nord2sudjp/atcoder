# 072 - Loop Railway Plan

D = [(1,0), (0,1), (-1,0), (0,-1)] # ���A�E�A��A���A�΂�


def dfs(h,w,cnt):
      global ans
      global maxans
    
      # Validation
      if not(0<=h<H and 0<=w<W) : return
      if SH==h and SW==w:
            if maxans<cnt:maxans=cnt
      # �T���ς݂��A�T���\�����m�F����
      if f[h][w]!=0 or G[h][w] != ".": return
      #ans.append(h*W+w)
      #print("Pass",ans,cnt)
      # Validation�����A�T���͈͓��A�T���\�A�S�[���ȊO����visit�t���O�𗧂Ă�
      f[h][w]=1
    
      # ans=max(ans,cnt)

      #print(h,w,f,cnt)
      # ���̏ꏊ�Ɍ�����
      cnt+=1
      for dx,dy in D:
         nh=h+dx
         nw=w+dy
         dfs(nh,nw,cnt)
      #ans.pop(-1)
      f[h][w]=0
      return

H,W=map(int,input().split())
G=[list(input()) for _ in range(H)]

# H=3
# W=2
# G=[['.','.'],['.','#'],['.','.']]

f=[[0]*W for _ in range(H)]
ans=[]
maxans=0

SH=0
SW=0

for i in range(H):
    for j in range(W):
        if G[i][j]=="#":continue
        SH,SW=i,j
        dfs(i,j,0)
print(maxans if maxans<=2 else -1 )
# �R�[�i�[�P�[�X�͗�O���������Ă���Ƃ���ɔ������₷���B
# �����maxans==2��-1�Ƃ��Ă��������̂ق��̏ꍇ���l���邱��
# ���ׂĂ�.�����ׂĂ�#