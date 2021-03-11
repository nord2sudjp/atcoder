# D
# nHr=(n+r-1)Cr

N=int(input())
K=int(input())

def comb(n,r,mod):
    k=min(r,n-r)
    C=1
    for i in range(1,k+1):
        C=(C*(n+1-i)*pow(i,mod-2,mod))%mod
    return C

P=10**9+7
print(comb(N+K-1,K,P))