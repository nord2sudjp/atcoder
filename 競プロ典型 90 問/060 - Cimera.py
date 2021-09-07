# 060 - Chimera

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