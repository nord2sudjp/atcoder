N,M=map(int,input().split())
S=input()
T=input()

MAX_N=N+2
MAX_M=M+2

DP=[[0]*(MAX_N) for _ in range(MAX_M)]

#DP[i+1][j+1] : S[i]T[j]�ɑ΂���LCS�̒���

for i in range(N):
    for j in range(M): 
        # i,j�͕�����Ƃ��Ă͌��݂����Ă���
        # DP�Ƃ��Ă͉ߋ���DP�����Ă���
        # DP[i][j]�͕�����S[i]T[j]�܂ł̋��ʕ�����̒�����\��
        DP[i][j+1]=max(DP[i][j+1],DP[i][j]) 
        DP[i+1][j]=max(DP[i+1][j],DP[i][j])
        if S[i]==T[j]:
            DP[i+1][j+1]=max(DP[i+1][j+1],DP[i][j]+1) #dp[i][j]�܂ł̒�����1�𑫂�����
print(DP[N][M])