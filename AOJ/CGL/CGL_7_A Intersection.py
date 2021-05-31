# CGL_7_A Intersection
from decimal import *
getcontext().prec = 15



c1x,c1y,r1 = map(int,input().split())
c2x,c2y,r2 = map(int,input().split())

def norm(v):
    return Decimal(v[0])**Decimal(2)+Decimal(v[1])**Decimal(2)

def _abs(v):
    return Decimal(norm(v))**Decimal(0.5)

def _absP(p1,p2):
  return _abs([s-t for s,t in zip(p1,p2)])

d=_absP([c1x,c1y],[c2x,c2y])

if d>r1+r2:
    print(4)
elif d==r1+r2:
    print(3)
else:
    t=abs(r2-r1)
    if t<d:
        print(2)
    elif d==t:
        print(1)
    else:
        print(0)