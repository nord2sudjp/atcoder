N=int(input())
*A,=map(int,input().split())

c=len([a for a in A if a<0])

for i in range(N):
  if A[i]<0:A[i]*=-1

if c%2==0:
    print(sum(A))
else:
    print(sum(A)-min(A)*2)