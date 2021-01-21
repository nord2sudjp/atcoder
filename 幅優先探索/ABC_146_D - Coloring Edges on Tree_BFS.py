import sys
sys.setrecursionlimit(10**7)

N=int(input())
G=[[] for _ in range(N+1)]
AB=[]
for i in range(N-1):
    x, y= map(int, input().split())
    AB.append((x,y))
    G[x].append(y)
    G[y].append(x)   
g_l=[len(a) for a in G]
g_l_max=max(g_l)
g_l_max_i=g_l.index(g_l_max)

F=[-1]*(N+1)
F[0]=F[g_l_max_i]=0

from collections import deque

d=deque()
d.append(g_l_max_i)
dic={}
c=1
while 0<len(d):
    #print(d)
    a=d.popleft()
    cnt=1
    for j in G[a]:
        #print(a,j)
        if F[j]!=-1:continue
        if cnt==F[a]:cnt+=1
        F[j]=cnt
        dic[(a,j)]=cnt
        dic[(j,a)]=cnt
        d.append(j)
        cnt+=1
print(g_l_max)
for ab in AB:
    print(dic[ab])