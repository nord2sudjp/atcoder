# 024 - Select +^- One

N,K=map(int,input().split())

*A,=list(map(int,input().split()))
*B,=list(map(int,input().split()))

ans=0
for n in range(N):
    ans+=abs(A[n]-B[n])

if K<ans: # WA
    print('No')
else:
    print('Yes' if ans%2 == K%2 else "No")  
