N=int(input())
*A,=list(map(int,input().split()))

m=[0]*(N+1)
for i in range(N):
   m[i+1]=m[i]+A[i]

#print(m)
for k in range(1,N+1):
    ans=0
    for j in range(0,N+1-k): 
        # N+1‚Ím‚Ì’·‚³
        #j+k<N => #j<N-k ‚æ‚Á‚Ä range(N-k+1)
        #print(k,j,j+k,m[j+k]-m[j])
        ans=max(ans,m[j+k]-m[j])
    print(ans)