import sys
import heapq
from collections import deque 

i1=lambda : input()
i2=lambda : int(input())
i3=lambda : map(int,input().split())
i4=lambda : list(map(int,input().split()))
i5=lambda n : [list(map(int,input().split())) for _ in range(n)]
i6=lambda n : [list(input())for _ in range(n)]

N=int(input())
X=i5(N)


# N=8
# X=[[1, 4], [1, 3], [1, 2], [1, 1], [3], [2], [1, 0], [2]]

P = deque()
Q = list()
D = list()

for op in X:
    if op[0]==1:
        P.append(op[1])
        #print(op[0],":",op[1],P)
    elif op[0]==2:
        if Q:
            print(heapq.heappop(Q))
        else:
            print(P.popleft())
    else:
        for p in P:
            heapq.heappush(Q,p)
        P=deque()
        #print(op[0],":",Q)
