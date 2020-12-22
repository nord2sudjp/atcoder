H,W=map(int,input().split())
A=[input() for _ in range(H)]
 
b=[[0]*W for _ in range(H)]
 
done=[[0]*W for _ in range(H)]
for h in range(H):
    for w in range(W):
        if done[h][w]:continue
        if A[h][w]=="#": continue
        x=0
        while w+x<W:
            if A[h][w+x]=='#':break
            x+=1
        for j in range(w,w+x):
            b[h][j]+=x
            done[h][j]=1
 
done=[[0]*W for _ in range(H)]
for h in range(H):
    for w in range(W):
        if done[h][w]:continue
        if A[h][w]=="#": continue
        x=0
        while h+x<H:
            if A[h+x][w]=='#':break
            x+=1
        for j in range(h,h+x):
            b[j][w]+=x
            done[j][w]=1
 
p=(0,0)
m=0
for h in range(H):
    for w in range(W):
        if m < b[h][w]:
            p=(h,w)
            m=b[h][w]
print(m-1)