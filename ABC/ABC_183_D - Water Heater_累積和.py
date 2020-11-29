f=lambda:list(map(int,input().split()))
N,W=f()
u=[0]*(2*10**5+10)

maxp=0

for _ in range(N):
    s,p,t=f()
    u[s]+=t
    u[p]-=t
    maxp=max(p,maxp)

ans=True
for i in range(maxp+1):
    t+=u[i]
    if W<t:
        ans=False
        break
        
print('Yes' if ans else 'No')