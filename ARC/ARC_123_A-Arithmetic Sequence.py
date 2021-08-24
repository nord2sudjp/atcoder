# ARC123 Arithmetic Sequence - AC

i1=lambda : input()
i2=lambda : int(input())
i3=lambda : map(int,input().split())
i4=lambda : list(map(int,input().split()))
i5=lambda n : [list(map(int,input().split())) for _ in range(n)]
i6=lambda n : [list(input())for _ in range(n)]

*A,=i4()

X=A[1]*2-A[0]-A[2]

if X==0:
    ans=0
elif X<0:
    ans=abs(X//2)
    ans+=X%2
else:
    ans=X
print(ans)    