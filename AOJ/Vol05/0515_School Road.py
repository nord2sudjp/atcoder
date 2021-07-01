    
# M=5
# N=4
# K=set(((2,2),(2,3),(4,2)))

while True:
    M,N=map(int,input().split())
    if M==N==0:break
    Q=int(input())
    
    k=[]
    for _ in range(Q):
        k.append(tuple(map(int,input().split())))
    K=set(k)


    DP=[[0]*(N+1) for _ in range(M+1)]
    DP[1][1]=1

    for m in range(1,M+1):
        for n in range(1,N+1):
            if (m,n) in K:continue
            DP[m][n]=DP[m][n]+DP[m-1][n]
            DP[m][n]=DP[m][n]+DP[m][n-1]
    print(DP[M][N])
