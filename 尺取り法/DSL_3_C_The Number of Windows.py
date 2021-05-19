# O(n^2) version


def solve(N,S,A):
    ans=0
    for left in range(N):
        sum=0
        right=left
        while right<N and sum+A[right]<=S:
            sum = sum+A[right]
            right=right+1
        ans=ans+right-left  
    return ans

import sys

N,Q=map(int,input().split())

*A,=list(map(int,input().split()))
*X,=list(map(int,input().split()))

for x in X:
    print(solve(N,x,A))
    
    
# 標準的な尺取り法
def solve(N,S,A):
    ans=0
    right=0
    sum=0
    for left in range(N):
        while right<N and sum+A[right]<=S:
            sum = sum+A[right]
            right=right+1
        #print(right,left)
        ans=ans+right-left
        if right==left:
          right=right+1
        else:
          sum=sum-A[left]
    return ans

N,Q=map(int,input().split())

*A,=list(map(int,input().split()))
*X,=list(map(int,input().split()))

for x in X:
    print(solve(N,x,A))

# 標準的な尺取り法 whileの条件分岐をわかりやすくした
def solve(N,S,A):
    ans=0
    right=0
    sum=0
    for left in range(N):
        while right<N:
            t=sum+A[right]
            if t>S:break
            sum = sum+t
            right=right+1
        #print(right,left)
        ans=ans+right-left
        if right==left:
          right=right+1
        else:
          sum=sum-A[left]
    return ans

N,Q=map(int,input().split())

*A,=list(map(int,input().split()))
*X,=list(map(int,input().split()))

for x in X:
    print(solve(N,x,A))
    
# Backword
def solve(N,S,A):
    ans = 0
    left = 0
    sum = 0
    for right in range(N):
        sum = sum+A[right]
        while(sum > S):
            sum = sum-A[left]
            left += 1
        ans += (right-left+1) # leftに対する条件を満たすパターン数
    return ans

N,Q=map(int,input().split())

*A,=list(map(int,input().split()))
*X,=list(map(int,input().split()))

for x in X:
    print(solve(N,x,A))