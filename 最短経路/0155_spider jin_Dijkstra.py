# 0155 Spider Jin
from decimal import Decimal 
from heapq import heappop, heappush

def dy(N,s,t,cost):
    #print(G,s,t,cost)
    src=[-1]*(N+1)
    dist=[float('inf')]*(N+1)
    q=[(0, s)] 
    dist[s] = 0
    while q:
        _, v = heappop(q)
        for w in G[v]:
            if dist[w] > dist[v] + cost[(v, w)]: 
                dist[w] = dist[v] + cost[(v, w)]
                src[w]=v
                heappush(q, (dist[w], w))
    ans=dist[t] if dist[t] < float('inf') else -1
    return(ans,src)
    #return dist[t] if dist[t] < float('inf') else -1

def norm(v):
    return Decimal(v[0])**Decimal(2)+Decimal(v[1])**Decimal(2)

def _abs(v):
    return Decimal(norm(v))**Decimal(0.5)

def _absP(p1,p2):
    v=[i-j for i,j in zip(p1,p2)]
    return _abs(v)



while True:
    N=int(input())
    if N==0:break
        
    A=[[] for _ in range(N+1)]

    for _ in range(N):
        c,x,y=map(int,input().split())
        A[c]=(x,y)

#     N=4
#     A=[(0, 0), (30, 0), (60, 40), (0, 60)]

    cost={}
    G = [set() for _ in range(N+1)]

    for i in range(1,N+1):
        for j in range(i+1,N+1):
            dis=_absP(A[i],A[j])
            if dis<=50:
              cost[(i,j)]=dis
              cost[(j,i)]=dis
              G[i].add(j)
              G[j].add(i)


    # S=2
    # T=[(1,3),(1,4)]

    S=int(input())

    for _ in range(S):
        s,e=map(int,input().split())
        dist,src=dy(N,s,e,cost)
        if dist==-1:
            print('NA')
        else:
            i=e
            ans=[i]
            while src[i]!=-1:
               ans.append(src[i])
               i=src[i]
            print(' '.join(map(str,ans[::-1])))