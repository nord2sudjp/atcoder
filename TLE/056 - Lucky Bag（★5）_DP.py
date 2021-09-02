# TLE - リストと辞書を両方使っていた
# AC - 辞書を使うのをやめた

# 056  Lucky Bag（★5）

N,S=map(int,input().split())
P=[list(map(int,input().split())) for  _ in range(N)]

# N=3
# S=34
# P=[[3, 14], [15, 9], [26, 5]]

MAXS=2*10**5+7
DP=[[0]*(MAXS) for _ in range(N+1)]
D={}

DP[0][0]=1

for i in range(N):
    for j in range(S):
        if DP[i][j]:
            t=j+P[i][0]
            DP[i+1][t]='A'
            #D[(i+1,t)]=0
            t=j+P[i][1]
            DP[i+1][t]='B'
            #D[(i+1,t)]=1
#print(D)
ans=[]
if DP[N][S]!=0:
    for j in range(N,0,-1):
        #print(j,S,D[(j,S)],P[j-1][D[(j,S)]])
        v=DP[j][S]
        ans.append(v)
        S=S-P[j-1][0 if v=='A' else 1]
    #print(ans[::-1])
    ans=ans[::-1]
      
    #ans1=['A' if i==0 else 'B' for i in ans]
    print(''.join(ans))
            
else:
    print("Impossible")
