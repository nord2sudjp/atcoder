def check(P):
    i=0
    for j in range(K):
        s=0
        while (s+T[i]<=P):
            s+=T[i]
            i+=1
            if i==N:return N
    return i


def solve():
    left=0
    right=100000 * 10000
    mid=0
    while (right-left>1):
        mid=(left+right)//2
        v=check(mid)
        if (v>=N) : 
            right=mid
        else:
            left=mid
    return right

N,K=map(int,input().split())
T=[int(input()) for _ in range(N)]
ans = solve()

print(ans)