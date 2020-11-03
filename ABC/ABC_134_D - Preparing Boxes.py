N=int(input())
*A,=map(int,input().split())

d=[-1]*(N+1)

z=N//2+1
for i in range(N,0,-1):
    if z<=i:
        d[i]=A[i-1]
        continue
    t=2
    c=0
    while t*i<=N:
        #print(i,t*i,d[t*i])
        c+=d[t*i]
        t+=1
    c%=2
    d[i]=c^A[i-1]
    #print(i,c,A[i-1],c^A[i-1])

print(sum(d[1:]))
r=[]
for i in range(1,N+1):
    if d[i]==1: r.append(i)
print(' '.join(map(str,r)))