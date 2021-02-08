# ‹a–{‚Ì‰ñ“š
# float('infinity')‚ðŽg‚Á‚Ä‚¢‚é

N=4
W=5
WV=[[2,3],[1,2],[3,4],[2,2]]

V=10
MAX_V=V+10
MAX_N=N+10

DP=[[float('infinity')]*(MAX_V*MAX_N) for _ in range(N+10)]
DP[0][0]=0

for i in range(N):
    w,v=WV[i]
    for j in range(MAX_V*MAX_N):
    #for j in range(V+1):
    
        if j<v:
            DP[i+1][j]=DP[i][j]
        else:
            DP[i+1][j]=min(DP[i][j],DP[i][j-v]+w )
def fmtdp(DP):
    for dp in DP:
        print(''.join(map(str,dp)))
        
ans=0
for t in range(MAX_V*MAX_N):
    if DP[N][t]<=W: 
        # print(DP[N][t]<=W,DP[N][t],W,t)
        ans=t
print(ans)