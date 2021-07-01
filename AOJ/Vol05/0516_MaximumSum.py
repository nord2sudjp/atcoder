# 0516 Maximum Sum

# N=5
# M=3

# S=[2,5,-4,10,3]

while True:
    N,M=map(int,input().split())
    if N==M==0:
        break
        
    S=[]
    for _ in range(N):
        S.append(int(input()))
    t=ans=sum(S[:M])

    for i in range(M,N):
        #print(ans,ans-S[i-M]+S[i],S[i-M],S[i])
        t=t-S[i-M]+S[i]
        # t=ans-S[i-M]+S[i]
        if ans<t:
            ans=t

    print(ans) 