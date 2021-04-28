# 0022: Maximum Sum Sequence

#N=7
#S=[-5, -1, 6, 4, 9, -6, -7]
#S=[1,2,3,4,0]


import sys
input=sys.stdin


while True:
    N=int(input.readline())
    if N==0:break

    S=[]
    for l in range(N):
        S.append(int(input.readline()))

    #print(S)
    CS=[0]*(N+1)

    for i in range(N):
        CS[i+1]=CS[i]+S[i]
    #print(CS)

    l=len(CS)
    INF=-1*float('inf')
    ans=INF
    for i in range(l-1):
        for j in range(i+1,l):
            t=CS[j]-CS[i]
            #print(i,j,CS[j]-CS[i],t)
            ans=max(ans,t)
    print(ans)