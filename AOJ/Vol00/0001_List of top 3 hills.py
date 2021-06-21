# 0001:List of top 3 hills.
N=10

A=[int(input()) for _ in range(N)]
A=sorted(A,reverse=True)
for i in range(3):
    print(A[i])