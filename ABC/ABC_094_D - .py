import bisect
import math


N=int(input())
*A,=sorted(map(int,input().split()))


a=A[-1]/2
l=bisect.bisect_left(A,a)

if abs(a-A[l-1])<=abs(a-A[l]):
    r=A[l-1]
else:
    r=A[l]

print(A[-1],r)