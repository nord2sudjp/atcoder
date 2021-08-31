# 036 - Max Manhattan Distance

N,Q=map(int,input().split())
L=[list(map(int,input().split())) for _ in range(N)]
Z=[int(input())-1 for _ in range(Q)]
       
# L=[[-1, 2], [1, 1], [-2, -3]]
# Z=[0,1, 2]
       
# ‰ñ“]‚µ‚È‚ª‚çLX,RX, UY, BY‚ğ‹‚ß‚é
INF=float('inf')
LX=BY=INF
RX=UY=-INF

for l in L:
    l[0],l[1]=l[0]-l[1],l[0]+l[1]
    if l[0]<LX: LX=l[0]
    if l[0]>RX: RX=l[0]
    if l[1]<BY: BY=l[1]
    if l[1]>UY: UY=l[1]
        
#print(L)
#print(LX,RX,BY,UY)
       
# Q‚É‚Â‚¢‚ÄÅ‘å’l‚Æ‚Ì·‚Ì‚İæ‚é

for i in Z:
    ans=max(abs(LX-L[i][0]), abs(RX-L[i][0]),abs(BY-L[i][1]),abs(UY-L[i][1]))
    print(ans)
