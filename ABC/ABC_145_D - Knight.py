X,Y=map(int,input().split())

def comb(n,r,mod):
    k=min(r,n-r)
    C=1
    for i in range(1,k+1):
        C=(C*(n+1-i)*pow(i,mod-2,mod))%mod
    return C

if (X+Y)%3!=0:
    print(0)
    exit()

n=(X+Y)//3
X-=n
Y-=n
P=10**9+7
if (X<0) or (Y<0):
    print(0)
    exit()
print(comb(X+Y,X,P))