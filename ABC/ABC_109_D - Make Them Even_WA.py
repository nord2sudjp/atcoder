from collections import deque

H,W=map(int,input().split())
A=[list(map(int,input().split())) for i in range(H)]

r=[(1,0),(-1,0),(0,1),(0,-1)]
flg=[[0]*W for _ in range(H)]

idou_m=[]
d=deque()

def bfs(si,sj):
    flg[si][sj]=1

    d.append((si,sj))

    while d:
      pi,pj = d.popleft()
      for di,dj in r:
        ni=pi+di;nj=pj+dj
        if not(0<=ni<H and 0<=nj<W) or flg[ni][nj]!=0:continue
        flg[ni][nj]=1
        if A[ni][nj]%2 == 0 :
            d.append((ni,nj))
            continue 
        else:
            return((ni,nj)) # Žc‚Á‚Ä‚¢‚½d‚Í‚«‚¦‚Ä‚µ‚Ü‚¤B
    return ((-1,-1))

def idou(a,b):
    s=a[0]
    e=b[0]+1
    for i in range(s+1,e):
        #print(a[0],a[1],i,a[1])
        idou_m.append([a[0],a[1],i,a[1]])
        a[0]=i

    s=a[1]
    e=b[1]+1
    for i in range(s+1,e):
        #print(a[0],a[1],a[0],i)
        idou_m.append([a[0],a[1],a[0],i])
        a[1]=i
rtn=0
for i in range(H):
    for j in range(W):
        if A[i][j]%2==0:
            flg[i][j]=1
        else:
            ni,nj=bfs(i, j)
            if ni==-1:
                rtn=1
                break
            #print(i+1,j+1,ni+1,nj+1)
            idou([i+1,j+1],[ni+1,nj+1])
            A[i][j]-=1
            A[ni][nj]+=1
    if rtn==1:break
print(len(idou_m))
for i in idou_m:
    print(' '.join(map(str,i)))