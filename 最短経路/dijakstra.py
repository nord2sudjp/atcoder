# ALDS1_12_B

# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_A&lang=ja

from heapq import heappop, heappush

N=int(input())
G = [[] for _ in range(N)]
# Graph
cost = {}

for _ in range(N):
    v,c,*t=map(int, input().split())
    for i in range(0,2*c,2):
        cost[(v,t[i])]=t[i+1]
        G[v].append(t[i])


# N=5
# G=[[2, 3, 1], [0, 3], [0, 3, 4], [2, 0, 1, 4], [2, 3]]
# cost={(0, 2): 3, (0, 3): 1, (0, 1): 2, (1, 0): 2, (1, 3): 4, (2, 0): 3, (2, 3): 1, (2, 4): 1, (3, 2): 1, (3, 0): 1, (3, 1): 4, (3, 4): 3, (4, 2): 1, (4, 3): 3}

def dijkstra(N,G,cost):
    r=0
    dist = [float('inf')]*N
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
    return dist

dist=dijkstra(N,G,cost)
for v in range(N):
   # print(dist[v] if dist[v] < float('inf') else "INF")
   print(v,dist[v])