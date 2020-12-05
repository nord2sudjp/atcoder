f=lambda:map(int,input().split())
#N,W=f()
#*S,=f()
#*V,=f()

N=4
W=5
S=[2,1,3,2]
V=[3,2,4,2]

dp=[[-1]*(W+1) for _ in range(N+1)]

def rec(i,j): 
    if 0<=dp[i][j]: return(dp[i][j])
    # i=使用した荷物(初期値=0,条件i<N)
    # j=利用できる重量(初期値=W, 条件0<=j)
    r=0
    if (i==N): # 荷物はない
        r=0
    elif j<S[i]: # この荷物は入らない
        r=rec(i+1,j)
    else:
        r=max(rec(i+1,j), rec(i+1,j-S[i])+V[i])
    dp[i][j]=r
    return(r)
print(rec(0,W))