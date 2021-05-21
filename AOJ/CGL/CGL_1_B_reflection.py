# CGL_1_A

from decimal import *
getcontext().prec = 15
  
def dot(v1,v2):
    return Decimal(v1[0])*Decimal(v2[0])+Decimal(v1[1])*Decimal(v2[1])

def cross(v1,v2):
    return Decimal(v1[0])*Decimal(v2[1])-Decimal(v1[1])*Decimal(v2[0])

def norm(v):
    return Decimal(v[0])**Decimal(2)+Decimal(v[1])**Decimal(2)


def reflect(p1,p2,po):
    pr=project(p1,p2,po)
    v=[i-j for i,j in zip(pr,po)]
    v=list(map(lambda x : Decimal(2)*Decimal(x), v))
    
    return [i+j for i,j in zip(po,v)]
    
def project(p1,p2,po):
    base=[i-j for i,j in zip(p1,p2)]
    v=[x-y for x,y in zip(po,p1)]
    r=Decimal(dot(v,base))/Decimal(norm(base))
    #print(p1,p2,po,base, norm(base), v,r)
    base=list(map(lambda x : Decimal(r)*Decimal(x), base))
    
    return [i+j for i,j in zip(p1,base)]

x1,y1,x2,y2=map(int,input().split())
Q=int(input())

for _ in range(Q):
    x3,y3=map(int,input().split())
    ans=reflect([x1,y1],[x2,y2],[x3,y3])
    print('{:.13f} {:.13f}'.format(ans[0],ans[1]))