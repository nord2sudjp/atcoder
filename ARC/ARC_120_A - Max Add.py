N=int(input())
*A,=list(map(int,input().split()))


# N=3
# A=[1,2,3]

ans=0
m=0
buf=0

for i in range(0,N):
    if m<A[i]:
        m=A[i]
    buf=buf+A[i]
    ans=ans+buf
    print(ans+(i+1)*m)
