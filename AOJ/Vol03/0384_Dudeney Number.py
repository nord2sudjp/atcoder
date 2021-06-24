# 0384

# A=16
# N=2
# M=1000

A,N,M=map(int,input().split())

MAXM=int(M**(1/N))
#print(MAXM)

ans=0
for i in range(1,MAXM+1):
    s=i**N
    sx=s
    t=0
    while sx>=1:
       t+=sx%10
       sx=sx//10
    if i==t+A:
        ans+=1
        #print(i,s,t,sx)
print(ans)