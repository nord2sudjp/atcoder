# GRL_1_C
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_C&lang=ja

V,E=map(int,input().split())

D = [[float('infinity')]*V for _ in range(V)]
# c²i,‘²jΖ·ιΖAcost[i][j]Νi->jΦΜ£

for i in range(V):
    D[i][i]=0  # i->iΜRXgΝR0

for _  in range(E):
    s,t,d=map(int,input().split())
    D[s][t]=d

for k in range(V): # pn_
    for i in range(V): # Start
        for j in range(V): # End
            if D[i][j] > D[i][k] + D[k][j]:
                D[i][j] = D[i][k] + D[k][j]

for i in range(V):
    if D[i][i] < 0: 
        print ('NEGATIVE CYCLE')
        exit()

for dis in D:
    dis = [str(i).replace('inf','INF') for i in dis]
    print(' '.join(dis))