def f(I,W,A): # �ŏ���I�����I��ŁAW�ɂ��邱�Ƃ��ł��邩
    # f(0,W,A)�̏ꍇ�A0�����I�ׂȂ��̂ŁA�����͕K��False�ɂȂ�B
    if (I==0): # �Ō�܂őI�����I����Ă���
        if W==0: # �I���������ʂ�W�Ɠ�����
            return True
        else:
            return False
    
    # I-1��I������
    if f(I-1,W-A[I-1],A): return True
    
    # I-1��I�����Ȃ�
    if f(I-1,W,A): return True

    # ���̑�
    return False


N,W=map(int,input().split())
*A,=list(map(int,input().split()))

print(f(len(A), W,A))