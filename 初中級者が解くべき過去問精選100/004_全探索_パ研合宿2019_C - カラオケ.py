N,M=map(int,input().split())
A=[list(map(int,input().split())) for i in range(N)]
ans=0
for i in range(M):
 for j in range(M):
  ans=max(ans, sum([max(A[k][i], A[k][j]) for k in range(N)]))
print(ans)