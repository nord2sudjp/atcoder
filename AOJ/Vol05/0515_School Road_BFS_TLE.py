# 0515 School Road

from collections import deque

while True:
    
# M=5
# N=4
# K=set(((2,2),(2,3),(4,2)))

    M,N=map(int,input().split())
    if M==N==0:break
    Q=int(input())
    k=[]
    for _ in range(Q):
        k.append(tuple(map(int,input().split())))
    K=set(k)

    D=deque()
    D.append((1,1))

    F=[[0]*(N+1) for _ in range(M+1)]

    directions=[(0,1),(1,0)]
    while D:
        x,y=D.pop()
        for dx,dy in directions:
            nx=x+dx
            ny=y+dy
            #print(nx,ny,nx>M,ny>N)
            if nx>M or ny>N:continue
            if (nx,ny) in K:continue
            #print(x,y,nx,ny)
            F[nx][ny]+=1
            D.append((nx,ny))
    print(F[M][N])