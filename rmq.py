import math

def prep(A):
    N=len(A)
    sparse=[[0]*int(math.log2(N)+1) for _ in range(N)]
    for i in range(N):
        sparse[i][0]=i
    
    j=1
    while 2**j<=N:
        i=0
        while i+2**j-1<N:
            if A[sparse[i][j-1]]<A[sparse[i+2**(j-1)][j-1]]:
                sparse[i][j]=sparse[i][j-1]
            else:
                sparse[i][j]=sparse[i+2**(j-1)][j-1]
            i+=1
        j+=1
    return sparse


def rmq(low,high,A,sparse):
    l=high-low
    k=int(math.log2(l))
    return min(A[sparse[low][k]], A[sparse[low+l-2**k][k]])





A = [7, 2, 3, 0, 5, 10, 3, 12, 18]
sparse=prep(A)

print(rmq(0, 4, A,sparse))
print(rmq(4, 7,A,sparse))
print(rmq(7, 8,A,sparse))
