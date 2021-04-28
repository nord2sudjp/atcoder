import bisect
N=int(input())
S=[int(input()) for _ in range(N)]

DP=[]
ans=0
R=[0]*N

DP.append(S[0])

for i in range(1,N):
    if DP[ans]<S[i]:
        ans+=1
        DP.append(S[i])
        R[i]=ans
    else:
        DP[bisect.bisect_left(DP, S[i])] = S[i]
print(N-len(DP))