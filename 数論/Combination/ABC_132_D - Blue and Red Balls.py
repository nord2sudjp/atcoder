mod=10**9+7
N,K=map(int,input().split())

def comb(n,r,mod):
    if n<r:return 0
    k=min(r,n-r)
    C=1
    for i in range(1,k+1):
        C=(C*(n+1-i)*pow(i,mod-2,mod))%mod
    return C

for i in range(1,K+1):
    #print(cmb(N-K+1, i),cmb(K-1,i-1))
    print((comb(N-K+1, i, mod)*comb(K-1,i-1,mod))%mod)