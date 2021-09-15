f1=lambda:list(map(int,input().split()))
 
H,W=f1()
C=[]
for i in range(10):
    C.append(f1())
 
for k in range(10):
    for i in range(10):
        for j in range(10):
            C[i][j]=min(C[i][j], C[i][k]+C[k][j])
 
ans=0
for i in range(H):
    A=f1()
    for a in A:
        if a!=-1 and a!=1:
            ans+=C[a][1]
print(ans)    