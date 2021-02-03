f=lambda:map(int,input().split())

N=3
W=7
WV=[[3,4],[4,5],[2,3]]

DP=[[0]*(W+10) for _ in range(N+10)]

for i in range(N):
    for j in range(W+1):
        w,v=WV[i]
        if (j<w):
          DP[i+1][j]=DP[i][j]
        else:
          DP[i+1][j]=max(DP[i][j], DP[i+1][j-w]+v)
print(DP[N][W])