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