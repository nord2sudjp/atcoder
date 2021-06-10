# 0179 Mysterious Worm

import sys
from collections import deque
sys.setrecursionlimit(1000000)


D={"rb":"gg","br":"gg","bg":"rr","gb":"rr","gr":"bb","rg":"bb"}

def bfs(S):
    F=set()
    ans=[]
    L=len(S)
    cnt=1
    d=deque()
    d.append([cnt,S])
    F.add(S)
    while d:
     # print(d)
     cnt,v = d.popleft()
     x=[]
     for i in range(L-1):
        t=D.get(v[i:i+2],"")
        if t=="":continue
        ns=v[:i]+t+v[i+2:]
        if len(set(ns))==1:
            ans.append([v,ns])
            #print(cnt,v,ns)
            break
            #continue
        if ns in F:continue
        F.add(ns)
        x.append(ns)
        d.append([cnt+1,ns])
     #print(v,cnt,x)
     if len(ans)!=0:break
     #print(v,x)
    print(cnt if len(ans)!=0 else "NA")
    #print(len(ans),ans)

while True:
    S=input()
    if S=='0':break
    if len(set(S))==1:
        print(0)
    else:
        v=bfs(S)
