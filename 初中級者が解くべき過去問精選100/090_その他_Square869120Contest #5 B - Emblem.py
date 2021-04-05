# N=0
# M=2
# C=[[6,3,-1],[2,4,-1]]

# N=0
# M=5
# C=[[8, 6,-1], [9, 1,-1], [2, 0,-1], [1, 0,-1], [0, 1,-1]]

# N=3
# M=0
# C=[[5, 2,3], [-1, 0,2], [2, -6,4]]

# N=1
# M=1
# C=[[0,0,5],[6,-3,-1]]


def d(p1,p2):
    x1,y1,r=p1
    x2,y2,r=p2
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

N,M=map(int,input().split())
C=[]
for _ in range(N):
    x,y,r=map(int,input().split())
    C.append([x,y,r])

for _ in range(M):
    x,y=map(int,input().split())
    C.append([x,y,-1])

dis=[]

for i in range(N+M):
    for j in range(i+1,N+M):
        t=d(C[i],C[j])
        dis.append([t,i,j])
dis=sorted(dis)

#print(dis)

# r=[-1]*M

for d in dis:
    t=d[0]
    p1=d[1]
    p2=d[2]
    #print(t,p1,p2)
    
    if C[p1][2]==-1 and C[p2][2]==-1:
        x=t/2
        C[p1][2]=x
        C[p2][2]=x
    elif C[p1][2]==-1:
        C[p1][2]=t-C[p2][2]
    elif C[p2][2]==-1:
        C[p2][2]=t-C[p1][2]
        
r=[n[2] for n in C]
print(min(r))
