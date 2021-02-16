#N=6
#M=[[30,35],[35,15],[15,5],[5,10],[10,20],[20,25]]

#N=5
#M=[[5,4],[4,6],[6,2],[2,7]]

N=int(input())
M=[map(int,input().split()) for _@in range(N)]

P=[a for a,b in M]
P.append(M[-1][-1])

N1=N+1

DP=[[0]*N1 for _ in range(N1)]
S=[[0]*N1 for _ in range(N1)]


for d in range(1,N1): # difference
    for i in range(1,N1-d): # start
        j=i+d # end
        mvalue=float('infinity')
        for k in range(i,j): # ‹æØ‚éˆÊ’u
            #print(i,d+i,k)
            q=DP[i][k]+DP[k+1][j]+P[i-1]*P[k]*P[j]
            if (q<mvalue):
                mvalue=q
                S[i][j]=k
        DP[i][j]=mvalue

#for d in DP:
#    print(d)
        
print(DP[1][N1-1])