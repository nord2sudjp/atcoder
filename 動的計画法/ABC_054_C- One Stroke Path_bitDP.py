f=lambda:map(int,input().split())
N,M=f()
 
A=[]
for i in range(M):
  a,b=f()
  A.append([a-1,b-1])
 
A=[*A,*[[y,x] for x,y in A]]
A=set(list(map(tuple,A)))
 
 
#N=3
#M=3
#A=[[1,2], [1, 3], [2, 3]]
 
 
def bit_dp(N,A):
    #print(A)
    dp = [[0]*N for i in range(1 << N)]
    #dp(S, v) = (頂点0から出発し、集合Sに含まれる頂点を全て訪れるpathのうち頂点vが最後になるようなpathの総数)
 
    dp[1][0] = 1     
    # dp({0}, 0) = 1 と初期化する
 
    for S in range(1 << N): # 1<<N=2**N
        for v in range(N):
            # v が S に含まれていないときはパスする
            if (S & (1 << v)) == 0:
                continue
 
            # sub = S - {v}
            sub = S ^ (1 << v) # vだけマスクする
 
            for u in range(N):
                # sub に u が含まれており、かつ u と v が辺で結ばれている
                if (sub & (1 << u)) and len(A&{(u,v)})==1:
                      #print(u,v,A&{(u,v)},dp[sub][u])          
                      dp[S][v] += dp[sub][u]
 
    ans = sum(dp[(1 << N) - 1][u] for u in range(1, N))
    # Σ dp({0,1,2,...,N-1},u))
    return ans
ans=bit_dp(N,A)
print(ans)    