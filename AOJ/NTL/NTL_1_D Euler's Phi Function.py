def euler_phi(n):
    res = n
    x = 2
    while x*x <= n: # x**2がnより低いxについて
        if n % x == 0: # nがxで割り切れる場合には除外する
            res = res // x * (x-1)
            while n % x == 0: # 素因数分解でxについてreduceしていく 例) 12=2**3*3のとき2**3を消し込む
                n //= x
        x += 1
    if n > 1:
        res = res // n * (n-1)
    return res


print(euler_phi(int(input())))