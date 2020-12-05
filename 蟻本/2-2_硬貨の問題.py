A=int(input())
*C,=map(int,input().split())
coin=[1,5,10,50,100,500]

ans=0

for i in range(5,-1,-1):
    t=min(A//coin[i],C[i])
    A-=t*coin[i]
    ans+=t
print(ans)