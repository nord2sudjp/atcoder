N=int(input())
M=100
*A,=list(map(int,input().split()))
X=[[0]*(N*M+1) for _ in range(N+1)]
# N個のポイントがあり、そのポイントの最大値は100であるので、0<=ポイント<=N*Mとなる。

X[0][0]=1

for i, a in enumerate(A):  # 配列の行 
    for j in range(N*M+1): # 配列の列
        X[i+1][j]=X[i][j]
        if j >= a:
            X[i+1][j] |= X[i][j-a]
print(sum(X[N]))