# https://qiita.com/drken/items/a5e6fe22863b7992efdb

N,A=map(int,input().split()) # 1<=N<=100,1<=A<=10000,  
*L,=map(int,input().split()) # 1<=L[i]<=1000, len(L)=N

dp=[[False]*(A+1) for _ in range(N+1)]

dp[0][0]=True

for i in range(N):
    for j in range(A+1):
        dp[i+1][j] |= dp[i][j]
        if (L[i] <= j):
            dp[i+1][j] |=dp[i][j-L[i]]
    print("i={}, j={}, dp={}".format(i,j,dp[i+1]))

print('Yes' if dp[N][A] else 'No')