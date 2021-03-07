from collections import deque

N=int(input())
graph = [[] for _ in range(N)] # —×ÚƒŠƒXƒg

for _ in range(N):
    v,c,*l = map(int,input().split())
    for i in l:
        graph[v-1].append(i-1)
        # graph[i-1].append(v-1)

dist=[-1]*N
dist[0]=0

d=deque()
d.append(0)

while d:
 # print(d)
 v = d.popleft()
 for i in graph[v]:
   if dist[i] != -1:
     continue
   dist[i] = dist[v] + 1
   d.append(i)
for i in range(len(dist)):
    print(i+1,dist[i])
    