# ALDS1_10_C

Q=int(input())

XY=[[list(input()) for _ in range(2)] for _ in range(Q)]

def solve(s,t):
    N=len(s)
    M=len(t)
    MAX_N=N+2
    MAX_M=M+2

    DP=[[0]*(MAX_M) for _ in range(MAX_N)]

    #DP[i+1][j+1] : S[i]T[j]‚É‘Î‚·‚éLCS‚Ì’·‚³

    for i in range(N):
        for j in range(M):

            if s[i]==t[j]:
                DP[i+1][j+1]=DP[i][j]+1 #dp[i][j]‚Ü‚Å‚Ì’·‚³‚É1‚ð‘«‚µ‚½•¨
            else:
                #DP[i+1][j+1]=max(DP[i][j+1], DP[i+1][j])
                if DP[i][j+1] < DP[i+1][j]:
                    DP[i+1][j+1]=DP[i+1][j]
                else:
                    DP[i+1][j+1]=DP[i][j+1]
    print(DP[N][M])

for s,t in XY:
    solve(s,t)