# 0557 A First Grader

N=int(input())
*S,=list(map(int,input().split()))

# N=11
# A=[8, 3, 2, 4, 8, 7, 2, 4, 0, 8, 8]


MAXM=21

DP=[[0]*(MAXM) for _ in range(N)]
DP[1][S[0]]=1
#DP[0][0]=1
# WA : ˆê”Ô–Ú‚ª0‚ÌŽž‚É‚Q‚¶‚ã‚¤‚¯‚¢‚¶‚å‚³‚ê‚Ä‚µ‚Ü‚¤B
for i in range(1,N-1):
    s=S[i]
    for j in range(MAXM):
        if j-s >= 0: 
            DP[i+1][j]=DP[i+1][j]+DP[i][j-s]
        if j+s < MAXM: 
            DP[i+1][j]=DP[i+1][j]+DP[i][j+s]
print(DP[-1][S[-1]])