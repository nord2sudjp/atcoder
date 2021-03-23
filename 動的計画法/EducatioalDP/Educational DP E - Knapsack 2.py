N,W=map(int,input().split())
WV=[list(map(int,input().split())) for _ in range(N)]

V=10**3
MAX_V=V+10
MAX_N=N+10

DP=[[float('infinity')]*(MAX_V*MAX_N) for _ in range(MAX_N)]
DP[0][0]=0

for i in range(N):
    w,v=WV[i]
    for j in range(MAX_V*MAX_N):
    #for j in range(MAX_V):
        if j-v>=0:
            DP[i+1][j]=min(DP[i][j],DP[i][j-v]+w)
        else:
            DP[i+1][j]=DP[i][j]
            
def fmtdp(DP):
    for dp in DP:
        t=[a if a!=float('infinity') else -1 for a in dp]
        print(','.join(map(str,t)))

ans=MAX_V*MAX_N-1
while (DP[N][ans]>W):
    ans-=1
    
print(ans)