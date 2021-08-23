# B

import collections
N,K=map(int,input().split())
*A,=list(map(int,input().split()))

# N,K=4,2
# A=[0,1,0,3]
# N,K=20,4
# A=[6, 2, 6, 8, 4, 5, 5, 8, 4, 1, 7, 8, 0, 3, 6, 1, 1, 8, 3, 0]
#A=sorted(A)
#print(A)

maxa=max(A)
DP=[]
c=(collections.Counter(A))

for k,v in c.items():
    if v>K:c[k]=K

#print(c)
ans={}
t=c.get(0,-1)
if t!=-1:
    ans[0]=t
    for i in range(1,maxa+1):
        cur=c.get(i,-1)
        if cur==-1:break
        prv=ans[i-1]
        #print(i,cur,prv)
        ans[i]=min(cur,prv)
print(sum(ans.values()))