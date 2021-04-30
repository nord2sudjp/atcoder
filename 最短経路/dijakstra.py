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
    return dist

dist=dijkstra(N,G,cost)
for v in range(N):
   # print(dist[v] if dist[v] < float('inf') else "INF")
   print(v,dist[v])