N,W=map(int,input().split())
P=[list(map(int, input().split())) for _ in range(N)]

mem=[[0]*(W+2) for _ in range(N+2)]

for i in range(N,0,-1):
    for w in range(0,W+1):
        value, weight=P[i-1]
        if w < weight:
            mem[i][w] =mem[i+1][w]
        else:
            mem[i][w]=max(mem[i+1][w], mem[i+1][w-weight]+value)
print(mem[1][W])