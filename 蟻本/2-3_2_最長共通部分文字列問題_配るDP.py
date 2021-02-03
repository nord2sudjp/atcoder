N,M=map(int,input().split())
S=input()
T=input()

MAX_N=N+2
MAX_M=M+2

DP=[[0]*(MAX_N) for _ in range(MAX_M)]

#DP[i+1][j+1] : S[i]T[j]‚É‘Î‚·‚éLCS‚Ì’·‚³

for i in range(N):
    for j in range(M): 
        # i,j‚Í•¶š—ñ‚Æ‚µ‚Ä‚ÍŒ»İ‚ğŒ©‚Ä‚¢‚é
        # DP‚Æ‚µ‚Ä‚Í‰ß‹‚ÌDP‚ğŒ©‚Ä‚¢‚é
        # DP[i][j]‚Í•¶š—ñS[i]T[j]‚Ü‚Å‚Ì‹¤’Ê•¶š—ñ‚Ì’·‚³‚ğ•\‚·
        DP[i][j+1]=max(DP[i][j+1],DP[i][j]) 
        DP[i+1][j]=max(DP[i+1][j],DP[i][j])
        if S[i]==T[j]:
            DP[i+1][j+1]=max(DP[i+1][j+1],DP[i][j]+1) #dp[i][j]‚Ü‚Å‚Ì’·‚³‚É1‚ğ‘«‚µ‚½•¨
print(DP[N][M])