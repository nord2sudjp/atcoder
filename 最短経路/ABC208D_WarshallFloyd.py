i1=lambda : input()
i2=lambda : int(input())
i3=lambda : map(int,input().split())
i4=lambda n : [list(map(int,input().split()) for _ in range(n))]

N,M=i3()

INF=float('infinity')

C=[[INF]*(N+1) for _ in range(N+1)]

for i in range(0,M):
    s,t,c=i3()
    C[s][t]=c

for i in range(0,N+1):
  C[i][i]=0

ans=0
for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            C[i][j]=min(C[i][j], C[i][k]+C[k][j])
            if C[i][j]!=INF:
              ans+=C[i][j]

print(ans)    