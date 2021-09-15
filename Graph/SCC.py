import sys
from collections import deque
sys.setrecursionlimit(1000000)

 
# N, Q = map(int, input().split())
# G = [[] for i in range(N)]
# cnt = [0]*N
 
# # “ü—Í‚µ‚È‚ª‚çƒOƒ‰ƒt‚ğì¬
# for i in range(N-1):
#   a, b = map(int, input().split())
#   a, b = a-1, b-1
#   G[a].append(b)
#   G[b].append(a)
 
 
N=11
G=[[1],[2,3],[0],[4],[5],[3],[5,7],[8],[9],[6,10],[]]

def rev(G):
    l_G=len(G)
    T=[[] for _ in range(l_G)]
    for i in range(l_G):
        #print(G[i])
        for e in G[i]:
            T[e].append(i)
    return T    

def dfs(i,G,V,S):
    V.remove(i)
    for p in G[i]:
        if p in V:
            dfs(p,G,V,S)
    S.append(i)
        
    return

def nextE(S,V):
    while True:
        e=S.pop()
        if e in V:
            break
    return e
            
    
    
V=set(range(N))
S=deque()
while V:
    init=V.pop()
    V.add(init)
    dfs(init,G,V,S)

G=rev(G)
V=set(range(N))
T=[]
while V:
    e=nextE(S,V)
    dfs(e,G,V,T)
    print(T)
    T=[]