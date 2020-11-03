f=lambda:map(int,input().split())
N,H=f()
x=0

B=[0]*N
for i in range(N):
    a,b=f()
    x=max(a,x)
    B[i]=b

B.sort(reverse=1)
R=10**10

for i in range(N+1):
    if i>0: H-=B[i-1]
    z=0
    if 0<H: z=-(-H//x)
    R=min(R,i+z)
  
print(R)
