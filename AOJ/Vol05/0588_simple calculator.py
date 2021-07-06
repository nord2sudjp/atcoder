# 0588 Simple Calculator

import sys
from collections import deque
input=sys.stdin.readlines()

exp=['-','+','*','/']

d=deque()
d.append("1")
d.append("*")


for l in input:
    l=l.rstrip()
    if l=='=':break
    if l.isdecimal():
        exp=d.pop()
        opr1=d.pop()
        ans=eval(opr1+exp+l)
        #print(opr1+exp+l)
        d.append(str(ans))
    else:
        if l=='/':l='//'
        d.append(l)
print(d.pop())