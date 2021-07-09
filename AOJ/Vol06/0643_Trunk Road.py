# 0643 Trunk Road

H,W=map(int,input().split())
A=[list(map(int,input().split())) for _ in range(H)]


def solve(H,W,ph,pw,A):
    t=0
    for i in range(H):
        for j in range(W):
                #print((i,j),abs(ph-i),abs(pw-j))
                t+=min(abs(ph-i),abs(pw-j))*A[i][j]
    return t

# H=3
# W=5
# A=[[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]



ans=float('inf')

for h in range(H):
     for w in range(W):
        t=solve(H,W,h,w,A)
        if ans>t:
            ans=t

        
print(ans)