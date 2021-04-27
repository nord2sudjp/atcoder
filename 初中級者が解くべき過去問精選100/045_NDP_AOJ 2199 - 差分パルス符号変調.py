# N=2
# M=7
# C=[4,2,1,0,-1,-2,-4]
# S=[131,137]

# min�����O
# readline()�Œ����ǂݍ���
# readlines() -> ���X�g�A�N�Z�X
# �֐���
# ls_square
# decoder
# result
# input�����Ƃɖ߂�
# ls_square->square
# input->stdin
# INF����폜

from sys import stdin
input = stdin
def solve():
    INF=10**10
    ls_square = tuple(tuple((x - t)**2 for x in range(256)) for t in range(256))


    res=[]
    while 1:
        N,M=map(int,input.readline().split())
        if N==0 and M==0: break
        #print(N,M, input_idx)

        C=[int(input.readline()) for _ in range(M)]
        S=[int(input.readline()) for _ in range(N)]
        DP1 = [INF]*256
        DP2 = [INF]*256
        DP1[128] = 0

        decoder = tuple(tuple(255 if i + c > 255 else 0 if i + c < 0 else i + c for c in C) for i in range(256))

        for i in range(N):
            x=S[i]
            square=ls_square[x] # ���̒l

            for j in range(256):
                
                # ���̃R�[�h�������ɂ����TLE
                #x=S[i]
                #square=ls_square[x] # ���̒l
                
                # if�̓R�X�g��������
                #if DP1[j]!=INF:

                
                dpnk=DP1[j] # ���v
                for c in decoder[j]:
                    ans=dpnk+square[c]
                    if ans<DP2[c]:DP2[c]=ans
            DP1 = DP2[:]
            DP2 = [INF]*256      
        res.append(min(DP1))
    for a in res:
        print(a)
solve()