D,N=map(int,input().split())
T=[int(input()) for _ in range(D)]
Cloth=[list(map(int,input().split())) for _ in range(N)]

# D=3
# N=4
# T=[31, 27, 35]
# Cloth=[[20, 25, 30], [23, 29, 90], [21, 35, 60], [28, 33, 40]]

# D=6
# N=6
# T=[41, 22, 17, 54, 55, 1]
# Cloth=[[18, 59, 19], [1, 32, 75], [14, 40, 97], [12, 32, 82], [14, 14, 0], [31, 52, 42]]

DP_1=[[-1]*N for _ in range(D)]

for i in range(D):
    t=T[i]
    for j in range(N):
        a,b,c=Cloth[j]
        if a<=t<=b:
            DP_1[i][j]=c
#print(DP_1)

DP_2=[[0]*N for _ in range(D)]

for i in range(1,D):
    for j in range(N):
        if DP_1[i][j]==-1:continue # “–“ú‚Ì•ž‚Ì‘ÎÛ‚Å‚Í‚È‚¢
        for k in range(N): 
            if DP_1[i-1][k]==-1:continue # ‘O“ú‚Ì•ž‚Ì‘ÎÛ‚Å‚Í‚È‚¢
            DP_2[i][j]=max(DP_2[i][j], DP_2[i-1][k]+abs(DP_1[i][j]-DP_1[i-1][k]))
#print(DP_2)

print(max(DP_2[-1]))