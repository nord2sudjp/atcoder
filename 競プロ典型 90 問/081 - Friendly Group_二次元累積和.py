# 081 - Friendly Group

N,K=map(int,input().split())
L=[list(map(int,input().split())) for _ in range(N)]

def fmtDP(DP):
    print('='*10)
    for i in DP:
        print(''.join(map(str,i)))
    print('='*10)

# N,K=3,4
# L=[[1, 1], [2, 5], [7, 4]]

MAXA=5007

DP=[[0]*MAXA for _ in range(MAXA)]

for a,b in L:
    DP[a][b] = DP[a][b] + 1

DP1=[[0]*MAXA for _ in range(MAXA)]


for i in range(1,MAXA):
    for j in range(1,MAXA):
        DP1[i][j]=DP1[i][j-1]+DP1[i-1][j]-DP1[i-1][j-1]+DP[i][j]

#fmtDP(DP)        
#fmtDP(DP1)

ans=0
for i in range(K+1,MAXA):
    for j in range(K+1,MAXA):
        t=DP1[i][j]-DP1[i-K-1][j]-DP1[i][j-K-1]+DP1[i-K-1][j-K-1]
        #print(i,j,t)
        if t>ans:ans=t
print(ans)
