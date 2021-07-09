# 0631 Point Card

N,M=map(int,input().split())
A=[list(map(int,input().split())) for _ in range(M)]


# N=4
# M=5
# A=[[1, 7], [6, 2], [3, 5], [4, 4], [0, 8]]

ans=0
p=[]
for m in range(M):
    a,b=A[m]
    if a>=N:
        ans+=1
    else:
        p.append(b-N)
if ans>=M-1:
    print(0)
else:
    t=(M-1)-ans
    p.sort()
    print(sum(p[:t]))