# CGL-CGL_2_D Line


# 2_B
from decimal import *
getcontext().prec = 15
  
def dot(v1,v2):
    return Decimal(v1[0])*Decimal(v2[0])+Decimal(v1[1])*Decimal(v2[1])

def cross(v1,v2):
    return Decimal(v1[0])*Decimal(v2[1])-Decimal(v1[1])*Decimal(v2[0])

def norm(v):
    return Decimal(v[0])**Decimal(2)+Decimal(v[1])**Decimal(2)

def _abs(v):
    return Decimal(norm(v))**Decimal(0.5)

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
    
def is_parallel(x1, y1, x2, y2, x3, y3, x4, y4):
    #https://pcl.solima.net/pyblog/archives/779

    d1x = x2 - x1
    d1y = y2 - y1
    d2x = x4 - x3
    d2y = y4 - y3

    return cross([d1x,d1y],[d2x,d2y])==0
    # ベクトルa,bの外積の大きさ=0

def is_orthogonal(x1, y1, x2, y2, x3, y3, x4, y4):
    d1x = x2 - x1
    d1y = y2 - y1
    d2x = x4 - x3
    d2y = y4 - y3
    
    return dot([d1x,d1y],[d2x,d2y])==0


def ccw(v1,v2):
    text={0:"ON_SEGMENT",1:"COUNTER_CLOCKWISE",-1:"CLOCKWISE",2:"ONLINE_BACK",-2:"ONLINE_FRONT"}
    if cross(v1,v2)>0: return 1 # Counter clockwise
    if cross(v1,v2)<0: return -1 # clockwise
    if dot(v1,v2)<0:return 2 #online back
    if norm(v1)<norm(v2): return -2 #online front
    return 0 # on segment

def ccw_p(po,p1,p2):
    v1=(po[0]-p1[0],po[1]-p1[1])
    v2=(po[0]-p2[0],po[1]-p2[1])
    return ccw(v1,v2)

def intersect_p(p1,p2,p3,p4):
    return (ccw_p(p1,p2,p3) * ccw_p(p1,p2,p4) <= 0 and ccw_p(p3,p4,p1) * ccw_p(p3,p4,p2) <=0)

def intersect(s1,s2):
    return intersect_p(s1[0], s1[1], s2[0], s2[1])

def get_cross_point(s1,s2):
    
    s2_p1=s2[0]
    s2_p2=s2[1]
    
    
    
    base=(s2_p2[0]-s2_p1[0],s2_p2[1]-s2_p1[1])
    d1=abs(cross(base, (s1[0][0]-s2_p1[0],s1[0][1]-s2_p1[1]) ))
    d2=abs(cross(base, (s1[1][0]-s2_p1[0],s1[1][1]-s2_p1[1]) ))
    t=Decimal(d1)/(Decimal(d1)+Decimal(d2))
    
    h=map(lambda x : x*t, [p2-p1 for p2,p1 in zip(s1[1],s1[0])])
    return [p1+p2 for p2,p1 in zip(s1[0],h)] 

def get_distanceLP(l,p):
    v1=[p2-p1 for p2,p1 in zip(l[1],l[0])]
    v2=[p2-p1 for p2,p1 in zip(p,l[0])]
    t1=cross(v1,v2)
    
    t2=_abs([p2-p1 for p2,p1 in zip(l[1],l[0])])
    return abs(Decimal(t1)/Decimal(t2))


def get_distanceSP(s,p):
    v1=[p2-p1 for p2,p1 in zip(s[1],s[0])]
    v2=[p2-p1 for p2,p1 in zip(p,s[0])]
    if dot(v1,v2) < 0: return _abs(v2)
        
    v1=[p2-p1 for p2,p1 in zip(s[0],s[1])]
    v2=[p2-p1 for p2,p1 in zip(p,s[1])]
    if dot(v1,v2) < 0: return _abs(v2)
    return get_distanceLP(s,p)

def get_distance(s1,s2):
        if intersect(s1,s2):return 0
        ans=min( get_distanceSP(s1,s2[0]),get_distanceSP(s1,s2[1]),get_distanceSP(s2,s1[0]),get_distanceSP(s2,s1[1]))
        return ans

Q=int(input())

for _ in range(Q):
    p1x,p1y,p2x,p2y,p3x,p3y,p4x,p4y=map(int,input().split())
    print('{:.13f}'.format(get_distance([(p1x,p1y),(p2x,p2y)],[(p3x,p3y),(p4x,p4y)])))
