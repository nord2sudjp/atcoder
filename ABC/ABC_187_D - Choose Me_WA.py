N=int(input())
A=[]
for _ in range(N):
    A.append(list(map(int,input().split())))


for a in A:
    #print(a,a[0]+a[1])
    a.append(a[0]+a[1])
#print(A)
A1=sorted(A, key=lambda x: (x[2],x[0]), reverse=True)
#print(A1)
l=len(A1)
sums=[0]*(l+1)
for i in range(l):
    sums[i+1]=sums[i]+A1[i][2]
#print(sums)

a_sums=[0]*(l+1)
a_sums[0]=sum(A1[i][0] for i in range(l))
for i in range(l):
    a_sums[i+1]=a_sums[i]-A1[i][0]
#print(a_sums)

ans=0
for u,v in zip(sums, a_sums):
    if v<u:break
    ans+=1
print(ans)