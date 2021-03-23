N=int(input())
AB=[list(map(int,input().split())) for _ in range(N)]

# N=4
# AB=[[0,2],[2,3],[2,4],[5,6]]

DP=[0]*1000010

for a,b in AB:
    DP[a]+=1
    DP[b+1]-=1

DP_A=[0]*1000001

l=len(DP_A)

DP_A[0]=DP[0]
for i in range(1,l):
    DP_A[i]=DP_A[i-1]+DP[i]
print(max(DP_A))