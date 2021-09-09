# 060 - Chimera - AC

N=int(input())
*A,=list(map(int,input().split()))

import bisect

# N=6
# A=[1, 2, 3, 3, 2, 1]


def lis_fast(S):
    INF=float('inf')
    N=len(S)
    DP=[INF]*(N)
    R=[-1]*(N)


    DP[0]=S[0]

    R[0]=1
    for i in range(1,N):
        pos=bisect.bisect_left(DP,S[i])
        #print(i,S[i],pos,DP)
        DP[pos]=S[i]
        R[i]=pos+1
    return R


dp_l=lis_fast(A)
dp_r=lis_fast(A[::-1])[::-1]

#print(dp_l,dp_r)

ans=0
for l,r in zip(dp_l,dp_r):
    #print(l,r,l+r-1)
    t=l+r-1
    if t>ans:
        ans=t
print(ans)


# 060 - Chimera - TLE

N=int(input())
*A,=list(map(int,input().split()))


# N=6
# A=[1, 2, 3, 3, 2, 1]

def lis(S):
    N=len(S)
    DP=[1]*N
    for i in range(1,N):
        for j in range(0,i):
            if S[j]<S[i]:
                #print(S[j],S[i])
                #DP[i]=max(DP[i], DP[j]+1)
                nnp=DP[j]+1
                if DP[i]<nnp:
                    DP[i]=nnp
    #print(N-max(DP))
    return DP

dp_l=lis(A)
dp_r=lis(A[::-1])[::-1]
    
ans=0
for l,r in zip(dp_l,dp_r):
    #print(l,r,l+r-1)
    t=l+r-1 # overlap
    if t>ans:
        ans=t
print(ans)