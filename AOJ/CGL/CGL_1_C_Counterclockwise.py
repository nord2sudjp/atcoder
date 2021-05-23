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


def clockwise(v1,v2):
    text={-1:"CLOCKWISE",0:"ON_SEGMENT",1:"COUNTER_CLOCKWISE",2:"ONLINE_BACK",-2:"ONLINE_FRONT"}
    if cross(v1,v2)>0: return 1 # Counter clockwise
    if cross(v1,v2)<0: return -1 # clockwise
    if dot(v1,v2)<0:return 2 #online back
    if norm(v1)<norm(v2): return -2 #online front
    return 0 # on segment

x0,y0,x1,y1=map(int,input().split())
Q=int(input())

text={-1:"CLOCKWISE",0:"ON_SEGMENT",1:"COUNTER_CLOCKWISE",2:"ONLINE_BACK",-2:"ONLINE_FRONT"}

for _ in range(Q):
    x2,y2=map(int,input().split())
    v1=(x0-x1,y0-y1)
    v2=(x0-x2,y0-y2)
    print(text[clockwise(v1,v2)])
    
    