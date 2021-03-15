import sys
input = sys.stdin.readline
N,M,Q=map(int,input().split())
LR=[list(map(int,input().split())) for _ in range(M)]
PQ=[list(map(int,input().split())) for _ in range(Q)]


DP_1=[[0]*(N+1) for _ in range(N+1)]
DP_R=[[0]*(N+1)]

for l,r in LR:
    DP_1[l][r]+=1
# print(DP_1)

for row in range(1,N+1):
    #print(DP_1[row])
    m=[0]*(N+1)
    for col in range(N):
        m[col+1]=m[col]+DP_R[-1][col+1]-DP_R[-1][col]+DP_1[row][col+1]
    DP_R.append(m)     
#print(DP_R)

def f(pos):
    pl=pos[0]
    pr=pos[1]
    pt=pos[0]
    pb=pos[1]
 
    base=DP_R[pb][pr]
    x1=DP_R[pt-1][pr]
    x2=DP_R[pb][pl-1]
    x3=DP_R[pt-1][pl-1]
    ans=base-x1-x2+x3
    print(ans)

for k in PQ:
    f(k)