# A->K�̌o�H�����߂���
# �_�C�N�X�g��=�ŒZ�o�H�����߂���
#     �؍\���ł̓_�C�N�X�g���͕K�v�Ȃ�
# �؍\���͌o�H�����=���D��T��
# DFS�ł��悢���A����ɂ���Ă͗����Ă��܂��B
# �����O���t�̂���A->K=K->A
# �܂�K����e���_�ւ̋����𕝗D��T���ŋ��߂�
#   BFS�̏I���͂ǂ�����Ċm�F���邩
#   �o�H�łȂ����߂ɏ���ɏI������
# ���̎��ɗ^����ꂽ�N�G���ɂ��ď���������
# BFS��DFS�̈Ⴂ
#   BFS : queue�𗘗p����
#   DFS : �ċA

import sys
sys.setrecursionlimit(10**7)

N=int(input())
G=[[] for _ in range(N+1)]
for i in range(N-1):
    x, y, z = map(int, input().split())
    G[x].append((y, z))
    G[y].append((x, z))
Q,K=map(int, input().split())

def dfs(s,dis):
    for e,d in G[s]:
        if flg[e]==1:continue
        DIS[e]=d+dis
        #print(e,d+dis)
        flg[e]=1
        dfs(e,d+dis)

flg=[0]*(N+1)
flg[K]=1
DIS={}
DIS[K]=0
dfs(K,0)

for _ in range(Q):
    s,t=map(int,input().split())
    print(DIS[s]+DIS[t])