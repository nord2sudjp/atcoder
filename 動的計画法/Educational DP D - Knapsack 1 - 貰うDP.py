N,W=map(int,input().split())
WV=[list(map(int, input().split())) for _ in range(N)]

DP=[[0]*(W+10) for _ in range(N+10)]

# Nのとき、DPの行は0～Nとなる
# 下記のループでは 0～N-1→DPは1～Nまで更新される

# Wのとき、DPの列は0～Wとなる
# 下記のループでは 0～W→DPは1～Wまで更新される

for i in range(N):
  for j in range(W+1):
  # for j in range(W):
    w,v=WV[i]
    if (j<w): # 重さが制限を超えている場合には
      DP[i+1][j]=DP[i][j]
    else: # 0<=j-w
      DP[i+1][j]=max(DP[i][j], DP[i][j-w]+v)
           # 貰うDPでは提供側を比較する
      #DP[i+1][j]=max(DP[i+1][j], DP[i][j-w]+v)
           # これは配るDPの時
print(DP[N][W])