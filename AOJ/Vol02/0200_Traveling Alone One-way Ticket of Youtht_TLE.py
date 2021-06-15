0200   Traveling Alone One-way Ticket of Youth
# 0200 Traveling Alone: One-way Ticket of Youth
from decimal import Decimal 
from heapq import heappop, heappush

def solve(N,G,fare,time,s,t,query):
    if query==0:
        cost=fare
    else:
        cost=time
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
    ans=dist[t] if dist[t] < float('inf') else -1
    return(ans)
    #return dist[t] if dist[t] < float('inf') else -1

    
def main():
    while True:
        N,M=map(int,input().split())
        if N==0 and M==0:return

        G = [set() for _ in range(M+1)]

        fare={}
        time={}

        for i in range(N):
            a,b,f,t=map(int,input().split())
            time[(a,b)]=t
            time[(b,a)]=t
            fare[(a,b)]=f
            fare[(b,a)]=f
            G[a].add(b)
            G[b].add(a)
        Q=int(input())
        for i in range(Q):
            p,q,r=map(int,input().split())
            print(solve(N,G,fare,time,p,q,r))
            

# time={(1, 2): 10, (2, 1): 10, (1, 4): 15, (4, 1): 15, (1, 3): 25, (3, 1): 25, (2, 4): 10, (4, 2): 10, (4, 5): 20, (5, 4): 20, (3, 5): 20, (5, 3): 20}
# fare={(1, 2): 200, (2, 1): 200, (1, 4): 400, (4, 1): 400, (1, 3): 250, (3, 1): 250, (2, 4): 100, (4, 2): 100, (4, 5): 150, (5, 4): 150, (3, 5): 300, (5, 3): 300}
# G=[set(), {2, 4, 3}, {1, 4}, {1, 5}, {1, 2, 5}, {4, 3}]
#print(solve(N,G,fare,time,1,5,1))

main()
    
