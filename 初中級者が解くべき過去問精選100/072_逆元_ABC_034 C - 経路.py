#
W,H=map(int,input().split())

MOD=1000000007
# Ž®
# (w+h-2)C(w-1)
# (H+W-2)! / (H-1)!(W-1)!

n=W+H-2
r=W-1

bunbo=1
bunshi=1
for i in range(r):
    bunbo=bunbo*(n-i)%MOD
    bunshi=bunshi*(i+1)%MOD
    # ‚±‚±‚ªbunbo*=(n-i)%MOD‚¾‚ÆTLE‚É‚È‚é

ans=bunbo*pow(bunshi,MOD-2,MOD)%MOD
print(ans)


#
W,H=map(int,input().split())

def pow_x(N,P,M):
    # N^P mod M
    
    if P==0: return 1 
    if P%2==0:
        t=pow_x(N,P//2,M)
        return (t*t)%M
    else:
        return N*pow_x(N, P-1, M)

def pow_x1(N,P,M):
    # N^P mod M
    
    if P==0: return 1 
    if P%2==0:
        t=pow_x1(N,P//2,M)
        return (t*t)%M
    else:
        return N*pow_x1(N, P-1, M)
    
MOD=1000000007
# Ž®
# (H+W-2)! / (H-1)!(W-1)!

bunbo=1
for i in range(H+W-2,0,-1):
    bunbo=bunbo*i%MOD

bunshi_h=1
for i in range(H-1,0,-1):
    bunshi_h=bunshi_h*i%MOD

bunshi_w=1
for i in range(W-1,0,-1):
    bunshi_w=bunshi_w*i%MOD

bunshi_h=pow_x1(bunshi_h,(MOD-2),MOD)
bunshi_w=pow_x1(bunshi_w,(MOD-2),MOD)
ans=bunbo*bunshi_h*bunshi_w%MOD
print(ans)
