N=int(input())
*A,=map(int,input().split())

fl=1
x=0
for a in A:
    x+=fl*a
    fl*=-1

print(x)
for i in range(N-1):
    x=2*A[i]-x
    print(x)