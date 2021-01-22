N=int(input())
C=tuple(sorted([tuple(map(int,input().split())) for i in range(N)]))
 
 
#N=10
#C=tuple(sorted(((9,4), (4,3), (1,1), (4,2), (2,4), (5,8), (4,0), (5,3), (0,5), (5,2))))
set_C=set(C)
 
S=0
d=0
sq=0
for i in range(N-1):
    x1,y1=C[i]
    for j in range(i+1,N):
        x2,y2=C[j]
        vx,vy=(-(y2-y1),x2-x1)
        p=(x1+vx, y1+vy)
        q=(x2+vx, y2+vy)
        #sq=vx**2+vy**2 # ‚±‚ê‚ªd‚¢‚ç‚µ‚¢
        if sq<d:continue
        if p in set_C and q in set_C:
            #print(C[i], C[j], p,q,v,v[0]**2+v[1]**2)
            sq=vx**2+vy**2
            S=max(S, sq)
            d=sq
print(S)