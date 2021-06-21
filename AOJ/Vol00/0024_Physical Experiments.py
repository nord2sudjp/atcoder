# 0024:   Physical Experiments
import sys

for l in sys.stdin:
    v=float(l)
    t=v/9.8
    y=4.9*t**2
    N=(y+5)/5
    if N!=int(N):
      N=int(N)+1
    print(N)
