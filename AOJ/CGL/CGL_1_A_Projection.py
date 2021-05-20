# CGL_1_A

def dot(v1,v2):
    return v1[0]*v2[0]+v1[1]*v2[1]

def cross(v1,v2):
    return v1[0]*v2[1]-v1[1]*v2[0]

def norm(v):
    return v[0]**2+v[1]**2

def project(p1,p2,po):
    base=[i-j for i,j in zip(p1,p2)]
    v=[x-y for x,y in zip(po,p1)]
    r=dot(v,base)/norm(base)
    #print(p1,p2,po,base, norm(base), v,r)
    base=list(map(lambda x : r*x, base))
    
    return [i+j for i,j in zip(p1,base)]

x1,y1,x2,y2=map(int,input().split())
Q=int(input())

for _ in range(Q):
    x3,y3=map(int,input().split())
    print(' '.join(map(str,project([x1,y1],[x2,y2],[x3,y3]))))