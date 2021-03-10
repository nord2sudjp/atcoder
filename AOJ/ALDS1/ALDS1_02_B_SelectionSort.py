# 2_B Selection Sort

def selectionsort(A):
    cnt=0
    l=len(A)
    for i in range(l):
        mini=i
        for j in range(i,l):
            if A[j]<A[mini]:
                mini=j
        A[i],A[mini]=A[mini],A[i]
        if mini!=i:cnt+=1

        #print(A)
    return (A,cnt)
N=int(input())
*A,=map(int,input().split())
ans,cnt=selectionsort(A)
print(' '.join(map(str,ans)))
print(cnt)