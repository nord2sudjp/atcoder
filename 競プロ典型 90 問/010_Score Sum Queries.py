# 010 - Score Sum Queries

# N=7

N=int(input())

A=[0]*(N+1)
B=[0]*(N+1)
for i in range(N):
    c,p=map(int,input().split())
    if c==1:
        A[i+1]=p
    else:
        B[i+1]=p

# print(A)
# print(B)

# A=[0, 72, 0, 0, 23, 0, 40, 75]
# B=[0, 0, 78, 94, 0, 89, 0, 0]

AS=[0]*(N+1)
BS=[0]*(N+1)

for i in range(N+1):
    AS[i]=AS[i-1]+A[i]
    BS[i]=BS[i-1]+B[i]
    
# print(AS)
# print(BS)

# Q=1
Q=int(input())

for _ in range(Q):
    l,r=map(int,input().split())
    a=AS[r]-AS[l-1]
    b=BS[r]-BS[l-1]
    print(a,b)