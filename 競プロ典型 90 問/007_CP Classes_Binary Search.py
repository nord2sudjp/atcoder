#https://atcoder.jp/contests/typical90/submissions/22166460

import bisect
 
N=int(input())
*A,=map(int,input().split())
 
A=sorted(A)
 
Q=int(input())
 
l=len(A)
ans=[]
amin=A[0]
amax=A[-1]
for _ in range(Q):
    b=int(input())
    if b<amin:
      ans.append(amin-b)
    elif amax<b:
      ans.append(b-amax)
    else:
      i=bisect.bisect_left(A,b)
      # print(A[i-1],A[i])
      t1=abs(b-A[i-1])
      t2=abs(b-A[i])
      if t1<t2:
        ans.append(t1)
      else:
        ans.append(t2)
 
for a in ans:
    print(a)