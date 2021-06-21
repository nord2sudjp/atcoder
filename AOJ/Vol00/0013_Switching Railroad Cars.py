# 13 Switching Railroad Cars

from collections import deque

d=deque()

import sys
S=[]
for l in sys.stdin:
     S.append(int(l))

#S=[1,6,0,8,10]

for s in S:
    if s==0:
        t=d.pop()
        print(t)
    else:
        d.append(s)
while d:
    print(d.pop())