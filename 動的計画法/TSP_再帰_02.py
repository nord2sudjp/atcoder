N=5

MAX_N=N+1

D=[[0]*MAX_N for _ in range(MAX_N)]
DP=[[-1]*MAX_N for _ in range(2**MAX_N)]
# DP[S][v]: 現在vにいる。すでにSは訪れたことになっている。
# 残りのすべての頂点を訪れて0に戻るときのコスト

#print(2**5) # 32
#print(1<<5) # 32

def rec(S,v):
    if DP[S][v]>=0:
        # DP[S][v]!=-1の場合すでに計算されている
        return DP[S][v]

    if (S==(1<<N)-1 and v==0):
        # 1<<n  = 100000
        # 1<<n-1=  11111
        DP[S][v]=0
        return 0 # 現在0にいて、Sを回ってきたときに回るために必要なコスト=0
        
    res=float('infinity')
    for u in range(N):
        if not(S>>u & 1): # uが集合に含まれていない場合
            # uに移動する
            
            #print(S,v,u)

            res = min(res, rec(S|1<<u,u) + G[v][u])
            # num1 = 0b0101; bin(1<<3)
            # bin(num1 | 1<<3)
            # '0b1101'
    DP[S][v]=res
    return res

INF=float('infinity')
G=[[0,3,INF,4,INF],[INF,0,5,INF,INF],[4,INF,0,5,INF],[INF,INF,INF,0,3],[7,6,INF,INF,0]]

rec(0,0)
        