# ���v���T�^-48
# �����_�͖��_��菬�������_�̔������傫��
# ���̏����ɂ�蕔���_�͂��Ȃ炸�c�������̃X�e�b�v�ŏ�����

N,K=map(int,input().split())
AB=[list(map(int,input().split())) for _ in range(N)]

# N=4
# K=3
# AB=[[4, 3], [9, 5], [15, 8], [8, 6]]

half=[h for f,h in AB]
rest=[f-h for f,h in AB]


half=[h for f,h in AB]
rest=[f-h for f,h in AB]
half.extend(rest)

half=sorted(half, reverse=True)

print(sum(half[:K]))
