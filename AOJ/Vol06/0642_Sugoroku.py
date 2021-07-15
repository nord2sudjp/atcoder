# 0642 Sugoroku

# 1を連続で増やしていった時に必要な双六がどのように変化するかを見ればよい。
# 0が連続しているところは必ずある値, 例 1で進んでいけばよいので制約条件はない

# コーナーケース
# すべて0

# N=10
# A=[0,1,1,0,0,0,1,1,1,0]

N=int(input())
*A,=list(map(int,input().split()))

ans=0
for i in range(N):
    for j in range(i,N):
        res=True
        for k in range(i,j+1):
            if A[k]==0:
                res=False
                break
            
        if res:
            #print(i,j)
            ans=max(ans,j-i+1)

print(ans+1)