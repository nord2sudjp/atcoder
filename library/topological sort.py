# GRL_4_B

import sys
from collections import deque
sys.setrecursionlimit(1000000)

def bfs(s):
    q=deque()
    q.append(s)
    V[s]=True
    
    while q:
     # print(d)
     u = q.popleft()
     outq.append(u) # root�͖��Ȃ�visit�ł���
     for v in G[u]:
        indeg[v]-=1 # ���������炷
        if indeg[v]==0 and not(V[v]):
            #����==0�ł���A�܂��K��Ă��Ȃ��Ȃ��
            V[v]=True
            q.append(v)    


def tsort():
    for u in range(N):
        for v in G[u]:
            indeg[v]+=1 # ���̖͂{��
    for u in range(N):
        if indeg[u]==0 and not(V[u]): bfs(u)
        # ����=0�A�v�����root�̂���
    
MAXN=10007
INF=float('infinity')

G=[[] for _ in range(MAXN)] 
V=[False]*MAXN
indeg=[0]*MAXN
outq=deque()

N,M=map(int,input().split())

Q = sys.stdin.readlines()

for q in Q:
 s,t=map(int,q.split())
 G[s].append(t)

# N=6
# M=6
# G=[[1], [2], [], [1, 4], [5], [2], [], [], [], []]

tsort()


#print(outq)

for i in outq:
    print(i)