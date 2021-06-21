# 0002:Digit Number
import sys
a = []
for l in sys.stdin:
    a.append(l.split())
for i in a:
    #print(i)
    s,t=map(int,i)
    print(len(str(s+t)))