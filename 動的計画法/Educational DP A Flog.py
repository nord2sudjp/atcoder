# A Flog
N=int(input())
*H,=map(int,input().split())

D=[float("inf")]*N
D[0]=0

for i in range(1,N):
    # print([abs(H[i]-H[i-a])+D[i-a] for a in [1,2]])
 D[i]=min(abs(H[i]-H[i-a])+D[i-a] for a in [1,2])
print(D[-1])



# B Flog 2
N,K=map(int,input().split())
*H,=map(int,input().split())

D=[float("inf")]*N
D[0]=0
D[1]=abs(H[1]-H[0])
for i in range(2,N):
  # print(i, "before:",D)
  # print(i,i-1,i-K, max(1, i-K))
  D[i]=min(abs(H[i]-H[k])+D[k] for k in range(max(0,i-K),i))
  # print(i, "after:",D)

print(D[-1])