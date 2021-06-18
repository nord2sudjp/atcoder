# 301 Baton Relay Game

N,M,Q=map(int,input().split())
*A,=list(map(int,input().split()))
*Q,=list(map(int,input().split()))

# N=10
# M=5
# Q=3

# A=[2,6,5,18,3]
# Q=[3,0,5]

F=[1]*N
prev=[0]*N
for i in range(N):
    prev[i]=(i-1+N)%N
    
next=[0]*N
for i in range(N):
    next[i]=(i+1+N)%N
    
#print(prev,next)

cur=0
for a in A:
    if a%2==0:
        for _ in range(a):
            cur=next[cur]
    else:
        for _ in range(a):
            cur=prev[cur]
    F[cur]=0
    prev[next[cur]]=prev[cur]
    next[prev[cur]]=next[cur]
    cur=next[cur]
    #print(prev,next,F)

for q in Q:
    print(F[q])