N,W=map(int,input().split())
VW=[list(map(int, input().split())) for _ in range(N)]

DP=[[0]*(W+10) for _ in range(N+10)]
 
for i in range(N):
    for j in range(W+1):
        DP[i+1][j] = max(DP[i+1][j], DP[i][j])
        v,w=VW[i]
        k=0
        while j+w*k<=W:
            # Œ»Ý‚Ìd‚³+w‚ª§ŒÀ“à‚Å‚ ‚ê‚Î
            DP[i+1][j+w*k]=max(DP[i+1][j+w*k], DP[i][j]+v*k)
            k+=1
print(DP[N][W])