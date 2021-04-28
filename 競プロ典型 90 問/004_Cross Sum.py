# 004 - Cross Sumiš2j

H,W=map(int,input().split())
A=[list(map(int,input().split())) for _ in range(H)]

# H=4
# W=4
# A=[[3, 1, 4, 1], [5, 9, 2, 6], [5, 3, 5, 8], [9, 7, 9, 3]]

row_sum=[sum(r) for r in A]

col_sum=[]
for i in range(W):
    t=0
    for j in range(H):
       t=t+A[j][i]
    col_sum.append(t)

# print(row_sum)
# print(col_sum)

ans=[]
for i in range(H):
    t=[row_sum[i]]*W
    for j in range(W):
       t[j]=t[j]+col_sum[j]-A[i][j]
    ans.append(t)
    
for a in ans:
    print(' '.join(map(str,a)))