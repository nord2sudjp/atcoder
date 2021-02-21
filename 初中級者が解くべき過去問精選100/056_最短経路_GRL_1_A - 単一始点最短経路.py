# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_A&lang=ja

from heapq import heappop, heappush

V, E, r = map(int, input().split())
# V:Number of Vertex
# E:Number of Edge
# r:�n�_

G = [[] for _ in range(V)]
# Graph
cost = {}
for _ in range(E):
   s, t, d = map(int, input().split())
   cost[(s, t)] = d
   G[s].append(t)

dist = [float('inf')]*V
q = [(0, r)]
dist[r] = 0
while q: # �L���[�Ƀf�[�^������Ԃ̓��[�v
   _, v = heappop(q) # _=�R�X�g, v=��������Vertex
   for w in G[v]: # v����Ȃ����Ă���Vertex��w�Ƃ���
       if dist[w] > dist[v] + cost[(v, w)]: 
        # v��w�͂Ȃ����Ă���̂ŕK��cost�����݂���
        # �R�X�g�̍X�V�����Ƃ��̂݃q�[�v�ɒǉ����遨�ĂіK���Ƃ��Ă������Ńt�B���^�����
           dist[w] = dist[v] + cost[(v, w)] # �R�X�g���Ⴂ�ꍇ�ɂ�dist[w]���X�V����
           heappush(q, (dist[w], w))
           # �Ȃ�dist[w]�܂�push����K�v������̂�?��# �ł��Ⴂcost��vertex�����ԂɎ擾���邽��
           # �ڎ�蒎�̂悤�ɍł��R�X�g���ႢVertex�������Ȃ���i��ł���

for v in range(V):
   print(dist[v] if dist[v] < float('inf') else "INF")