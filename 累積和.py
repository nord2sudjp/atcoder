def ruisekiwa(A):
    l=len(A)
    B=[0]*l
    for i in range(1,l):
        B[i]=a[i]+B[i-1]
    return B
ruisekiwa(list(range(0,9)))