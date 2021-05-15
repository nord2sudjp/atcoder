# GRL_1_C
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_C&lang=ja

V,E=map(int,input().split())

D = [[float('infinity')]*V for _ in range(V)]
# 縦軸i,横軸jとすると、cost[i][j]はi->jへの距離

for i in range(V):
    D[i][i]=0  # i->iのコストは当然0

for _  in range(E):
    s,t,d=map(int,input().split())
    D[s][t]=d

for k in range(V): # 中継地点
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