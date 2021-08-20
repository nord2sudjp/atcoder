# 072 - Loop Railway Plan

D = [(1,0), (0,1), (-1,0), (0,-1)] # 下、右、上、左、斜め


def dfs(h,w,cnt):
      global ans
      global maxans
    
      # Validation
      if not(0<=h<H and 0<=w<W) : return
      if SH==h and SW==w:
            if maxans<cnt:maxans=cnt
      # 探索済みか、探索可能かを確認する
      if f[h][w]!=0 or G[h][w] != ".": return
      #ans.append(h*W+w)
      #print("Pass",ans,cnt)
      # Validation完了、探索範囲内、探索可能、ゴール以外＝＞visitフラグを立てる
      f[h][w]=1
    
      # ans=max(ans,cnt)

      #print(h,w,f,cnt)
      # 次の場所に向かう
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
# コーナーケースは例外処理をしているところに発生しやすい。
# 今回はmaxans==2で-1としていたがそのほかの場合も考えること
# すべてが.→すべてが#