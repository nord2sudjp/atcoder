# 055 - Select 5
# N,P,Q=map(int,input().split())
# *A,=list(map(int,input().split()))
 
# N=6
# P=7
# Q=1
# A=[1, 2, 3, 4, 5, 6]
 
import numpy as np
 
from numba import jit
@jit("i8(i8,i8,i8,i8[:])",nopython=True) 
def solve(N,P,Q,A):
    ans=0
    for i1 in range(N):
        q=A[i1]%P
        for i2 in range(i1+1,N):
            r=q*A[i2]%P
            for i3 in range(i2+1,N):
                s=r*A[i3]%P
                for i4 in range(i3+1,N):
                    t=s*A[i4]%P
                    for i5 in range(i4+1,N):
                        ans=ans+(t*A[i5]%P==Q)
                            
    return ans
 
def main():
    N,P,Q=map(int,input().split())
    *T,=list(map(int,input().split()))
    A = np.array(T)
    print(solve(N,P,Q,A))
if __name__ == "__main__":
    main()