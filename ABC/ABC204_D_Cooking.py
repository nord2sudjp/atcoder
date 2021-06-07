i1=lambda : input()
i2=lambda : int(input())
i3=lambda : map(int,input().split())
i4=lambda : list(map(int,input().split()))
i5=lambda n : [list(map(int,input().split())) for _ in range(n)]
import bisect as bi
import itertools as it
import collections as co


N=i2()
*T,=i4()

# N=5
# T=[8, 3, 7, 2, 5]

sumt=sum(T)
dp_t=sumt+7
DP=[[0]*(dp_t) for _ in range(N+1)]
    
for i in range(N+1):
    DP[i][0]=1

for i in range(i):
    #print(T[i])
    t=T[i]
    for j in range(t,dp_t):
        DP[i+1][j]|=DP[i][j]
        DP[i+1][j]|=DP[i][j-t]
        

ans=sumt//2

for i in range(ans,sumt+1):
    if DP[N][i]==1:
        ans=i
        break
print(max(i,sumt-i))