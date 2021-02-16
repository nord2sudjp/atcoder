#https://www.youtube.com/watch?v=eKkXU3uu2zk

N=5
M=[[5,4],[4,6],[6,2],[2,7]]

P=[a for a,b in M]
P.append(M[-1][-1])

print(P)

DP=[[0]*N for _ in range(N)]
S=[[0]*N for _ in range(N)]


for d in range(1,N-1): # difference
    for i in range(1,N-d): # start
        j=i+d # end
        mvalue=float('infinity')
        for k in range(i,j): # ‹æØ‚éˆÊ’u
            #print(i,d+i,k)
            q=DP[i][k]+DP[k+1][j]+P[i-1]*P[k]*P[j]
            if (q<mvalue):
                mvalue=q
                S[i][j]=k
        DP[i][j]=mvalue
print(DP)
print(DP[1][N-1])