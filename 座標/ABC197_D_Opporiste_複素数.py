# atan2‚É‚æ‚é‰ñ“š

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


s=complex(p0[0],p0[1])
t=complex(pn[0],pn[1])
o=(s+t)/2.0

rad=2*math.pi/N
r=complex(math.cos(rad),math.sin(rad))

ans=o+(s-o)*r


print(ans.real, ans.imag)