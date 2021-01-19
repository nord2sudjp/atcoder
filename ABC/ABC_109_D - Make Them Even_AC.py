H,W=map(int,input().split())
A=[list(map(int,input().split())) for i in range(H)]

idou=[]
for i in range(H-1):
    for j in range(W):
        if A[i][j]%2!=0:
            A[i][j]-=1
            A[i+1][j]+=1
            idou.append([i+1, j+1, i+2, j+1])
            #print(i+1, j+1, i+2, j+1)

for i in range(W-1):
    if A[H-1][i]%2!=0:
        A[H-1][i]-=1
        A[H-1][i+1]+=1
        idou.append([H, i+1, H, i+2])
        
print(len(idou))
for i in idou:
    print(' '.join(map(str,i)))