ROW = 5
INF = float('inf')
N=int(input())
Colors={}

for i in range(ROW): # i=—ñ
    s=input()
    for j in range(N): # j •¶Žš
        t=Colors.get((j+1,s[j]),0)
        Colors[(j+1,s[j])]=t+1

#print(Colors)
# N=3
# Colors={(1, 'W'): 1, (2, 'W'): 2, (3, 'R'): 2, (1, '#'): 2, (2, 'R'): 1, (3, 'W'): 1, (1, 'B'): 1, (3, '#'): 1, (2, '#'): 1, (3, 'B'): 1, (1, 'R'): 1, (2, 'B'): 1}

DP_1=[[0]*3 for _ in range(N+1)]

for i in range(1,N+1):
    for j,s in enumerate(["B","W","R"]):
        DP_1[i][j]=ROW-Colors.get((i,s),0)
#print(DP_1)

DP_2=[[INF]*3 for _ in range(N+1)]

for i in range(3):
    DP_2[0][i]=0

for i in range(1,N+1):
    for j,s in enumerate(["B","W","R"]):
            #print(i,j,s)
            DP_2[i][j]=DP_1[i][j]+min([DP_2[i-1][v] for v in range(3) if v != j])
print(min(DP_2[-1]))