N=int(input())

d={}
for i in range(1,N+1):
    s=str(i)
    t=(int(s[0]), int(s[-1]))
    d[t]=d.get(t, 0)+1
ans=0

for i in d:
    j=(i[1],i[0])
    ans+=d.get(i,0)*d.get(j,0)
print(ans)