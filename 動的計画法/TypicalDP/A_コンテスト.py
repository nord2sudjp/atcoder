N=int(input())
M=100
*A,=list(map(int,input().split()))
X=[[0]*(N*M+1) for _ in range(N+1)]
# N�̃|�C���g������A���̃|�C���g�̍ő�l��100�ł���̂ŁA0<=�|�C���g<=N*M�ƂȂ�B

X[0][0]=1

for i, a in enumerate(A):  # �z��̍s 
    for j in range(N*M+1): # �z��̗�
        X[i+1][j]=X[i][j]
        if j >= a:
            X[i+1][j] |= X[i][j-a]
print(sum(X[N]))