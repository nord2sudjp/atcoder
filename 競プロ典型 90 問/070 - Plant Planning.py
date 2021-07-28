# 070 070 - Plant Planning
i1=lambda : input()
i2=lambda : int(input())
i3=lambda : map(int,input().split())
i4=lambda : list(map(int,input().split()))
i5=lambda n : [list(map(int,input().split())) for _ in range(n)]
i6=lambda n : [list(input())for _ in range(n)]

N=i2()

X=[]
Y=[]
for _ in range(N):
    x,y=i3()
    X.append(x)
    Y.append(y)

# N=2
# X=[-1,2]
# Y=[1,1]

X=sorted(X)
Y=sorted(Y)

if N%2!=0:
    middle=N//2
    mid_x=X[middle]
    mid_y=Y[middle]
else:
    middle=N//2
    mid_x=(X[middle]+X[middle-1])/2
    mid_y=(Y[middle]+Y[middle-1])/2


X=list(map(lambda x : abs(x-mid_x),X))
Y=list(map(lambda y : abs(y-mid_y),Y))

print(int(sum(X)+sum(Y)))