def pascal(N):
    pas=[[0]*N for _ in range(N)]
    pas[0][0]=1
    for i in range(N-1):
        for j in range(i+1):
            pas[i+1][j]+=pas[i][j]
            pas[i+1][j+1]+=pas[i][j]
    return pas
        
from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under        

pas=pascal(60)
N=50
for i in range(N):
    for j in range(i,N):
        if pas[j][i] != cmb(j,i):
            print(i,j)