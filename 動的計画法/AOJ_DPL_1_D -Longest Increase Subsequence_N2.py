N=int(input())
S=[int(input()) for _ in range(N)]

l=len(S)

DP=[1]*l
ans=0

for i in range(1,N):
    for j in range(i):
        #print(j,i)
        if S[j]<S[i]:
            DP[i]=max(DP[i],DP[j]+1)
    ans=max(ans,DP[i])        
print(ans)