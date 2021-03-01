def f_M(x,n,MOD):
    ret = 1
    while n > 0:
        if n&1:
            ret = ret * x % MOD #n ‚ÌÅ‰ºˆÊbit‚ª 1 ‚È‚ç‚Î x^(2^i) ‚ğ‚©‚¯‚é
        x = x * x % MOD
        n >>= 1 #n ‚ğ1bit ¶‚É‚¸‚ç‚·
    return ret

MOD=1000000007
m,n=map(int,input().split())
print(f_M(m,n,MOD))