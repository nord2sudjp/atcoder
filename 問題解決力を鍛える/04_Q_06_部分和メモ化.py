def f(I,W,A): # �ŏ���I�����I��ŁAW�ɂ��邱�Ƃ��ł��邩
    print(DP)
    # f(0,W,A)�̏ꍇ�A0�����I�ׂȂ��̂ŁA�����͕K��False�ɂȂ�B
    if (I==0): # �Ō�܂őI�����I����Ă���
        if W==0: # �I���������ʂ�W�Ɠ�����
            return True
        else:
            return False
    
    if DP[I][W]!=-1:return DP[I][W]
    
    # I-1��I������
    if f(I-1,W-A[I-1],A):
        DP[I][W]=True
        return True
    
    # I-1��I�����Ȃ�
    if f(I-1,W,A): 
        DP[I][W]=True
        return True

    # ���̑�
    DP[I][W]=False
    return False


N,W=map(int,input().split())
*A,=list(map(int,input().split()))

DP=[[-1]*(N+10) for _ in range(sum(A)+10)]
DP[0][0]=False
# �T�u�Z�b�g�ɑ΂��ēK�؂ȍ��v�l��W�����ł͂͂Ȃ��Ȃ�
# ����͈����Z����Ă�������
# �����DP[I]�����ł͂Ȃ肽���Ȃ��B

print(f(len(A), W,A))