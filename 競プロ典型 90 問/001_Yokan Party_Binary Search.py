# 001 - Yokan Party

N,L=map(int,input().split())
K=int(input())
*A,=list(map(int,input().split()))

def divide(A, mid, K):
    l=len(A)
    i=0
    t=0
    #tdim=[]
    cnt=0
    while i<l:
        #print(A[i])
        t+=A[i]
        #tdim.append(A[i])
        if mid<=t:
            #print(t,tdim)
            t=0
            #tdim=[]
            cnt+=1
        if K<=cnt:break
        i+=1
    #print(i, A[i+1:])
    #print('Yes' if mid <= sum(A[i+1:]) else 'No') 
    return True if mid <= sum(A[i+1:]) else False


# N=3
# L=34
# K=1
# A=[8,13,26]
A.append(L)
Adiff=[]
prv=0
for a in A:
    Adiff.append(a-prv)
    prv=a
INF=1<<60
left=1
right=L

while right-left>1:
    #print(left,right)
    mid = (left+right)//2
    if divide(Adiff, mid, K):
        left=mid
    else:
        right=mid
print(left)