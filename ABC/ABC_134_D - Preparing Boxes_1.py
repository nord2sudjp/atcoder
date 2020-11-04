N=int(input())
*A,=list(map(int,input().split()))
 
d=[-1]*(N+1)
d[0]=0
 
for i in range(N,0,-1):
 s=0
 for j in range(i+i,N+1,i):
  s^=d[j]
 d[i]=s^A[i-1]
 
print(sum(d))
for i in range(1,N+1):
 if d[i]: print(i)
