# 0360 Reservation System
a,b=map(int,input().split())
N=int(input())
SF=[list(map(int,input().split())) for _ in range(N)]

# a=5
# b=7
# N=3
# SF=[[1, 4], [4, 5], [7, 10]]

MAXD=1007
D1=[0]*MAXD
D2=[0]*MAXD


for s,f in SF:
    D1[s]+=1
    D1[f]-=1
#print(D1)    

prv=0
for i in range(MAXD-1):
    D2[i]=prv+D1[i]
    prv=D2[i]
#print(D2)

print(1 if sum(D2[a:b])>0 else 0)