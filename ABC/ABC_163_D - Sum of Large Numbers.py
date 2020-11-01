N,K=map(int,input().split())

M=10**9+7

A=range(N+1)
l=len(A)

c=0
for i in range(K,l+1):
    # l=sum(A[0:i])
    # print(l,i,(i-1)*i/2,A[0:i])
    l=(i-1)*i//2
    #r=sum(A[-1:-i-1:-1])
    #print(r,i,(A[-1]+A[-i])*i/2,list(A[-1:-i-1:-1]))
    r=(A[-1]+A[-i])*i//2
    c+=r-l+1
    c%M
print(c%M)