def euler_phi(n):
    res = n
    x = 2
    while x*x <= n: # x**2��n���Ⴂx�ɂ���
        if n % x == 0: # n��x�Ŋ���؂��ꍇ�ɂ͏��O����
            res = res // x * (x-1)
            while n % x == 0: # �f����������x�ɂ���reduce���Ă��� ��) 12=2**3*3�̂Ƃ�2**3����������
                n //= x
        x += 1
    if n > 1:
        res = res // n * (n-1)
    return res


print(euler_phi(int(input())))