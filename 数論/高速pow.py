# https://algo-logic.info/calc-pow/
def f_M(x,n,MOD):
    ret = 1
    while n > 0:
        if n&1:
            ret = ret * x % MOD #n ‚ÌÅ‰ºˆÊbit‚ª 1 ‚È‚ç‚Î x^(2^i) ‚ğ‚©‚¯‚é
        x = x * x % MOD
        n >>= 1 #n ‚ğ1bit ¶‚É‚¸‚ç‚·
    return ret

def f(x,n,M):
    ret = 1
    while n > 0:
        if n&1:
            ret *= x  #n ‚ÌÅ‰ºˆÊbit‚ª 1 ‚È‚ç‚Î x^(2^i) ‚ğ‚©‚¯‚é
        x *= x
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


#
def f(n,M):
    if n==0:return 1
    elif n%2==0:
        x=f(n/2,M)
        x*=x
        return x%M
    else:
        x=f((n-1)/2,M)
        x*=x*2
        return x%M


for i in range(1,100):
    print(f(i,10**9+7),pow(2,i,10**9+7))
    
    