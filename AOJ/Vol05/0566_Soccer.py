# 0566 Soccer

import sys
N=int(input())

input=sys.stdin.readlines()

D=[0]*(N+1)

for l in input:
    t1,t2,p1,p2=map(int,l.split())
    if p1>p2:
        D[t1]+=3
    elif p1<p2:
        D[t2]+=3
    else:
        D[t1]+=1
        D[t2]+=1

T=[[p,i] for i,p in enumerate(D) if i!=0]
T.sort(reverse=True)
#print(T)
cur=0
prv_p=0
ans={}
l_T=len(T)
for t in range(l_T):
  p,i=T[t]
  
  if prv_p!=p:
    cur=t+1
    prv_p=p
  ans[i]=cur
  #print(i,cur)
  
for i in range(1,N+1):
  print(ans[i])