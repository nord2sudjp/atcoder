#N=int(input())
#S=input()

N=6
S='ACDBCB'
a=0
b=N-1
X=[]
while a<=b:
    left=False
    for i in range(b-a+1):
        if S[a+i]<S[b-i]:
            left=True # ���񂪒Ⴂ�̂ō�������Ƃ�
            break
        elif S[a+i]>S[b-i]:
            left=False # ���]��
            break
        #else:
            # ������������X�L�b�v����
    if left:
        X.append(S[a])
        a+=1
    else:
        X.append(S[b])
        b-=1
print(''.join(X))