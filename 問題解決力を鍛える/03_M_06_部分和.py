# bit‘S’Tõ‚ğ—˜—p
N,W=map(int,input().split())
*A,=map(int,input().split())

exist=False

for i in range(2**N):
    sum=0
    for j in range(N):
        if (i & (1<<j)):
            sum+=A[j]
    if (sum==W):
        exist=True
print('Yes' if exist else 'No')