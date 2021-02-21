# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_A&lang=ja

from heapq import heappop, heappush

V, E, r = map(int, input().split())
# V:Number of Vertex
# E:Number of Edge
# r:始点

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
while q: # キューにデータがある間はループ
   _, v = heappop(q) # _=コスト, v=処理するVertex
   for w in G[v]: # vからつながっているVertexをwとする
       if dist[w] > dist[v] + cost[(v, w)]: 
        # vとwはつながっているので必ずcostが存在する
        # コストの更新されるときのみヒープに追加する→再び訪れるとしてもここでフィルタされる
           dist[w] = dist[v] + cost[(v, w)] # コストが低い場合にはdist[w]を更新する
           heappush(q, (dist[w], w))
           # なぜdist[w]までpushする必要があるのか?→# 最も低いcostのvertexを順番に取得するため
           # 尺取り虫のように最もコストが低いVertexを見つけながら進んでいく

for v in range(V):
   print(dist[v] if dist[v] < float('inf') else "INF")