def f_M(x,n,MOD):
    ret = 1
    while n > 0:
        if n&1:
            ret = ret * x % MOD #n の最下位bitが 1 ならば x^(2^i) をかける
        x = x * x % MOD
        n >>= 1 #n を1bit 左にずらす
    return ret

MOD=1000000007
m,n=map(int,input().split())
print(f_M(m,n,MOD))