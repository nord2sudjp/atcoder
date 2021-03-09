# https://szarny.hatenablog.com/entry/2017/09/21/232855#%E3%82%BD%E3%83%BC%E3%82%B9%E3%82%B3%E3%83%BC%E3%83%89-4
import math
def s(k):
    f=0
    if k%2==0 and k!=2:return False
    limit=math.floor(math.sqrt(k))+1
    for d in range(2, l):
        if k%d == 0:return False
    return True

# https://szarny.hatenablog.com/entry/2017/09/21/232855#%E3%82%BD%E3%83%BC%E3%82%B9%E3%82%B3%E3%83%BC%E3%83%89-4
# AOJ‚ÅTLE
def s(k):
    f=0
    if k%2==0 and k!=2:return False
    for d in range(2, k//2):
        if k%d == 0:return False
    return True


#
a=[True]*n
a[0]=False
a[1]=False
for i in range(2,n):
    if a[i]:
        for j in range(i*2,n,i):
            a[j]=False
