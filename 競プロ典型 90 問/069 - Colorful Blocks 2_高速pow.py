# 069 - Colorful Blocks 2

def f_M(x,n,MOD):
    ret = 1
    while n > 0:
        if n&1:
            ret = ret * x % MOD #n �̍ŉ���bit�� 1 �Ȃ�� x^(2^i) ��������
        x = x * x % MOD
        n >>= 1 #n ��1bit ���ɂ��炷
    return ret

N,K=map(int,input().split())
MOD=10**9+7

if N==1:
    print(K%MOD)
elif N==2:
    print(K*(K-1)%MOD)
else:
    
    ans=1
    for i in range(3):
        ans=(ans*K)%MOD
        K-=1

    K+=1
    print(ans*f_M(K,(N-3),MOD)%MOD)

