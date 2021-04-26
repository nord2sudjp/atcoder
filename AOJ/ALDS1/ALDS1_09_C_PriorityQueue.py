# “–‰TLE‚ª‚Å‚Ä‚¢‚½
# sys.stdin.readlines()
# elif -> else
# opr="insert" -> opr[0]="i"

# Œ‹˜_
# sys.stdin.readlines()‚ª‚Í‚â‚¢

import heapq
import sys
a = []
heapq.heapify(a)
l=sys.stdin.readlines()

for t in l:
    opr,*v=t.split()
    if opr[0]=='i':
        heapq.heappush(a, int(v[0])*-1)
    elif opr[1]=='x':
        print(heapq.heappop(a)*-1)
    else:
        break