# 0340 Pancake

# N=3
# P=[1,2,1]
N=int(input())
*P,=list(map(int,input().split()))


f_ans=float('inf')
for s in range(0,P[0]+1):
    ans=0
    q=P[:]
    #print(q)
    q[0]=q[0]-s
    ans+=s
    #print(q,ans)
    for i in range(N-1):
        t=q[i]
        ans+=t
        q[i]=0

        ans+=t
        q[i+1]=max(q[i+1]-t,0)
        #print(q,t,ans)
    ans+=q[-1] # don't forget to add right value.
    if f_ans > ans:
        f_ans=ans
print(f_ans)