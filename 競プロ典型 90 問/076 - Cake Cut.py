# 076 - Cake Cut�i��3�j

def solve():
    A.extend(A)
    C=[0]
    for i in range(N*2):
        C.append(C[i]+A[i])
    C.append(C[-1]+A[0])
    target=s//10
    l_C=len(C)
    
    for i in range(N+1): # A�̍Ō�܂ŏ�������΂悢�B
        res=C[i]
        for j in range(i+1,l_C): # left�Œ肾����Atarget>�ɂȂ����甲����΂悢�B
            if C[j]-C[i]<target:continue
            break
        if C[j]-C[i] == target:
            print('Yes')
            return
    print('No')
    return

N=int(input())
*A,=list(map(int,input().split()))

# N=4
# A=[1, 3, 7, 9]

C=[0]

s=sum(A)
if s%10!=0:
    print('No')
else:
    solve()
