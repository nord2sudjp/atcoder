# A->Kの経路を求められる
# ダイクストラ=最短経路を求める問題
#     木構造ではダイクストラは必要ない
# 木構造は経路が一つ=幅優先探索
# DFSでもよいが、言語によっては落ちてしまう。
# 無向グラフのためA->K=K->A
# まずKから各頂点への距離を幅優先探索で求める
#   BFSの終了はどうやって確認するか
#   閉経路でないために勝手に終了する
# その次に与えられたクエリについて処理をする
# BFSとDFSの違い
#   BFS : queueを利用する
#   DFS : 再帰

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