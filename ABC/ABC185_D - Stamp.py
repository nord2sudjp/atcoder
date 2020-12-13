N,M=map(int,input().split())
*A,=sorted(map(int,input().split()))

pa=0
w=N+1
dis=[]
for a in A:
    if a-pa>1:
        d=a-pa-1
        dis.append(d)
        # print(a,dis)

        w=min(w,d)
    pa=a

d=N-pa
if N!=pa: # 1‚Ì‚¸‚ç‚µ‚ªŠÔˆá‚Á‚Ä‚¢‚½
    w=min(w,d)
    dis.append(d)

# print(M,dis,w)

if M==0:
    ans=1 #–â‘è‚ÌˆÓ–¡‚ðŠ¨ˆá‚¢
elif w==0:
    ans=0
else:
    ans=sum(-(-i//w) for i in dis)
print(ans)