# Python‚ÅTLE
# Pypy3‚ÅAC

N,M=map(int,input().split())
D=[int(input()) for _ in range(N)]
C=[int(input()) for _ in range(M)]

# N=3
# M=5
# D=[10, 25, 15]
# C=[50, 30, 15, 40, 30]

INF=float('inf')

DP=[[INF]*(M+1) for _ in range(N+1)]

for i in range(M+1):
    DP[0][i]=0
for i in range(N+1):
    DP[i][0]=0
#print(DP)

for i in range(1,N+1):
    s=i
    e=s+(M-N)
    #print(s,e)
    for j in range(s,e+1):
        DP[i][j]=min(DP[i][j], DP[i-1][j-1] + D[i-1]*C[j-1])
        for k in range(s,j):
            #print(s,e,j,k)
            DP[i][j]=min(DP[i][j], DP[i][k])
#print(DP)            
print(min(DP[N][1:]))