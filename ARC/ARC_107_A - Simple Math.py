A,B,C=map(int,input().split())

M=998244353

A%=M
B%=M
C%=M

print(A,B,C)


x=(A*(A+1)/2)%M
y=(B*(B+1)/2)%M
z=(C*(C+1)/2)%M

print(int((x*y*z)%M))