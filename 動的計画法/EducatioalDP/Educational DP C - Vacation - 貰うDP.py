N=int(input())
ABC=[list(map(int,input().split())) for _ in range(N)]

M=3

MAX_N=N+10
MAX_M=M+10

DP=[[0]*(MAX_M) for _ in range(MAX_N)]

#DP=[[0]*(MAX_N) for _ in range(MAX_M)]
# Runtime Error

# DP[i+1][j] =[i]“ú–Ú‚Å‘I‘ğˆ[j]‚ğ‚Æ‚Á‚½‚ÌÅ‘åK•Ÿ’l


for i in range(N):
        DP[i+1][0] = ABC[i][0]+max(DP[i][1], DP[i][2])
        DP[i+1][1] = ABC[i][1]+max(DP[i][0], DP[i][2])
        DP[i+1][2] = ABC[i][2]+max(DP[i][0], DP[i][1])
print(max(DP[N][0],DP[N][1],DP[N][2]))