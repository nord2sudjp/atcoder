#
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
