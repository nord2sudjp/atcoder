# 0642 Sugoroku

# 1��A���ő��₵�Ă��������ɕK�v�ȑo�Z���ǂ̂悤�ɕω����邩������΂悢�B
# 0���A�����Ă���Ƃ���͕K������l, �� 1�Ői��ł����΂悢�̂Ő�������͂Ȃ�

# �R�[�i�[�P�[�X
# ���ׂ�0

# N=10
# A=[0,1,1,0,0,0,1,1,1,0]

N=int(input())
*A,=list(map(int,input().split()))

ans=0
for i in range(N):
    for j in range(i,N):
        res=True
        for k in range(i,j+1):
            if A[k]==0:
                res=False
                break
            
        if res:
            #print(i,j)
            ans=max(ans,j-i+1)

print(ans+1)