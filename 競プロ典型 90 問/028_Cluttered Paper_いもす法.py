N=int(input())
A=[list(map(int,input().split())) for _ in range(N)]

MAXN=1001


DP=[[0]*MAXN for _ in range(MAXN)]

for lx,ly,rx,ry in A:
    DP[lx][ly]+=1
    DP[lx][ry]-=1
    DP[rx][ly]-=1
    DP[rx][ry]+=1

DP1=[[0]*MAXN for _ in range(MAXN)]

for sy in range(MAXN):
    DP1[0][sy]=DP[0][sy]
    for sx in range(1,MAXN):
            DP1[sx][sy]=DP1[sx-1][sy]+DP[sx][sy]
DP2=[[0]*MAXN for _ in range(MAXN)]

for sx in range(MAXN):
    DP2[sx][0]=DP1[sx][0]
    for sy in range(1,MAXN):
            DP2[sx][sy]=DP2[sx][sy-1]+DP1[sx][sy]

            
import itertools            
x=list(itertools.chain.from_iterable(DP2))

import collections
c = collections.Counter(x)

#print(c)

for i in range(1,N+1):
    print(c[i])