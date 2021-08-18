# 058 Original Calculator


N,K=map(int,input().split())

# N=5
# K=3

MAXN=MOD=10**5
#DP=[-1]*MAXN

def solve(N):
    T=N
    DP=[-1]*MAXN

    count=1
    while True:
        t=N
        t_ans=0
        while t>=1:
            t_ans+=t%10
            t=t//10
            #print(i,N,t_ans)
        #print(count,N,t_ans,(N+t_ans)%MOD)
        N=(N+t_ans)%MOD
        if DP[N]!=-1:break
        DP[N]=count
        count+=1
        
    
    head=DP[N]
    cycle=count-head
    #print("T={},N={},DP[N]={},head={},count={},cycle={}".format(T,N,DP[:10],head,count,cycle))
    return head,cycle,DP


head,cycle,DP=solve(N)

# for i in range(2,1000):
#     head,cycle,count,DP=solve(i)
#     print(i,head,cycle)
# head,cycle,count,DP=solve(N)

d={}
for i,x in enumerate(DP):
    if x!=-1:
        d[x]=i

if K<head:
    print(d[K])
else:
    #print(K,head,cycle,(K-head)%cycle)
    K=K-head
    K=K%cycle
    print(d[K+head])