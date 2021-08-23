# 13 Passing

from heapq import heappop, heappush


N,M=map(int,input().split())
G = [[] for _ in range(N+1)]
# Graph
cost = {}

for _ in range(M):
    a,b,c=map(int, input().split())
    cost[(a,b)]=c
    cost[(b,a)]=c
    G[a].append(b)
    G[b].append(a)

    
print(cost)
print(G)
def dy(N,s,t):
    #print(G,s,t,cost)
    dist=[float('inf')]*(N+1)
    q=[(0, s)] 
    dist[s] = 0
    while q:
        _, v = heappop(q)
        for w in G[v]:
            if dist[w] > dist[v] + cost[(v, w)]: 
                dist[w] = dist[v] + cost[(v, w)]
                heappush(q, (dist[w], w))
    return dist[t] if dist[t] < float('inf') else -1

dist1=dy(N,1,N)
distN=dy(N,N,1)

for k in range(1,N+1):
    print(dist1[k]+distN[k])