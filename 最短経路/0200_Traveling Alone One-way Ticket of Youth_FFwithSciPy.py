# GRL_1_C
from scipy.sparse.csgraph import floyd_warshall 

INF=10**9+7
inf=10**9+7

def solve(V,fare,time):
    for k in range(V):
        for i in range(V):
            for j in range(V):
                t=fare[i][k] + fare[k][j]
                if fare[i][j] > t:
                    fare[i][j] = t
                t=time[i][k] + time[k][j]
                if time[i][j] > t:
                    time[i][j] = t
    return (fare,time)

                    
#def main():


while True:    
        N,M=map(int,input().split())
        if N==0 and M==0:break
        MAXM=M+1
        fare=[[INF]*(MAXM) for _ in range(MAXM)]
        time=[[INF]*(MAXM) for _ in range(MAXM)]

        # Don't forget initialize 
        for i in range(MAXM):
            fare[i][i]=0
            time[i][i]=0
        
        for i in range(N):
            a,b,f,t=map(int,input().split())
            fare[a][b]=f
            fare[b][a]=f
            time[a][b]=t
            time[b][a]=t

        #fare,time=solve(MAXM,fare,time)
        fare=floyd_warshall(fare)
        time=floyd_warshall(time)
        
        Q=int(input())
        for i in range(Q):
            p,q,r=map(int,input().split())
            print(int(fare[p][q]) if r==0 else int(time[p][q]))


#main()