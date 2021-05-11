import bisect

def bisect_insert(A,t):
    index=bisect.bisect_left(A,t)
    A.insert(index,t)
    return A

def bisect_unique_insert(A,t):
    index=bisect.bisect_left(A,t)
    if len(A)==index or A[index]!=t:
        A.insert(index,t)
    return A

def bisect_slice(A,L,R):
    if len(A)==0:return []
    if R<L: return []
    index_l=bisect.bisect_left(A,L)
    index_r=bisect.bisect_left(A,R)
    if index_r<len(A) and A[index_r]==R:
        index_r+=1
    return A[index_l:index_r]



A=[1,2,3,5,8,10]

index=bisect.bisect_left(A,3)
print(index,A[index])

index=bisect.bisect_left(A,4)
print(index,A[index])

bisect_insert(A,4)
print(A)

bisect_unique_insert(A,4)
print(A)

A=[]
bisect_unique_insert(A,4)
print(A)

A=[10]
bisect_unique_insert(A,4)
print(A)

A=[10]
bisect_unique_insert(A,11)
print(A)


A=[1,2,3,5,8,10]
print(bisect_slice(A,3,8))
print(bisect_slice(A,3,9))
print(bisect_slice(A,4,8))
print(bisect_slice(A,4,9))
print(bisect_slice(A,-1,11))

print(bisect_slice(A,1,1))
print(bisect_slice(A,1,0))
print(bisect_slice(A,11,11))
print(bisect_slice(A,10,10))


A=[]
print(bisect_slice(A,3,8))

