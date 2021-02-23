V,E=map(int,input().split())

D = [[float('infinity')]*(V) for _ in range(V)]
# 縦軸i,横軸jとすると、cost[i][j]はi->jへの距離

for i in range(V):
    D[i][i]=0  # i->iのコストは当然0

for _  in range(E):
    s,t,d=map(int,input().split())
    D[s-1][t-1]=d
    D[t-1][s-1]=d

for k in range(V): # 中継地点
    for i in range(V): # Start
        for j in range(V): # End
            if D[i][j] > D[i][k] + D[k][j]:
                D[i][j] = D[i][k] + D[k][j]

#sumd=[sum(d) for d in D]
# 合計で計算するのではない最大値で比較する必要がある
#min_sum=min(d)
#sumd_i=[i for i in range(len(sumd)) if sumd[i]==min_sum]

#ans=float('infinity')
#for d in sumd_i:
#    if max(D[d]) < ans:
#        ans=max(D[d])

ans=min([max(d) for d in D])
print(ans)