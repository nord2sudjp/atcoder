# A Flog
N=int(input())
*H,=map(int,input().split())

D=[float("inf")]*N
D[0]=0

for i in range(1,N):
    # print([abs(H[i]-H[i-a])+D[i-a] for a in [1,2]])
 D[i]=min(abs(H[i]-H[i-a])+D[i-a] for a in [1,2])
print(D[-1])
