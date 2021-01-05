#
print(s)

l=len(s)
B=[0]*(l+1)
for i in range(0,l):
    B[i+1]=B[i]+s[i]
print(B)


#
def ruisekiwa(A):
    l=len(A)
    B=[0]*l
    for i in range(1,l):
        B[i]=a[i]+B[i-1]
    return B
ruisekiwa(list(range(0,9)))

