N=int(input())
*A,=list(map(int,input().split()))


l=len(A)
for i in range(1,l):
    print(' '.join(map(str,A)))
    key=A[i] # key�̓\�[�g����Ă��Ȃ��l
    j=i-1 # �\�[�g����Ă���z��̍Ō��
    while j>=0 and A[j] > key: 
        # ���łɃ\�[�g����Ă���z���0..i-1
        # �l���傫���ꍇ�ɂ͂��炵�Ă���
        A[j+1] = A[j]
        # �ŏ���j=i-1�ł���
        # ���炵�Ă���
        j-=1
    A[j+1]=key
        # ���炵�I������key��ݒ�
print(' '.join(map(str,A)))
