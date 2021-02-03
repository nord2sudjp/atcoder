N,W=map(int,input().split())
VW=[list(map(int, input().split())) for _ in range(N)]


DP=[[0]*(W+10) for _ in range(N+10)]

for i in range(N):
    for j in range(W+1):
        v,w=VW[i]
        if (j<w):
          DP[i+1][j]=DP[i][j]
        else:
          DP[i+1][j]=max(DP[i][j], DP[i+1][j-w]+v)
print(DP[N][W])