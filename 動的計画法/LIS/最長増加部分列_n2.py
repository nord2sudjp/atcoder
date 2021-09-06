# D - トランプ挿入ソート
# https://www.youtube.com/watch?v=CE2b_-XfVDk
https://www.youtube.com/watch?v=fV-TF4OvZpk&t=544s

# N=5
# S=[4,2,3,1,5]

N=int(input())
S=[int(input()) for _ in range(N)]


DP=[1]*N
for i in range(1,N):
    for j in range(0,i):
        if S[j]<S[i]:
            #print(S[j],S[i])
            #DP[i]=max(DP[i], DP[j]+1)
            nnp=DP[j]+1
            if DP[i]<nnp:
                DP[i]=nnp
           
print(N-max(DP))