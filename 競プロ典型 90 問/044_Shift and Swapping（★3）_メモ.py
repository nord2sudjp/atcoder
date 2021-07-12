# 044 - Shift and Swapping
import sys

N,Q=map(int,input().split())
*A,=list(map(int,input().split()))
lenA=len(A)
start=0
#T=sys.stdin.readlines()
#for i in T:
for i in range(Q):
    t=input().split()
    #t=T[i].split()
    q=t[0]
    if q=="1":
        l=int(t[1])-start-1
        if l<-lenA:l%=-lenA
    
        r=int(t[2])-start-1
        if r<-lenA:r%=-lenA

        A[l],A[r]=A[r],A[l]
    elif q=="2":
        start=start+1
    else:
        index=int(t[1])-start-1
        if index<-lenA:index%=-lenA
        print(A[index])
    #print(start,A)