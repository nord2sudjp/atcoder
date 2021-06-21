# Volume0-0026 Dropping Ink
import sys

S=[[0]*10 for _ in range(10)]

INK=[[],[],[]]
INK[0]=[[-1,0],[0,-1],[1,0],[0,1]]
INK[1]=[[-1,-1],[-1,1],[1,-1],[1,1]]
INK[1].extend(INK[0])
INK[2]=[[2,0],[0,2],[-2,0],[0,-2]]
INK[2].extend(INK[1])

for l in sys.stdin.readlines():
    x,y,s = map(int,l.split(","))
    for i in INK[s]:
        x=x+i[0]
        y=y+i[1]
        if 0<=x<=9 and 0<=y<=9:
            S[x][y]+=1

from itertools import chain
from collections import Counter
t=list(chain(*S))
print(t.count(0))
print(max(t))