N,K=map(int,input().split())
AB={}
for _ in range(K):
    a,b=map(int,input().split())
    AB[a-1]=b-1


DP=[[[0]*3 for _ in range(3)] for _ in range(N+1)]
DP[0][0][0]=1

for n in range(N):
    for day2 in range(3):
        for day1 in range(3):
            pasta=[0,1,2]
            #print(n,day2,day1,DP[n][day2][day1])
            if AB.get(n,-1)!=-1:
                pasta=[AB.get(n,-1)]
            for p in pasta:
                if n>=2 and day1 == day2 == p:continue
    
                DP[n+1][day1][p]+=DP[n][day2][day1]
                

print( sum(map(sum, DP[N])) %10000)