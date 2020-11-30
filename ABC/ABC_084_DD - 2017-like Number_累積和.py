n=100003
Q=int(input())

p=[1]*(n)
d=[0]*(n)

p[0]=0
p[1]=0
for i in range(2,n):
    if p[i]:
        for j in range(i*2,n,i):
            p[j]=False

c=0
for i in range(1,n):
   if p[i] and p[(i+1)//2]:c+=1
   d[i]=c

for _ in range(Q):
    l,r=map(int,input().split())
    print(d[r]-d[l-1])