# https://algo-logic.info/calc-pow/
def f_M(x,n,MOD):
    ret = 1
    while n > 0:
        if n&1:
            ret = ret * x % MOD #n �̍ŉ���bit�� 1 �Ȃ�� x^(2^i) ��������
        x = x * x % MOD
        n >>= 1 #n ��1bit ���ɂ��炷
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
    