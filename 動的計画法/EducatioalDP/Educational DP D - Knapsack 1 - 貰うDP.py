N,W=map(int,input().split())
WV=[list(map(int, input().split())) for _ in range(N)]

DP=[[0]*(W+10) for _ in range(N+10)]

# N�̂Ƃ��ADP�̍s��0�`N�ƂȂ�
# ���L�̃��[�v�ł� 0�`N-1��DP��1�`N�܂ōX�V�����

# W�̂Ƃ��ADP�̗��0�`W�ƂȂ�
# ���L�̃��[�v�ł� 0�`W��DP��1�`W�܂ōX�V�����

for i in range(N):
  for j in range(W+1):
  # for j in range(W):
    w,v=WV[i]
    if (j<w): # �d���������𒴂��Ă���ꍇ�ɂ�
      DP[i+1][j]=DP[i][j]
    else: # 0<=j-w
      DP[i+1][j]=max(DP[i][j], DP[i][j-w]+v)
           # �ႤDP�ł͒񋟑����r����
      #DP[i+1][j]=max(DP[i+1][j], DP[i][j-w]+v)
           # ����͔z��DP�̎�
print(DP[N][W])