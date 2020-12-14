N=int(input())
*A,=sorted(map(int,input().split()))

l=len(A)
amax=A[-1]
DP=[0]*(amax+1)
         
for a in A:

    if DP[a]!=0:
        DP[a]+=1 # DP[a]=2‚Å‚æ‚¢
        continue # continue‚ÅØ‚é
    #else:
        #t=a
        #while t<=amax:
    for t in range(a,amax+1,a): # for‚ğ—˜—p‚·‚é
        #print(a, t)
        DP[t]+=1
        #t+=a
            
cnt=0
for a in A:
    if DP[a]==1:
        #print(a)
        cnt+=1
print(cnt)