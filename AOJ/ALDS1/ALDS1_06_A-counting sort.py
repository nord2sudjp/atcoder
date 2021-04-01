# 6_A Counting sort

def cs(A,k):
    c=[0]*(k+1)
    a_l=len(A)
    for j in range(a_l):
        c[A[j]] = c[A[j]]+1
    #print(c)
    
    for i in range(1,k+1):
        c[i]=c[i]+c[i-1]
    #print(c)
    
    B=[0]*a_l
    
    for j in range(a_l-1,-1,-1):
        #print(j,A[j],c[A[j]],B)
        B[c[A[j]]-1] = A[j]
        c[A[j]]-=1
        #print(j,A[j],c[A[j]],B)
    return B

N=int(input())
*A,=list(map(int,input().split()))
         
print(' '.join(map(str,cs(A,max(A)))))