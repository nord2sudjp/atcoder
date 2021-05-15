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
     outq.append(u) # rootは問題なくvisitできる
     for v in G[u]:
        indeg[v]-=1 # 次数を減らす
        if indeg[v]==0 and not(V[v]):
            #次数==0であり、まだ訪れていないならば
            V[v]=True
            q.append(v)    


def tsort():
    for u in range(N):
        for v in G[u]:
            indeg[v]+=1 # 入力の本数
    for u in range(N):
        if indeg[u]==0 and not(V[u]): bfs(u)
        # 次数=0、要するにrootのこと
    
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