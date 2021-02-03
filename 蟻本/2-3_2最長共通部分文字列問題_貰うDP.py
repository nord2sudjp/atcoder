N,M=map(int,input().split())
S=input()
T=input()

MAX_N=N+2
MAX_M=M+2

DP=[[0]*(MAX_N) for _ in range(MAX_M)]

#DP[i+1][j+1] : S[i]T[j]�ɑ΂���LCS�̒���

for i in range(N):
    for j in range(M):
        
        if S[i]==T[j]:
            DP[i+1][j+1]=DP[i][j]+1 #dp[i][j]�܂ł̒�����1�𑫂�����
        else:
            DP[i+1][j+1]=max(DP[i][j+1], DP[i+1][j])
print(DP[N][M])