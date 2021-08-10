i1=lambda : input()
i2=lambda : int(input())
i3=lambda : map(int,input().split())
i4=lambda : list(map(int,input().split()))
i5=lambda n : [list(map(int,input().split())) for _ in range(n)]
i6=lambda n : [list(input())for _ in range(n)]


def compress(N,V):
    mp={}
    for i in range(N):
        mp[V[i]]=0
    id=1
    k=list(mp.keys())
    k=sorted(k)
    for i in k:
        mp[i]=id
        id+=1
    for i in range(N):
        V[i]=mp[V[i]]
    return V

H,W,N=i3()
AB=i5(N)


# H,W,N=4,5,2
# AB=[[3, 2], [2, 5]]
# H,W,N=3,3,3
# AB=[[3,3],[1,2],[2,1]]

X=[0]*(N)
Y=[0]*(N)

for i in range(N):
    X[i]=AB[i][0]
    Y[i]=AB[i][1]


dx=compress(N,X)
dy=compress(N,Y)


# print(dx)
# print(dy)

for i,j in zip(dx,dy):
    print(i,j)