N=int(input())
*A,=map(int,input().split())
Q=int(input())
*M,=map(int,input().split())
mf=['no']*Q
t=[]
for i in range(0,2**N):
    ans=0
    for j in range(N):
        if (i>>j&1):
            ans+=A[j]
    t.append(ans)
tset=set(t)

for i in range(Q):
    if M[i] in tset:
        mf[i] = 'yes'

for i in mf:
    print(i)