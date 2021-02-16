N,K=map(int,input().split())
AB={}
for _ in range(K):
    a,b=map(int,input().split())
    AB[a]=b

MAX_N=N+10

DP=[[0]*(3) for _ in range(N+1)]

b=AB.get(1,-1)
if b==-1:
  DP[1][0]=1
  DP[1][1]=1
  DP[1][2]=1
else:
  DP[1][b-1]=1
  
#DP[1][0]=1
# 初期値の設定がおかしい。これはサンプル１にしか合わない

for i in range(2,N+1):
    t_all=sum(DP[i-1])
    b=AB.get(i,-1)
    if b==-1:
        DP[i][0] = t_all
        DP[i][1] = t_all
        DP[i][2] = t_all
        for j in range(3):
            if DP[i-1][j] != 0 and DP[i-2][j] != 0:
                DP[i][j]=DP[i][j]-DP[i-1][j]
    else:
        DP[i][b-1]=t_all
        if DP[i-1][b-1] != 0 and DP[i-2][b-1] != 0:
                DP[i][b-1]=DP[i][b-1]-DP[i-1][b-1]
        

print(sum(DP[N])%10000)