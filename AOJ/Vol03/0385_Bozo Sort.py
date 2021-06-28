# 0385 Bozo Sort
import sys

N=int(input())
*A,=list(map(int,input().split()))
Q=int(input())
input=sys.stdin.readlines()
#print(input)

# N=6
# A=[9, 7, 5, 6, 3, 1]
# Q=3
# xy=[[1,6],[2,5],[3,4]]

sorted_A=sorted(A)


diff=0
for i in range(N):
    if A[i]!=sorted_A[i]:
        diff=diff+1

if diff==0:
    print(0)
else:
    ans=-1
    for q in range(Q):
        x,y=map(int,input[q].split())
        x-=1
        y-=1
        A[x],A[y]=A[y],A[x]
        if A[x]==sorted_A[x] and A[y]!=sorted_A[x]:
            diff-=1
        if A[x]!=sorted_A[x] and A[y]==sorted_A[x]:
            diff+=1
        if A[y]==sorted_A[y] and A[x]!=sorted_A[y]:
            diff-=1
        if A[y]!=sorted_A[y] and A[x]==sorted_A[y]:
            diff+=1
        #print(diff,A)
        if diff==0:
            ans=q+1
            break
    print(ans)