def f_M(x,n,MOD):
    ret = 1
    while n > 0:
        if n&1:
            ret = ret * x % MOD #n �̍ŉ���bit�� 1 �Ȃ�� x^(2^i) ��������
        x = x * x % MOD
        n >>= 1 #n ��1bit ���ɂ��炷
    return ret

MOD=1000000007
m,n=map(int,input().split())
print(f_M(m,n,MOD))