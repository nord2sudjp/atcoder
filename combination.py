# https://atcoder.jp/contests/abc145/submissions/10775904
def comb(n,r,mod):
    # n+rからr通りを選択する
    k=min(r,n-r)
    C=1
    for i in range(1,k+1):
        C=(C*(n+1-i)*pow(i,mod-2,mod))%mod
    return C


# 
def comb_cal(n):
    s=1
    m=0
    for i in range(n):
        s*=2
        m+=s-1
        #print(s-1)
    return((s-1,m))

i,j=comb_cal(3)
print(i,j)


# CombinationのN
def cc(n):
    t=2**n-1
    return(t)

# CombinationのNまでの合計
def cc_a(n):
    t=2**n-1
    return(t+t-n)
