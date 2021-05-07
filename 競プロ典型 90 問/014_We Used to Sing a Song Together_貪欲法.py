# 014 - We Used to Sing a Song Together
# https://atcoder.jp/contests/typical90/submissions/22166780

N=int(input())
 
*A,=list(map(int,input().split()))
*B,=list(map(int,input().split()))
 
A=sorted(A)
B=sorted(B)
 
ans=0
for a,b in zip(A,B):
    ans=ans+abs(a-b)
print(ans)