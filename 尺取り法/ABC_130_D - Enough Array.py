f=lambda:map(int,input().split())
N,K=f()
*A,=f()
        
c=i=t=0
for a in range(N):
    while i<N and t<K:
        t+=A[i]
        i+=1
    #print(A[a],i,K,t)

    if K<=t:
        c+=N-(i-1)
    t-=A[a]
    #print(i,t)

print(c)