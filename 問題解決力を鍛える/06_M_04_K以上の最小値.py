# lowerbound‚Ì‰ğà https://qiita.com/kontotto/items/c718ec114b1532a2d159
# N=3, K=10, A=8 5 4, B=4 1 9
# ans=12

import bisect
N,K=map(int,input().split())
*A,=list(map(int,input().split()))
*B,=list(map(int,input().split()))

min_value=float('inf')

B=sorted(B)

for i in range(N):
    pos = bisect.bisect_left(B,K-A[i])
    min_value=min(min_value, A[i]+B[pos])
print(min_value)