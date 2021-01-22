f=lambda : [tuple(map(int,input().split())) for i in range(int(input()))]
P=f()
Q=f()
 
sq=set(Q)
px1=P[0][0]
py1=P[0][1]
v=[(x-px1,y-py1) for x,y in P[1:]]
for x,y in Q:
 if all([p in sq for p in [(x+vx,y+vy) for vx,vy in v]]) : 
   print(x-px1,y-py1)
   break