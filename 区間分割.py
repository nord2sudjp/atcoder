N=[1, 0, 1, 1, 1, 1, 0, 1, 1, 1]
i=0;
l=len(N)
res=0
while i<l:
    if (N[i] == 0):
        i+=1# 0�Ȃ炻�̂܂ܐi��
    else:
        res+=1 # �V������Ԃ̎n�܂�
        while i<l and 0<N[i]:
            i+=1 #��Ԃ̏I���܂ň�C��
print(res)