# D
# 最大値が大きい場合には番兵をDPの末端につけておき、そこに集約するようにする。

i1=lambda : input()
i2=lambda : int(input())
i3=lambda : map(int,input().split())
i4=lambda : list(map(int,input().split()))
i5=lambda n : [list(map(int,input().split())) for _ in range(n)]
i6=lambda n : [list(input())for _ in range(n)]


def fmt(DP):
    print("-"*10)
    for d in DP:
        print(d)
    
N=i2()
X,Y=i3()
O=[i4() for _ in range(N)]

# N=3
# X,Y=8,8
# O=[[3, 4], [2, 3], [2, 1]]

# N=3
# X,Y=3,5
# O=[[2, 1], [3, 4], [2, 3]]

MAXN=307
LIMN=MAXN-1
INF=float('inf')

def fmt(DP):
    print("-"*10)
    for i,s in enumerate(DP):
        print(i,s)

DP1=[[INF]*MAXN for _ in range(MAXN)]
DP2=[[INF]*MAXN for _ in range(MAXN)]

DP1[0][0]=0
for tako,tai in O:
    for i in range(MAXN):
        for j in range(MAXN):
            if DP1[i][j]!=INF:
                DP2[i][j]=min(DP1[i][j],DP2[i][j]) # お弁当を買わない
                
                # お弁当を買う
                n_tako=min(i+tako, MAXN-1)
                n_tai=min(j+tai, MAXN-1)
                DP2[n_tako][n_tai]=min(DP1[i][j]+1,DP2[n_tako][n_tai])
    DP1=DP2[:]
    #fmt(DP1)
    DP2=[[INF]*MAXN for _ in range(MAXN)]
    
ans=INF
for i in range(X,MAXN):
    for j in range(Y,MAXN):
        t=DP1[i][j]
        if t!=INF and t<=ans: 
            ans=t
print(-1 if ans==INF else ans)
    