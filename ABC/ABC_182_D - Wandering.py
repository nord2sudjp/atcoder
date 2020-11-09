N=int(input())
*A,=map(int,input().split())

l=len(A)
B=[0]*(l+1)
C=[0]*(l+1)

c=0
for i in range(l):
   c+=A[i]
   B[i+1]=c
   C[i+1]=C[i]+c

# C=jÇ∆Ç∑ÇÈÇ∆B=0Å`j+1

mc=0
mb=max(B[:2])
for i in range(1,l):
    mb=max(mb,B[i+1])
    s=C[i]+mb
    mc=max(mc,s)

print(max(mc,C[-1]))