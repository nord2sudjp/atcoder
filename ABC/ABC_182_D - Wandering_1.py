N=int(input())
*A,=map(int,input().split())

ans=0
s=b=mx_b=0
for i in range(N):
    b+=A[i] # i�i�ڂɂ����郰A�����߂�
    mx_b=max(mx_b,b)
    ans=max(ans, s+mx_b)
    s+=b # s�͎��̒i�̃X�^�[�g�A�����i�i�ڂɂ�����b���X�^�[�g�n�_�ɑ������l
    print(b,s)

print(ans)