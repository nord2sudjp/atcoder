# 0621 Russian Flag

N,M=map(int,input().split())
S=[input() for _ in range(N)]

# N=4
# M=5
# S=['WRWRW', 'BWRWB', 'WRWRW', 'RWBWR']

R = [s.replace('W', '0').replace('B','1').replace('R','2') for s in S]
R=list(map(list,R))
R=[list(map(int,r)) for r in R]
#print(R)
ans=float('inf')

for w in range(1,N-1):
    for r in range(1,N-w):
        #print(w,r,N-w-r)
        t=0
        for i in range(w):
            #print(R[i],[0]*M)
            t+=len([x for x in R[i] if x!=0])
            #print(t)
        for i in range(r):
            #print(R[i+w],[1]*M)
            t+=len([x for x in R[i+w] if x!=1])
            #print(t)
        for i in range(N-w-r):
            #print(R[i+w+r],[2]*M)
            t+=len([x for x in R[i+w+r] if x!=2])
            #print(t)
        if ans>t:ans=t
        #print(t)
print(ans)