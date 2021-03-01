from heapq import heappop, heappush


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
            
N,K = map(int, input().split())
            
G = [set() for _ in range(N+1)]
cost = {}
for _ in range(K):
    q,*c= map(int, input().split())
    if q==1:
        s,t,f=c
        min_cost=min(cost.get((s,t),float('inf')),f)
        cost[(s,t)] = min_cost
        cost[(t,s)] = min_cost
        G[s].add(t)
        G[t].add(s)
    else:
        s,t=c
        print(dy(N,s,t))