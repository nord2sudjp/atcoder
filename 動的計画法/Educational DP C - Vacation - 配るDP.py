#N=3
#ABC=[[10,40,70],[20,50,80],[30,60,90]]

N=int(input())
ABC=[list(map(int,input().split())) for _ in range(N)]

M=3

MAX_N=N+10
MAX_M=M+10

DP=[[0]*(MAX_M) for _ in range(MAX_N)]


# DP[i+1][j] =[i]“ú–Ú‚Å‘I‘ğˆ[j]‚ğ‚Æ‚Á‚½‚ÌÅ‘åK•Ÿ’l
for i in range(N):
        a,b,c=ABC[i]
        DP[i+1][1] = max(DP[i][0]+b,DP[i+1][1])
        DP[i+1][2] = max(DP[i][0]+c,DP[i+1][2])
        
        DP[i+1][0] = max(DP[i][1]+a,DP[i+1][0])
        DP[i+1][2] = max(DP[i][1]+c,DP[i+1][2])
        
        DP[i+1][0] = max(DP[i][2]+a,DP[i+1][0])
        DP[i+1][1] = max(DP[i][2]+b,DP[i+1][1])
        
print(max(DP[N][0],DP[N][1],DP[N][2]))