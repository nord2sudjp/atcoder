#https://atcoder.jp/contests/abc134/submissions/10585550

N=int(input())
*A,=[0]+list(map(int,input().split()))

d=[-1]*(N+1)
d[0]=0

for i in range(N,0,-1):
 d[i]=sum(d[i+i::i])%2^A[i]

print(sum(d))
for i in range(1,N+1):
 if d[i]: print(i)