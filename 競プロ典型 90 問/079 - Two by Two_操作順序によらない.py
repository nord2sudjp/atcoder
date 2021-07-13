# 079 - Two by Two

f=lambda : map(int,input().split())

H,W=f()

A=[list(f()) for _ in range(H)]
B=[list(f()) for _ in range(H)]

C=[[0]*W for _ in range(H)]
for i in range(H):
    for j in range(W):
        C[i][j]=B[i][j]-A[i][j]
ans=0
for i in range(H-1):
    for j in range(W-1):
        t=C[i][j]
        if t!=0:
          ans+=abs(t)
          for x in [0,1]:
              for y in [0,1]:
                  C[i+x][j+y]=C[i+x][j+y]-t
check=True
for i in range(H):
  for j in range(W):
    if C[i][j]!=0:
      check=False
if check:
  print('Yes')
  print(ans)
else:
  print('No')
