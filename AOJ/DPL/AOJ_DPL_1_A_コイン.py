N,M=map(int,input().split())
*P,=list(map(int, input().split())) 


DP=[[0]*(N+10) for _ in range(M+10)]

for i in range(1,N+10):
    DP[0][i]=float('inf')

for i in range(M):
    for j in range(N+1):
        p=P[i]
        if (j<p):
          DP[i+1][j]=DP[i][j]
        else:
          DP[i+1][j]=min(DP[i][j], DP[i+1][j-p]+1)
print(DP[M][N])