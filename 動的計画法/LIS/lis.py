import bisect

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


A=[3,4,-1,5,8,2,3,12,7,9,10]
D=lis(A)
print(lis(A))
print(lis_fast(A))