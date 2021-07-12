# 008 - AtCounter

mod=10**9+7

def solve(s,t):
    N=len(s)
    M=len(t)
    MAX_N=N+2
    MAX_M=M+2

    
    DP=[[0]*(MAX_N) for _ in range(MAX_M)]
    for i in range(N):
        DP[0][i]=1

    for i in range(M):
        for j in range(N):
            if t[i]==s[j]:
                DP[i+1][j+1]=DP[i+1][j]
                DP[i+1][j+1]+=DP[i][j]
            else:
                DP[i+1][j+1]=DP[i+1][j]
    print(DP[M][N]%mod)

N=int(input())
s=input()
t="atcoder"
solve(s,t)