N,W=map(int,input().split())
WV=[list(map(int, input().split())) for _ in range(N)]
 
DP=[[0]*(W+10) for _ in range(N+10)]
 
for i in range(N):
    for j in range(W+1): # W+1�ɂȂ邱�Ƃɗv����
        DP[i+1][j] = max(DP[i+1][j], DP[i][j])
        w,v=WV[i]
        if j+w <= W: # ���݂̏d��+w���������ł����
            DP[i+1][j+w]=max(DP[i+1][j+w], DP[i][j]+v)
print(DP[N][W])