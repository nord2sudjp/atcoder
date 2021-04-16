N=10
passize=N+5
pas=[[0]*passize for _ in range(passize)]
pas[0][0]=1
for i in range(N+1):
    for j in range(i+1):
        pas[i+1][j]+=pas[i][j]
        pas[i+1][j+1]+=pas[i][j]
print(pas)