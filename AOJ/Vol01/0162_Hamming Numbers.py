# 0162 Hamming Numbers

# M=3
# N=8

while True:
    t=list(map(int,input().split()))
    if len(t)==1:break
    
    M,N=t
    MAXN=N+7
    DP=[0]*(MAXN)
    DP[1]=1
    DP[2]=1
    DP[3]=1
    DP[5]=1

    for i in range(1,MAXN):

        if DP[i]==1:
            if i*2 >= MAXN:continue
            DP[i*2]=1
            if i*3 >= MAXN:continue
            DP[i*3]=1
            if i*5 >= MAXN:continue
            DP[i*5]=1
    print(sum(DP[M:N+1]))