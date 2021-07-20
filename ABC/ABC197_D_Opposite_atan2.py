i1=lambda : input()
i2=lambda : int(input())
i3=lambda : map(int,input().split())
i4=lambda : list(map(int,input().split()))
i5=lambda n : [list(map(int,input().split())) for _ in range(n)]
i6=lambda n : [list(input())for _ in range(n)]

import math
from decimal import *
getcontext().prec = 15

def norm(v):
    return Decimal(v[0])**Decimal(2)+Decimal(v[1])**Decimal(2)

def _abs(v):
    return Decimal(norm(v))**Decimal(0.5)

def _absP(p1,p2):
    v=[i-j for i,j in zip(p1,p2)]
    return _abs(v)    
N=i2()

p0=i4()
pn=i4()

# N=4
# p0=[1,1]
# pn=[2,2]

cx=(Decimal(p0[0])+Decimal(pn[0]))/Decimal(2)
cy=(Decimal(p0[1])+Decimal(pn[1]))/Decimal(2)
r=_absP(p0,pn)/2
mv_theta=math.pi/(N//2)

theta=math.atan2(Decimal(p0[1])-Decimal(cy),Decimal(p0[0])-Decimal(cx))
n_theta=theta+mv_theta
#print(cx,cy,r,math.degrees(theta),math.degrees(n_theta),math.cos(n_theta),math.sin(n_theta))

nx=cx+r*Decimal(math.cos(n_theta))
ny=cy+r*Decimal(math.sin(n_theta))

print(nx,ny)