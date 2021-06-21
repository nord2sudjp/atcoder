# Volume0-0033 Ball

N=int(input())

for _ in range(N):
    *A,=list(map(int,input().split()))
    
    Q1=0
    Q2=0
    ans=True
    for i in range(10):
        if Q1<A[i]:
            Q1=A[i]
            continue
        if Q2<A[i]:
            Q2=A[i]
            continue
        ans=False
        break
    print('YES' if ans else 'NO')
