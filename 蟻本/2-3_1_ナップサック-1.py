f=lambda:map(int,input().split())
#N,W=f()
#*S,=f()
#*V,=f()

N=4
W=5
S=[2,1,3,2]
V=[3,2,4,2]

def rec(i,j): 
    # i=�g�p�����ו�(�����l=0,����i<N)
    # j=���p�ł���d��(�����l=W, ����0<=j)
    r=0
    if (i==N): # �ו��͂Ȃ�
        r=0
    elif j<S[i]: # ���̉ו��͓���Ȃ�
        r=rec(i+1,j)
    else:
        r=max(rec(i+1,j), rec(i+1,j-S[i])+V[i])
    return(r)
print(rec(0,W))