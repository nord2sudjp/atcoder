# ARC123 Arithmetic Sequence - WA

i1=lambda : input()
i2=lambda : int(input())
i3=lambda : map(int,input().split())
i4=lambda : list(map(int,input().split()))
i5=lambda n : [list(map(int,input().split())) for _ in range(n)]
i6=lambda n : [list(input())for _ in range(n)]

*A,=i4()

if A[1]*2-A[0]-A[2]==0:
    print(0)
elif A[0]==A[1]==A[2]:
    print(0)
elif A[0]==A[2]:
    if A[0]>A[1]:
        print(A[0]-A[1])
    else:
        print((A[1]-A[0])*2)
elif A[1]==A[0] or A[1]==A[2]:
    print(abs(A[1]-A[2]+A[1]-A[0]))
else:
    ans=0
    if A[-1]<A[0]:
        A=A[::-1]
    if A[2]>=A[1]:
        t=(A[0]+A[2])//2
        if t>A[1]:
            ans+=t-A[1]
            A[1]=t
        ans+=abs(A[1]*2-A[0]-A[2])
    else:
        ans=abs(A[1]-A[2]+A[1]-A[0])
    print(ans)