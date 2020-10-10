#
N,W=map(int,input().split())
P=[list(map(int, input().split())) for _ in range(N)]

save=[[-1]*(W) for _ in range(N)]

def kp(i,w):
    if N<i or w<=0: return 0 # python‚Å‚Í-1‚É‚È‚é‚Æ”z—ñ‚ğ‰E‚©‚çæ“¾‚·‚é
    if 0 <= save[i-1][w-1]: return save[i-1][w-1]
    ans=0
    value, weight=P[i-1]
    if w < weight:
        ans=kp(i+1,w)
    else:
        ans=max(kp(i+1,w), kp(i+1,w-weight)+value)
    save[i-1][w-1] = ans
    return ans

print(kp(1,W))



#
N,W=map(int,input().split())
P=[list(map(int, input().split())) for _ in range(N)]

mem=[[0]*(W+2) for _ in range(N+2)]

for i in range(N,0,-1):
    for w in range(0,W+1):
        value, weight=P[i-1]
        if w < weight:
            mem[i][w] =mem[i+1][w]
        else:
            mem[i][w]=max(mem[i+1][w], mem[i+1][w-weight]+value)
print(mem[1][W])