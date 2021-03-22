MAX=500000
SENTINEL=2*10**10
cnt=0

L=[0]*MAX
R=[0]*MAX

def merge(A, n, left, mid, right):
    global cnt
    n1 = mid - left
    n2 = right - mid
    #L=[0]*(n1+1)
    #R=[0]*(n2+1)
    L[n1]=R[n2]=SENTINEL
    L[:n1]=A[left:left+n1]
    R[:n2]=A[mid:mid+n2]
#     for i in range(n1):
#         L[i] = A[left + i]
#     for i in range(n2):
#         R[i] = A[mid + i]
    L[n1] = SENTINEL
    R[n2] = SENTINEL
    i = 0;
    j = 0;
    for k in range(left,right):
        cnt+=1
        if L[i] <= R[j]:
            A[k] = L[i]
            i=i+1
        else:
            A[k] = R[j]
            j=j+1

def mergesort(A, n,left, right):
    if left+1 < right:
        mid = (left + right)//2
        mergesort(A, n,left, mid)
        mergesort(A, n,mid, right)
        merge(A, n,left, mid, right)
    
#A=[0]*MAX


import sys
input = sys.stdin.readline
N=int(input())
*A,=map(int,input().split())
# N=10
# A=[8, 5, 9, 2, 6, 3, 7, 1, 10, 4]

mergesort(A,N,0,N)

print(' '.join(map(str,A)))
print(cnt)