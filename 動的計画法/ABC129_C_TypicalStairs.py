N,M=map(int, input().split())
A=set(int(input()) for _ in range(M))
D=[0]*(N+1)
D[0]=1

for i in range(1,N+1):
 if i in A: continue
    # ��΂��K�i�͂����܂ł̕���0�Ƃ���B
 D[i]=(D[i-1]+D[i-2])%(10**9+7) # mod�̘a�Z�őΉ�
    # i-2, i-1��out of range�̏ꍇ�A�E�[�̒l�ƂȂ�B�����0�Ȃ̂ŉe�����Ȃ�
print(D[-1])