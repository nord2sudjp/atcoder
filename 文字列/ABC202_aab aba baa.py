i1=lambda : input()
i2=lambda : int(input())
i3=lambda : map(int,input().split())
i4=lambda : list(map(int,input().split()))
i5=lambda n : [list(map(int,input().split())) for _ in range(n)]
import bisect as bi
import itertools as it
import collections as co
import math
from operator import mul
from functools import reduce

def pascal(N):
    pas=[[0]*N for _ in range(N)]
    pas[0][0]=1
    for i in range(N-1):
        for j in range(i+1):
            pas[i+1][j]+=pas[i][j]
            pas[i+1][j+1]+=pas[i][j]
    return pas

A,B,K=i3()

# A=2
# B=2
# K=4

pas=pascal(A+B+1)

ans=[]
while 0<A+B:
    t=pas[A+B-1][A-1]
    #print(K,A,B,A+B,t,K<t)
    if K<=t:
        ans.append('a')
        A-=1
    else:
        ans.append('b')
        B-=1
        K-=t
print(''.join(ans))

