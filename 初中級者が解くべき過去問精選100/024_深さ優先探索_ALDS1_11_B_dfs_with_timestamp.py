# G �͗אڃ��X�g�\���̌`���ŗ^�����܂��B�e���_�ɂ� 1 ���� n �܂ł̔ԍ����ӂ��Ă��܂��B
# �e�אڃ��X�g�̒��_�͔ԍ������������ɕ��ׂ��Ă��܂��B
# �v���O�����͊e���_�̔��������Ɗ���������񍐂��܂��B
# �[���D��T���̉ߒ��ɂ����āA�K�₷�钸�_�̌�₪��������ꍇ�͒��_�ԍ������������̂���I�����܂��B
# �ŏ��ɖK�₷�钸�_�̊J�n������ 1 �Ƃ��܂��B


# N=4
# G=[[2],[4],[],[3]]
import sys
sys.setrecursionlimit(1000000)

N=int(input())
G=[list(map(int, input().split()))[2:] for _ in range(N)]

v=[False]*N
d=[0]*N
f=[0]*N
timecount=1

def dfs(i):
    global timecount
    if v[i] : return
    v[i] = True
    d[i] = timecount
    # print("D",i+1,timecount)
    timecount += 1
    for p in G[i]:
        dfs(p-1)
    # print("F",i+1,timecount)
    f[i] = timecount
    timecount += 1
    return

for i in range(N):
  if v[i]==0: dfs(i)

for i in range(N):
    print(i+1, d[i], f[i])