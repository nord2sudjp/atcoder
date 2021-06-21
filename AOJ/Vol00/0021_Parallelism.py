# 0021:   Parallelism

N=int(input())

INF=float('inf')

for _ in range(N):
    x1,y1,x2,y2,x3,y3,x4,y4 = map(float, input().split())
    if x2-x1!=0:
      d1=(y2-y1)/(x2-x1)
    else:
      d1=INF
    if x4-x3!=0:
      d2=(y4-y3)/(x4-x3)
    else:
      d2=INF

    #print(round(d1,5),round(d2,5))
    if round(d1,10)==round(d2,10):
        print('YES')
    else:
        print('NO')