# https://algo-logic.info/calc-pow/
def f_M(x,n,MOD):
    ret = 1
    while n > 0:
        if n&1:
            ret = ret * x % MOD #n ‚ÌÅ‰ºˆÊbit‚ª 1 ‚È‚ç‚Î x^(2^i) ‚ğ‚©‚¯‚é
        x = x * x % MOD
        n >>= 1 #n ‚ğ1bit ¶‚É‚¸‚ç‚·
    return ret

# https://qiita.com/b1ueskydragon/items/0b8e0c382d782423c6d3
def pow_k(x, n):
    if n == 0:
        return 1

    K = 1
    while n > 1:
        if n % 2 != 0:
            K *= x
        x *= x
        n //= 2

    return K * x
    