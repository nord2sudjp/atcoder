N,M=map(int,input().split())
S=input()
T=input()

MAX_N=N+2
MAX_M=M+2

DP=[[0]*(MAX_N) for _ in range(MAX_M)]

#DP[i+1][j+1] : S[i]T[j]に対するLCSの長さ

for i in range(N):
    for j in range(M): 
        # i,jは文字列としては現在を見ている
        # DPとしては過去のDPを見ている
        # DP[i][j]は文字列S[i]T[j]までの共通文字列の長さを表す
        DP[i][j+1]=max(DP[i][j+1],DP[i][j]) 
        DP[i+1][j]=max(DP[i+1][j],DP[i][j])
        if S[i]==T[j]:
            DP[i+1][j+1]=max(DP[i+1][j+1],DP[i][j]+1) #dp[i][j]までの長さに1を足した物
print(DP[N][M])