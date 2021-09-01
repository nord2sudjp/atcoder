# 051 - Typical Shop（★5） AC

# dictionaryで別にカウントを計算していた
# リストの多次元配列に組み替え
# 一次元にしたらもっと早いかもしれない。
# cntをループの中で判断→cntをグループにしてしまい一括で処理する

import bisect
N,K,P=map(int,input().split())
*A,=list(map(int,input().split()))

# N,K,P=5, 2, 10
# A=[8, 3, 7, 5, 11]

# N,K,P=5,1,10
# A=[7,7,7,7,7]

A1=A[:N//2]
A2=A[N//2:]


l_a=len(A1)
t1=[[] for _ in range(K+1)]
for i in range(2**l_a): 
    t=0
    cnt=0
    for j in range(l_a): 
        if (i>>j&1):
            cnt=cnt+1
            t=t+A1[j]
    if cnt<=K:
        t1[cnt].append(t)

l_a=len(A2)
t2=[[] for _ in range(K+1)]
for i in range(2**l_a): 
    t=0
    cnt=0
    for j in range(l_a): 
        if (i>>j&1):
            cnt=cnt+1
            t=t+A2[j]
    if cnt<=K:
        t2[cnt].append(t)


for t in t1:t.sort()
for t in t2:t.sort()    
    
# print(t1)
# print(t2)    
    

ans=0
for cnt in range(K+1):
    cnt_zan=K-cnt
#     print('='*10)
#     print(K,cnt,cnt_zan,t1[cnt],t2[cnt_zan])
#     print('-'*10)
    for j in t1[cnt]:
        if j>P:continue
        s=bisect.bisect_right(t2[cnt_zan],P-j)
#         print(j,P-j,s)
        ans=ans+s
print(ans)


# 051 - Typical Shop（★5） TLE

import bisect
N,K,P=map(int,input().split())
*A,=list(map(int,input().split()))

# N,K,P=5, 2, 10
# A=[3, 8, 7, 5, 11]

A1=A[:N//2]
A2=A[N//2:]


l_a=len(A1)
t1=[[] for _ in range(K+1)]
d1={}
for i in range(2**l_a): 
    t=0
    cnt=0
    for j in range(l_a): 
        if (i>>j&1):
            cnt=cnt+1
            t=t+A1[j]
    t1.append(t)
    d1[t]=cnt

l_a=len(A2)
t2=[]
d2={}
for i in range(2**l_a): 
    t=0
    cnt=0
    for j in range(l_a): 
        if (i>>j&1):
            cnt=cnt+1
            t=t+A2[j]
    t2.append(t)
    d2[t]=cnt

t1=sorted(t1)
t2=sorted(t2)

#print(t1,d1,t2,d2)

ans=0
for i in t1:
    zan=P-i
    cnt1=K-d1[i]
    s=bisect.bisect_right(t2,zan)
    for j in range(s):
        cnt2=d2[t2[j]]
        #print(i,zan,s,j,t2[j],cnt1+cnt2)
        if cnt1==cnt2:
            ans=ans+1
print(ans)