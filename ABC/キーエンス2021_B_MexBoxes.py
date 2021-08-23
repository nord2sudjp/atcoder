# B

import collections
N,K=map(int,input().split())
*A,=list(map(int,input().split()))

# N,K=4,2
# A=[0,1,0,2]
# N,K=20,4
# A=[6, 2, 6, 8, 4, 5, 5, 8, 4, 1, 7, 8, 0, 3, 6, 1, 1, 8, 3, 0]
#A=sorted(A)
#print(A)

maxa=max(A)
DP=[]
c=(collections.Counter(A))

active=K
for i in range(maxa+1):
    t=c.get(i,-1) 
    if t==-1:
        DP.extend([i-1]*(active))
        break
    if active>t:
        DP.extend([i-1]*(active-t))
        active=t


if len(DP)<K:
    DP.extend([maxa]*(active))

ans=0
for d in DP:
        ans+=(d+1)
print(ans)