N=int(input())
*A,=[0]+list(map(int,input().split()))

for i in range(N,0,-1):
 A[i]^=sum(A[i+i::i])%2

print(sum(A))
for i in range(1,N+1):
 if A[i]: print(i)