N=int(input())
f=lambda:sorted(map(int,input().split()))
*A,=f()
*B,=f()
*C,=f()
from bisect import *
print(sum(bisect_left(A,b)*(N-bisect_right(C,b))for b in B))