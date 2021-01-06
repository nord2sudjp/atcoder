N=int(input())
A=[]
for _ in range(N):
    A.append(list(map(int,input().split())))

b=[]

total=0
for a in A:
    b.append(a[0]*2+a[1])
    total+=a[0]
b=sorted(b, reverse=True)
#print(b,total)

ans=0
while 0<=total:
    total-=b[ans]
    ans+=1
print(ans)