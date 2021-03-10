
def bubblesort(A):
    l=len(A)
    cnt=0
    for i in range(l):
        for j in range(l-1,i,-1):
            #print(i,j,A[j],A[j-1])
            if A[j]<A[j-1]:
                A[j],A[j-1]=A[j-1],A[j]
                cnt+=1
            #print(A)

    return (A,cnt)
N=int(input())
*A,=map(int,input().split())
ans,cnt=bubblesort(A)
print(' '.join(map(str,ans)))
print(cnt)