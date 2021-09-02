# 066 - Various Arraysiš5j 

N=int(input())
*P,=[list(map(int,input().split())) for _ in range(N)]

# N=2
# P=[[1,2],[1,2]]

total=1
for p in P:
    total=total*len(p)
#print(total)

ans=0
for i in range(N):
    for j in range(i+1,N):
        if i==j:continue
        p1=P[i]
        p2=P[j]
        total=(p1[1]-p1[0]+1)*(p2[1]-p2[0]+1)
        t=0
        for n1 in range(p1[0],p1[1]+1):
            for n2 in range(p2[0],p2[1]+1):
                if n1>n2:t=t+1
        ans=ans+(t/total)
print(ans)