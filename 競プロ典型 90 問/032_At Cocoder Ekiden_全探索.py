# 032 At Cocoder Ekiden
 
import itertools
INF=float('infinity')
 
N=int(input())
A=[list(map(int,input().split())) for _ in range(N)]
M=int(input())
X=[tuple(map(int,input().split())) for _ in range(M)]
X=set(X)
# N=3
# A=[[1, 10, 100], [10, 1, 100], [100, 10, 1]]
# M=1
# X=set([(1, 2)])
 
def main():
    global N
    global M
    e=list(itertools.permutations(range(1,N+1),N))
    #l_e=len(e)
    ans=INF
    for i in e:
        prv=-1
        t=0
        for j in range(N): # Kukan
            r=i[j]
            if (prv,r) in X or (r,prv) in X:
                t=INF
                break
            t=t+A[r-1][j]
            prv=r
        #print(i,ans,t)
        if t<ans:ans=t
    return ans
ans=main()
print(ans if ans!=INF else -1)