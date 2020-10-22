def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

factorization(24)

def improve(limit):
    n = 0
    for k in range(2, limit+1):
        factor = 0
        
        # 2�ȊO�̋����͑f���ł͂Ȃ��̂Ŗ�������
        if k % 2 == 0 and k != 2:
            continue
        
        # �J��Ԃ��̏���𔼕��ɂ���
        for divisor in range(2, k//2):
            if k % divisor == 0:
                factor += 1
                
        if factor == 0:
            n += 1
            
    return n
    
    
    
def s(l):
    n=0
    for k in range(2,l+1):
        f=0
        if k%2==0 and k!=2:continue
        for d in range(2, k//2):
            if k%d == 0:
                f+=1
        if f==0:
            n+=1
    return n