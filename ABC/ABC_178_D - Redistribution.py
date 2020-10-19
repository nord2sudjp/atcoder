from operator import mul
from functools import reduce
 
def cc(n, r):
    r = min(r, n - r)
    numer = reduce(mul, range(n, n - r, -1), 1)
    denom = reduce(mul, range(1, r + 1), 1)
    return numer // denom
 
def c(n, r):
    return cc(n + r - 1, r)
 
 
S=int(input())
maxl=S//3
 
a=0
for i in range(1,maxl+1):
    a+=c(i,S-3*i)%(10**9+7)
    # print(c(i,S-3*i))
print(a%(10**9+7))
